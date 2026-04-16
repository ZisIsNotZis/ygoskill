#!/bin/env python
"""ydkcheck.py — 卡组量化检查工具

用法:
  ./ydkcheck.py deck.ydk                  单卡组全检查
  ./ydkcheck.py deck.ydk --section basic  只查基础
  ./ydkcheck.py deck.ydk --section lflist 只查禁限
  ./ydkcheck.py deck.ydk --section extra  只查额外
  ./ydkcheck.py deck.ydk --section start  只查T0/T1起手
  ./ydkcheck.py deck.ydk --section all    全检查(默认)
  N_SAMPLES=200 ./ydkcheck.py deck.ydk    起手模拟次数(默认500)

返回码: 0=全部通过, 1=有错误, 2=有警告但不致命
"""
from sqlite3 import connect
from sys import argv
from os import getenv
from itertools import combinations
from collections import Counter
from random import shuffle
import re

# ── 常量 ──
TYPE_MONSTER = 0x1
TYPE_SPELL = 0x2
TYPE_TRAP = 0x4
TYPE_EFFECT = 0x20
TYPE_FUSION = 0x40
TYPE_SYNCHRO = 0x2000
TYPE_XYZ = 0x800000
TYPE_LINK = 0x4000000
TYPE_TOKEN = 0x10000000
EXTRA_MASK = 0x4802040  # fusion|synchro|xyz|link|token

RACE = '战士 魔法师 天使 恶魔 不死 机械 水 炎 岩石 鸟兽 植物 昆虫 雷 龙 兽 兽战士 恐龙 鱼 海龙 爬虫类 念动力 幻神兽 创造神 幻龙 电子界 幻想魔'.split(' ')
ATTRIBUTE = '地水炎风光暗神'
TYPE_NAMES = ' 魔法 陷阱  通常  融合 仪式  灵魂 同盟 二重 调整 同调   速攻 永续 装备 场地 反击 反转 卡通 超量 灵摆  连接'.split(' ')
LINK_DIR = '↙↓↘←-→↖↑↗'

# ── 数据库加载 ──


def load_db():
    con = connect('cards.cdb')
    cur = con.cursor()
    cur.execute('select datas.id,alias,name,type,setcode,attribute,race,level,atk,def,desc from datas join texts on datas.id=texts.id')
    cards = {}
    for row in cur.fetchall():
        cid, alias, name, typ, setcode, attr, race, lvl, atk, df, desc = row
        cards[cid] = {
            'id': cid, 'alias': alias, 'name': name, 'type': typ,
            'setcode': setcode, 'attribute': attr, 'race': race,
            'level': lvl, 'atk': atk, 'def': df, 'desc': desc,
            'is_extra': bool(typ & EXTRA_MASK),
            'is_monster': bool(typ & TYPE_MONSTER),
            'is_spell': bool(typ & TYPE_SPELL),
            'is_trap': bool(typ & TYPE_TRAP),
            'is_fusion': bool(typ & TYPE_FUSION),
            'is_synchro': bool(typ & TYPE_SYNCHRO),
            'is_xyz': bool(typ & TYPE_XYZ),
            'is_link': bool(typ & TYPE_LINK),
        }
    con.close()
    return cards


def load_lflist():
    """返回 {card_id: limit} limit: 0=禁,1=限1,2=限2"""
    lf = {}
    try:
        text = open('lflist.conf').read()
        sections = text.split('\n\n')
        if sections:
            first = sections[0]
            for line in first.split('\n'):
                if line and line[0] not in '#!':
                    parts = line.split()
                    if len(parts) >= 2:
                        lf[int(parts[0])] = int(parts[1])
    except FileNotFoundError:
        pass
    return lf

# ── YDK解析 ──


def parse_ydk(path):
    main_deck, extra_deck, side_deck = [], [], []
    section = None
    with open(path, 'rb') as f:
        for line in f.read().split():
            token = line.decode('utf-8', errors='ignore')
            if token == '#main':
                section = 'main'
            elif token == '#extra':
                section = 'extra'
            elif token == '!side':
                section = 'side'
            elif token.isdigit() and section:
                cid = int(token)
                if section == 'main':
                    main_deck.append(cid)
                elif section == 'extra':
                    extra_deck.append(cid)
                elif section == 'side':
                    side_deck.append(cid)
    return main_deck, extra_deck, side_deck

