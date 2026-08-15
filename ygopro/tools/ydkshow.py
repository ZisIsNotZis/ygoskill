#!/bin/env python
from sqlite3 import connect
from sys import argv, stdout
from os import getenv, listdir
from datetime import date


TYPE = '怪兽 魔法 陷阱  通常 效果 融合 仪式  灵魂 同盟 二重 调整 同调   速攻 永续 装备 场地 反击 反转 卡通 超量 灵摆 特招 连接'.split(' ')
RACE = '战士 魔法师 天使 恶魔 不死 机械 水 炎 岩石 鸟兽 植物 昆虫 雷 龙 兽 兽战士 恐龙 鱼 海龙 爬虫类 念动力 幻神兽 创造神 幻龙 电子界 幻想魔'.split()
ATT = '地水炎风光暗神'
LINK = '↙↓↘← →↖↑↗'
CAT = '魔陷破坏 怪兽破坏 卡片除外 送去墓地 返回手卡 返回卡组 手卡破坏 卡组破坏 抽卡辅助 卡组检索 卡片回收 表示形式 控制权 攻守变化 穿刺伤害 多次攻击 攻击限制 直接攻击 特殊召唤 衍生物 种族相关 属性相关 LP伤害 LP回复 破坏耐性 效果耐性 指示物 幸运 融合相关 同调相关 超量相关 效果无效'.split()
OT = 'OCG TCG DIY CN'.split(' ')
YGOROOT = getenv('YGOROOT', '.')
YGOROOTDIY = getenv('YGOROOTDIY', '')
COLOR = int(getenv('COLOR', stdout.isatty()))
CLUSTER = int(getenv('CLUSTER', 0))
N = int(getenv('N', 100))
LF = {}
for i in open(f'{YGOROOT}/lflist.conf').read().split('\n!')[:0:-1]:
    ot, _, i = i.partition('\n')
    t, _, ot = ot.partition(' ')
    ot = ot or 'OCG'
    lf = {int(i): int(j)for i in i.split('\n')if i[:1]not in '#!'for i, j in [i.split()[:2]]}
    for i, j in lf.items():
        lfs = LF.setdefault(ot, {}).setdefault(i, {})
        if not lfs or list(lfs.values())[-1] != j:
            lfs[t] = j
    for i, lfs in LF[ot].items():
        if i not in lf and lfs and list(lfs.values())[-1] != 3:
            LF[ot][i][t] = 3
SET = {int(i, 16): j for i in open(f'{YGOROOT}/strings.conf').read().split('setname ')[1:]for i, j in [i.split()[:2]]}
DATE = {int(j): date.fromisoformat(i.split()[0].replace('misc.ydk', '01-01'))for i in listdir(f'{YGOROOT}/pack')for j in open(f'{YGOROOT}/pack/{i}')if j.strip().isdigit()}
CARD = {
    i: f'{name} {type}\t{desc}'
    for diy, i in enumerate([f'{YGOROOT}/cards.cdb',*([f'{YGOROOTDIY}/cards.cdb']if YGOROOTDIY else'')])
    for i, alias, name, ot, type, set, att, race, lv, atk, Def, category, desc in connect(i).execute('select datas.id,alias,name,ot,type,setcode,attribute,race,level,atk,def,category,desc from datas join texts on datas.id=texts.id where not type&0x4000')
    for name in [f'{name}{'('if set else''}{'|'.join(SET.get(set >> i & 0xffff, hex(set >> i & 0xffff))for i in range(0, 64, 16)if set >> i)}{')'if set else''} {alias or i}{f'←{i}'if alias else ''},{DATE.get(i,DATE.get(alias,'-'))},{','.join(k+'·'.join(f'{j}={k}'for j, k in LF.get(k, {}).get(i, {}).items())for j, k in enumerate(OT)if (ot | diy*4) & 1 << j)}']
    for type in [f'{''.join(j for i, j in enumerate(TYPE)if type & 1 << i)}{f'{lv >> 24 if type & 0x1000000 else ''}{''.join(j for i,j in enumerate(LINK)if Def & 1 << i)if type & 0x4000000 else''}·{RACE[race.bit_length()-1]}族·{ATT[att.bit_length()-1]}属性·{'连接'if type & 0x4000000 else ''}{lv & 15}{'阶'if type & 0x800000 else ''if type & 0x4000000 else '星'}·攻击力{'?'if atk < 0 else atk}·守备力{'?'if Def < 0 else '-'if type & 0x4000000 else Def}'if type & 1 else ''}']
    for desc in [f'{'。'.join(i for i in desc.replace('\r', '').split('\n')if i for i in[i.strip('。：')])}。{'('if category else''}{'·'.join(j for i, j in enumerate(CAT)if category & 1 << i)}{')'if category else''}']
}
if len(argv) <= 1:
    print('''(YGOROOT=. YGOROOTDIY=expansions COLOR=1(isatty) CLUSTER=0 N=100) ydkshow.py <file>.ydk|<ydkfolder>/|<cardregex>
    Show cards or top N cards per deck. Group decks into CLUSTER clusters if used''')
elif argv[1].endswith('ydk')or argv[1].endswith('/'):
    from glob import iglob
    from collections import Counter
    from functools import reduce
    deck = [Counter(int(i)for i in open(i).read().split()if i.isdigit())for i in argv[1:]for i in (iglob(f'{i}**/*.ydk', recursive=True)if i.endswith('/')else(i,))]
    if CLUSTER:
        from sklearn.cluster import KMeans
        from glob import iglob
        import numpy as np
        class stat(list):
            def __init__(self, n):
                self.n = n
            def __lt__(self, _):
                return len(self) > len(_) or (len(self) == len(_) and sum(self) > sum(_))
            def __str__(self):
                return f'{len(self)/self.n*100:.1f}%has({('%.2f' % (sum(self)/len(self))).strip('0').rstrip('.') or '0'}±{('%.2f' % np.std(self)).strip('0').rstrip('.') or '0'} q1-9={','.join('%.0f' % i for i in np.quantile(self, (.1, .3, .5, .7, .9)))})'
        card = {j: i for i, j in enumerate({i for i in deck for i in i})}
        deckmat = np.zeros((len(deck), len(card)), 'f')
        for i, j in zip(deckmat, deck):
            i[list(map(card.__getitem__, j))] = list(j.values())
        deckmat /= deckmat.sum(1, keepdims=True)
        deck = [reduce(lambda a, i: ([a.setdefault(i, stat(len(deck))).append(j)for i, j in deck[i].items()], a)[1], i.nonzero()[0], {})for j,i in enumerate(KMeans(CLUSTER).fit(deckmat).labels_ == np.arange(CLUSTER)[:, None])]
    for i in deck:
        print(*(f'{j} {CARD.get(i, i)}'for i, j in sorted(i.items(), key=lambda i: i[1])[:N]), sep='\n', end='\n\n')
else:
    from re import compile
    card = CARD.values()
    for i in argv[1:]:
        i = compile(i)
        card = [J for j in card for J in [i.sub(f'{'\033[31m'if COLOR else '**'}\\g<0>{'\033[0m'if COLOR else '**'}', j)]if J!=j]
    print(*card, sep='\n', end='\n\n')