# ── 检查结果收集 ──


class CheckResult:
    def __init__(self):
        self.errors = []
        self.warnings = []
        self.infos = []

    def error(self, msg):
        self.errors.append(f"  [ERROR] {msg}")

    def warn(self, msg):
        self.warnings.append(f"  [WARN] {msg}")

    def info(self, msg):
        self.infos.append(f"  [INFO] {msg}")

    def ok(self, msg):
        self.infos.append(f"  [OK] {msg}")

    def passed(self):
        return len(self.errors) == 0

    def __str__(self):
        lines = []
        for m in self.infos + self.warnings + self.errors:
            lines.append(m)
        return '\n'.join(lines)

# ── 检查函数 ──


def check_basic(main_deck, extra_deck, cards, lf):
    """基础计数检查"""
    r = CheckResult()
    r.info(f"=== 基础计数检查 ===")

    # Main deck size
    main_count = len(main_deck)
    if 40 <= main_count <= 60:
        r.ok(f"主卡组={main_count}张 (40-60范围内)")
    else:
        r.error(f"主卡组={main_count}张, 必须在40-60之间")

    if main_count < 40:
        r.error(f"主卡组<40张, 无法构成合法卡组")
    elif 40 <= main_count <= 44:
        r.ok(f"主卡组在推荐范围40-44内, 抽核心最稳定")
    elif main_count > 44:
        r.warn(f"主卡组={main_count}>44, 抽核心概率降低, 确认理由充分")

    # Extra deck size
    extra_count = len(extra_deck)
    if extra_count == 0:
        r.info(f"额外卡组=0张 (纯主卡组构筑, 确认是有意为之)")
    elif 12 <= extra_count <= 15:
        r.ok(f"额外卡组={extra_count}张 (12-15范围内)")
    elif extra_count < 12:
        r.warn(f"额外卡组={extra_count}<12, 推荐12-15张, 确认理由充分")
    elif extra_count > 15:
        r.error(f"额外卡组={extra_count}>15, 超过上限")

    # Total
    r.info(f"总卡数={main_count + extra_count}张")
    return r


def check_duplicates(main_deck, extra_deck, cards, lf):
    """同名卡检查(含alias处理)"""
    r = CheckResult()
    r.info(f"=== 同名卡检查 ===")

    # 合并卡组
    all_cards = main_deck + extra_deck

    # 构建 name->count 和 alias 映射
    name_counts = Counter()
    alias_groups = {}  # alias_id -> [card_ids]
    card_names = {}

    for cid in all_cards:
        c = cards.get(cid)
        if not c:
            r.error(f"未知卡片id={cid}")
            continue

        card_names[cid] = c['name']
        # 确定"同名"的key: 用alias(如果alias≠0且与id差>10)或id
        alias = c['alias']
        if alias != 0 and abs(cid - alias) > 10:
            key = alias
        else:
            key = cid

        if key not in alias_groups:
            alias_groups[key] = []
        alias_groups[key].append(cid)
        name_counts[key] += 1

    # 检查超限
    violated = False
    for key, count in sorted(name_counts.items(), key=lambda x: -x[1]):
        if count > 3:
            name = cards[key]['name'] if key in cards else card_names.get(key, str(key))
            members = alias_groups[key]
            member_names = set(card_names[c] for c in members if c in card_names)
            r.error(f"'{name}' 出现{count}次(>3), 违反同名规则")
            violated = True

    if not violated:
        r.ok("所有同名卡≤3张")

    # 显示接近上限的
    near_limit = [(k, c) for k, c in name_counts.items() if c == 3]
    if near_limit:
        names = [cards[k]['name'] if k in cards else str(k) for k, _ in near_limit[:5]]
        r.info(f"已达3张上限: {', '.join(names)}")

    return r


def check_lflist(main_deck, extra_deck, cards, lf):
    """禁限卡表检查"""
    r = CheckResult()
    r.info(f"=== 禁限卡表检查 ===")

    if not lf:
        r.warn("lflist.conf未找到或无数据, 跳过禁限检查")
        return r

    all_cards = main_deck + extra_deck
    counts = Counter(all_cards)

    violated = False
    for cid, count in counts.items():
        # 优先查alias的lim
        c = cards.get(cid)
        if not c:
            continue
        check_id = cid
        if c['alias'] != 0 and c['alias'] in lf:
            check_id = c['alias']
        elif cid in lf:
            check_id = cid
        else:
            continue

        if check_id not in lf:
            continue

        limit = lf[check_id]
        name = c['name']
        if limit == 0:
            r.error(f"'{name}' 是禁卡(lim0), 不能携带")
            violated = True
        elif limit == 1 and count > 1:
            r.error(f"'{name}' 限1(lim1), 当前带{count}张")
            violated = True
        elif limit == 2 and count > 2:
            r.error(f"'{name}' 限2(lim2), 当前带{count}张")
            violated = True

    if not violated:
        r.ok("所有卡片符合禁限卡表")

    # 显示带了的限卡
    limited_cards = []
    for cid in set(all_cards):
        c = cards.get(cid)
        if not c:
            continue
        check_id = c['alias'] if (c['alias'] != 0 and c['alias'] in lf) else cid
        if check_id in lf:
            lim = lf[check_id]
            limited_cards.append((c['name'], lim, counts[cid]))

    if limited_cards:
        for name, lim, cnt in sorted(limited_cards):
            r.info(f"限卡: '{name}' lim{lim} 携带{cnt}张")

    return r


def check_card_types(main_deck, extra_deck, cards, lf):
    """卡片类型比例检查"""
    r = CheckResult()
    r.info(f"=== 卡片类型比例 ===")

    monsters = [c for c in main_deck if (cards.get(c) or {}).get('is_monster', False)]
    spells = [c for c in main_deck if (cards.get(c) or {}).get('is_spell', False)]
    traps = [c for c in main_deck if (cards.get(c) or {}).get('is_trap', False)]
    total = len(main_deck)

    r.info(f"主卡组怪兽: {len(monsters)}/{total} ({len(monsters)/total*100:.0f}%)")
    r.info(f"主卡组魔法: {len(spells)}/{total} ({len(spells)/total*100:.0f}%)")
    r.info(f"主卡组陷阱: {len(traps)}/{total} ({len(traps)/total*100:.0f}%)")

    # 额外类型
    if extra_deck:
        fusions = [c for c in extra_deck if (cards.get(c) or {}).get('is_fusion', False)]
        synchros = [c for c in extra_deck if (cards.get(c) or {}).get('is_synchro', False)]
        xyzs = [c for c in extra_deck if (cards.get(c) or {}).get('is_xyz', False)]
        links = [c for c in extra_deck if (cards.get(c) or {}).get('is_link', False)]
        total_extra = len(extra_deck)

        r.info(f"额外融合: {len(fusions)}/{total_extra}")
        r.info(f"额外同调: {len(synchros)}/{total_extra}")
        r.info(f"额外超量: {len(xyzs)}/{total_extra}")
        r.info(f"额外连接: {len(links)}/{total_extra}")

        if len(links) == 0 and total_extra > 0:
            r.warn("额外无连接怪兽, 可能缺少Link跳板")
        if len(links) >= 2:
            r.ok(f"额外有{len(links)}张连接怪兽, Link跳板充足")

    # 怪兽内型
    if monsters:
        effects = [c for c in monsters if (cards.get(c) or {}).get('type', 0) & TYPE_EFFECT]
        normals = [c for c in monsters if not ((cards.get(c) or {}).get('type', 0) & TYPE_EFFECT)]
        r.info(f"怪兽中效果: {len(effects)}, 通常: {len(normals)}")

    return r


def check_extra_summonability(extra_deck, main_deck, cards, lf):
    """额外怪兽可召唤性检查"""
    r = CheckResult()
    r.info(f"=== 额外怪兽可召唤性 ===")

    if not extra_deck:
        r.info("额外卡组为空, 跳过")
        return r

    # 获取主卡组的系列(setcode)
    main_setcodes = set()
    main_races = set()
    main_attributes = set()
    main_levels = set()
    for cid in main_deck:
        c = cards.get(cid)
        if c:
            sc = c['setcode']
            if sc:
                for i in range(0, 64, 16):
                    main_setcodes.add((sc >> i) & 0xFFFF)
            main_races.add(c['race'])
            main_attributes.add(c['attribute'])
            main_levels.add(c['level'] >> 24 if c['type'] & 0x1000000 else c['level'])

    unsummonable = []
    for cid in extra_deck:
        c = cards.get(cid)
        if not c:
            unsummonable.append((cid, "未知卡片"))
            continue

        desc = c.get('desc', '')
        # 简单启发式: 如果extra怪兽的setcode完全不在main中出现, 且desc中没有明显的配合
        extra_setcodes = set()
        sc = c['setcode']
        if sc:
            for i in range(0, 64, 16):
                extra_setcodes.add((sc >> i) & 0xFFFF)

        # 泛用额外(无setcode或setcode非常宽泛)跳过
        if not extra_setcodes:
            continue

        # 检查是否有overlap
        overlap = extra_setcodes & main_setcodes
        if not overlap:
            # 可能是泛用卡(如S:P小夜/独角兔等有非常宽泛的召唤条件)
            # 检查是否是连接怪兽且召唤条件宽泛
            if c['is_link']:
                # Link怪兽通常只需要效果怪兽, 可能是泛用的
                pass
            elif c['is_synchro']:
                # 同调需要调整, 如果main没调整则有问题
                has_tuner = any((cards.get(mc) or {}).get('type', 0) & 0x1000 for mc in main_deck)
                if not has_tuner:
                    unsummonable.append((cid, f"{c['name']}是同调怪兽但主卡组无调整"))
            elif c['is_xyz']:
                # 超量需要同等级怪兽
                r.info(f"'{c['name']}' 是超量怪兽, 确认主卡组有对应等级")
            elif c['is_fusion']:
                r.info(f"'{c['name']}' 是融合怪兽, 确认有融合召唤手段")

    if unsummonable:
        for cid, reason in unsummonable:
            name = cards.get(cid, {}).get('name', str(cid))
            r.warn(f"'{name}': {reason}")
    else:
        r.ok("未发现明显无法召唤的额外怪兽")

    r.info("注意: 精确召唤条件需人工阅读效果文本确认")
    return r


def check_t0t1_start(main_deck, cards, lf, n_samples=None):
    """T0/T1起手率模拟"""
    r = CheckResult()
    r.info(f"=== T0/T1起手率检查 ===")

    if n_samples is None:
        n_samples = int(getenv('N_SAMPLES', 500))

    if len(main_deck) < 5:
        r.error("主卡组<5张, 无法模拟起手")
        return r

    # 分类卡片
    starters = []  # 能启动的卡: 核心本家/展开支援/检索
    handtraps = []  # 手坑
    negates = []  # 康/无效
    starters_set = set()
    handtraps_set = set()

    for cid in main_deck:
        c = cards.get(cid)
        if not c:
            continue
        desc = c.get('desc', '')
        name = c['name']

        # 手坑检测: 从手卡发动 + 对方相关 + 干扰
        is_ht = False
        if c['is_monster']:
            # 从手卡发动: "从手卡丢弃" / "从手卡送去墓地" / "从手卡特殊召唤"
            from_hand = '从手卡' in desc or '手卡丢弃' in desc
            # 干扰对方: 无效/除外/破坏/阻止/抽卡(资源压制)
            disrupt = any(kw in desc for kw in ['无效', '除外', '破坏', '不能', '抽1张', '回到手卡'])
            # 对方相关: 对方场上/对方墓地/对方回合/对方效果
            vs_opp = '对方' in desc
            if from_hand and disrupt and vs_opp:
                # 排除纯检索/展开(只有检索没有干扰)
                if not (any(kw in desc for kw in ['加入手卡', '从卡组加入']) and
                        not any(kw in desc for kw in ['无效', '除外', '破坏', '不能'])):
                    is_ht = True
        if c['is_trap']:
            # 陷阱从手卡发动: "从手卡也能" / "手卡发动"
            if ('从手卡' in desc or '手卡也能' in desc) and \
               any(kw in desc for kw in ['无效', '除外', '破坏', '不能']):
                is_ht = True

        if is_ht:
            handtraps.append(cid)
            handtraps_set.add(cid)

        # 启动卡: 检索/堆墓/特招/展开
        if c['is_monster'] or c['is_spell']:
            if any(kw in desc for kw in ['检索', '卡组', '特殊召唤', '送去墓地', '抽卡', '场上']):
                starters.append(cid)
                starters_set.add(cid)

    # 如果starters太少, 用更宽松的判定
    if len(starters) < 8:
        starters = [c for c in main_deck if c not in handtraps_set]

    r.info(f"启动卡: {len(starters)}/{len(main_deck)}张")
    r.info(f"手坑: {len(handtraps)}/{len(main_deck)}张")

    # 模拟
    deck = list(main_deck)
    t0_starts = 0
    t1_starts = 0
    t2_starts = 0

    for _ in range(n_samples):
        shuffle(deck)
        hand = set(deck[:5])

        hand_starter_count = len(hand & starters_set)
        hand_ht_count = len(hand & handtraps_set)

        # T0: 起手有≥2张启动卡 或 (≥1启动+≥1手坑)
        if hand_starter_count >= 2 or (hand_starter_count >= 1 and hand_ht_count >= 1):
            t0_starts += 1
        # T1: 起手有≥1张启动卡
        elif hand_starter_count >= 1:
            t1_starts += 1
        # T2: 无启动卡
        else:
            t2_starts += 1

    t0_rate = t0_starts / n_samples * 100
    t1_rate = (t0_starts + t1_starts) / n_samples * 100
    t2_rate = t2_starts / n_samples * 100

    r.info(f"T0起手率(≥2启动或1启动+1手坑): {t0_rate:.1f}%")
    r.info(f"T1累计起手率(T0+有1启动): {t1_rate:.1f}%")
    r.info(f"T2无法起手率: {t2_rate:.1f}%")

    if t1_rate >= 80:
        r.ok(f"T1累计起手率{t1_rate:.1f}%≥80%, 通过")
    elif t1_rate >= 60:
        r.warn(f"T1累计起手率{t1_rate:.1f}%<80%, 可能频繁卡手")
    else:
        r.error(f"T1累计起手率{t1_rate:.1f}%<60%, 严重卡手, 不建议使用")

    if t0_rate >= 50:
        r.ok(f"T0起手率{t0_rate:.1f}%≥50%, 先攻能力强")
    elif t0_rate >= 30:
        r.info(f"T0起手率{t0_rate:.1f}%, 先攻能力一般")
    else:
        r.warn(f"T0起手率{t0_rate:.1f}%<30%, 先攻较弱")

    if t2_rate > 20:
        r.warn(f"T2率{t2_rate:.1f}%>20%, 超过1/5概率完全无法启动")

    return r


def check_card_usability(main_deck, extra_deck, cards, lf):
    """卡片可用性粗略检查"""
    r = CheckResult()
    r.info(f"=== 卡片可用性检查 ===")

    all_cards = main_deck + extra_deck
    issues = []

    for cid in all_cards:
        c = cards.get(cid)
        if not c:
            issues.append(f"id={cid}: 未知卡片, 请确认是否存在")
            continue

        desc = c.get('desc', '')
        name = c['name']

        # 检查明显需要cost/素材的卡
        # 需要除外区有大量卡的
        if '除外' in desc and any(kw in desc for kw in ['除外区', '除外']):
            # 粗略检查: 如果卡组没有除外手段
            pass  # 过于复杂, 仅提示

        # 需要特定种族在场
        if '必须' in desc or '需要' in desc:
            # 简单提示
            pass

    if issues:
        for issue in issues:
            r.warn(issue)
    else:
        r.info("未发现明显不可用的卡片")

    r.info("注意: 精确的cost/素材/发动条件检查需要人工阅读效果文本")
    r.info("以下卡片建议重点检查:")

    # 列出可能需要特定条件的卡
    for cid in all_cards:
        c = cards.get(cid)
        if not c:
            continue
        desc = c.get('desc', '')
        # 需要LP支付的
        if 'LP' in desc or '基本分' in desc:
            if '支付' in desc:
                r.info(f"  '{c['name']}': 需要支付LP, 确认资源管理")

    return r


def check_quality_score(main_deck, extra_deck, cards, lf):
    """质量评分"""
    r = CheckResult()
    r.info(f"=== 质量评分 ===")

    scores = {}

    # 核心完整度(25%)
    # 用简单启发式: main中怪兽数量作为代理
    monsters = [c for c in main_deck if (cards.get(c) or {}).get('is_monster', False)]
    core_count = len(monsters)
    if core_count >= 15:
        scores['core'] = 5
    elif core_count >= 12:
        scores['core'] = 3
    else:
        scores['core'] = 1
    r.info(f"核心完整度: {scores['core']}/5 (怪兽数={core_count})")

    # 手坑覆盖(20%)
    ht_count = 0
    ht_types = set()
    for cid in main_deck:
        c = cards.get(cid)
        if not c:
            continue
        desc = c.get('desc', '')
        name = c['name']
        # 改进的手坑检测
        is_ht = False
        if c['is_monster']:
            from_hand = '从手卡' in desc
            disrupt = any(kw in desc for kw in ['无效', '除外', '破坏', '不能', '抽1张'])
            vs_opp = '对方' in desc
            if from_hand and disrupt and vs_opp:
                is_ht = True
        if c['is_trap']:
            if ('从手卡' in desc or '手卡也能' in desc) and \
               any(kw in desc for kw in ['无效', '除外', '破坏', '不能']):
                is_ht = True
        if is_ht:
            ht_count += 1
            if '灰' in name or '灰流丽' in name:
                ht_types.add('ash')
            if 'G' in name or '增殖' in name:
                ht_types.add('g')
            if '墓穴' in name or '指名' in name:
                ht_types.add('nb')
            if '泡影' in name:
                ht_types.add('veiler')
            ht_types.add('other')

    if ht_count >= 9 and len(ht_types) >= 3:
        scores['handtrap'] = 5
    elif ht_count >= 6 and len(ht_types) >= 2:
        scores['handtrap'] = 3
    else:
        scores['handtrap'] = 1
    r.info(f"手坑覆盖: {scores['handtrap']}/5 ({ht_count}张, {len(ht_types)}种)")

    # 额外可用性(15%)
    extra_count = len(extra_deck)
    if 12 <= extra_count <= 15:
        scores['extra'] = 5
    elif 10 <= extra_count <= 11:
        scores['extra'] = 3
    else:
        scores['extra'] = 1
    r.info(f"额外可用性: {scores['extra']}/5 (额外={extra_count})")

    # 先攻阻抗(15%) - 用康/无效卡数量估算
    negate_count = 0
    for cid in main_deck + extra_deck:
        c = cards.get(cid)
        if not c:
            continue
        desc = c.get('desc', '')
        if '无效' in desc or '康' in desc or '效果不发动' in desc:
            negate_count += 1

    if negate_count >= 6:
        scores['first_negate'] = 5
    elif negate_count >= 4:
        scores['first_negate'] = 3
    else:
        scores['first_negate'] = 1
    r.info(f"先攻阻抗估算: {scores['first_negate']}/5 (康/无效相关={negate_count})")

    # 妥协能力(10%)
    scores['compromise'] = 3  # 默认, 需要更多信息
    r.info(f"妥协能力: {scores['compromise']}/5 (需实战验证)")

    # 后攻突破(10%)
    break_count = 0
    for cid in main_deck:
        c = cards.get(cid)
        if not c:
            continue
        desc = c.get('desc', '')
        if any(kw in desc for kw in ['破坏', '除外', '弹回', '回手', '返回卡组']):
            break_count += 1

    if break_count >= 4:
        scores['break'] = 5
    elif break_count >= 2:
        scores['break'] = 3
    else:
        scores['break'] = 1
    r.info(f"后攻突破估算: {scores['break']}/5 (解场相关={break_count})")

    # 共识匹配(5%) - 需要ydkshow数据, 这里默认
    scores['consensus'] = 3
    r.info(f"共识匹配: {scores['consensus']}/5 (需ydkshow对比)")

    # 加权总分
    weights = {'core': 0.25, 'handtrap': 0.20, 'extra': 0.15,
               'first_negate': 0.15, 'compromise': 0.10, 'break': 0.10, 'consensus': 0.05}
    total = sum(scores[k] * weights[k] for k in scores) * 20  # scale 1-5 to 0-100
    r.info(f"质量总分: {total:.0f}/100")

    if total >= 80:
        r.info("评级: 大师级")
    elif total >= 60:
        r.info("评级: 竞技级")
    elif total >= 40:
        r.info("评级: 可用")
    else:
        r.warn("评级: 建议重做")

    return r

# ── 主函数 ──


def run_checks(ydk_path, section='all'):
    cards = load_db()
    lf = load_lflist()
    main_deck, extra_deck, side_deck = parse_ydk(ydk_path)

    all_checks = CheckResult()
    print(f"\n卡组: {ydk_path}")
    print(f"主卡组: {len(main_deck)}张 | 额外: {len(extra_deck)}张 | 副卡组: {len(side_deck)}张\n")

    checks = {
        'basic': lambda: check_basic(main_deck, extra_deck, cards, lf),
        'duplicates': lambda: check_duplicates(main_deck, extra_deck, cards, lf),
        'lflist': lambda: check_lflist(main_deck, extra_deck, cards, lf),
        'types': lambda: check_card_types(main_deck, extra_deck, cards, lf),
        'extra': lambda: check_extra_summonability(extra_deck, main_deck, cards, lf),
        'start': lambda: check_t0t1_start(main_deck, cards, lf),
        'usability': lambda: check_card_usability(main_deck, extra_deck, cards, lf),
        'quality': lambda: check_quality_score(main_deck, extra_deck, cards, lf),
    }

    if section == 'all':
        sections_to_run = list(checks.keys())
    else:
        sections_to_run = [section]

    for name in sections_to_run:
        if name in checks:
            result = checks[name]()
            print(result)
            all_checks.errors.extend(result.errors)
            all_checks.warnings.extend(result.warnings)
            all_checks.infos.extend(result.infos)
            print()

    # 总结
    print("=" * 50)
    if all_checks.errors:
        print(f"结果: 失败 ({len(all_checks.errors)}个错误, {len(all_checks.warnings)}个警告)")
        for e in all_checks.errors:
            print(e)
        return 1
    elif all_checks.warnings:
        print(f"结果: 通过但有警告 ({len(all_checks.warnings)}个)")
        for w in all_checks.warnings:
            print(w)
        return 2
    else:
        print("结果: 全部通过")
        return 0


if __name__ == '__main__':
    args = [a for a in argv[1:] if not a.startswith('--section=')]
    section = 'all'
    for a in argv[1:]:
        if a.startswith('--section='):
            section = a.split('=', 1)[1]

    if not args:
        print("用法: ./ydkcheck.py <deck.ydk> [--section=basic|lflist|extra|start|types|usability|quality|all]")
        print("")
        print("检查项:")
        print("  basic      - 基础计数(40-60 main, 0-15 extra)")
        print("  duplicates - 同名卡≤3检查(含alias)")
        print("  lflist     - 禁限卡表检查")
        print("  types      - 卡片类型比例")
        print("  extra      - 额外可召唤性")
        print("  start      - T0/T1起手率模拟(N_SAMPLES=500)")
        print("  usability  - 卡片可用性粗略检查")
        print("  quality    - 质量评分")
        print("  all        - 全部检查(默认)")
        exit(1)

    exit(run_checks(args[0], section))
