#!/bin/env python
from sqlite3 import connect
from sys import argv, stdout
from sys import argv
from glob import iglob
from os import getenv, listdir
from functools import reduce
from collections import Counter
from datetime import date
from re import compile
import numpy as np
from sklearn.cluster import KMeans


class stat(list):
    def __init__(self, n):
        self.n = n

    def __lt__(self, _):
        return len(self) > len(_) or (len(self) == len(_) and sum(self) > sum(_))

    def __str__(self):
        return f'{len(self)/self.n*100:.1f}%has({('%.2f' % (sum(self)/len(self))).strip('0').rstrip('.') or '0'}±{('%.2f' % np.std(self)).strip('0').rstrip('.') or '0'} q1-9={','.join('%.0f' % i for i in np.quantile(self, (.1, .3, .5, .7, .9)))})'


def highlight(x, i, pre=False):
    return x if not (i := '·'.join(i for i in i if not (i in x and (x := x.replace(i, f'\033[31m{i}\033[0m'if COLOR else f'*{i}*')))))else f'({i}){x}'if pre else f'{x}({i})'


TYPE = '怪兽 魔法 陷阱  通常 效果 融合 仪式  灵魂 同盟 二重 调整 同调   速攻 永续 装备 场地 反击 反转 卡通 超量 灵摆  '.split(' ')
RACE = '战士 魔法师 天使 恶魔 不死 机械 水 炎 岩石 鸟兽 植物 昆虫 雷 龙 兽 兽战士 恐龙 鱼 海龙 爬虫类 念动力 幻神兽 创造神 幻龙 电子界 幻想魔'.split()
ATT = '地水炎风光暗神'
LINK = '↙↓↘← →↖↑↗'
CAT = '卡破坏 怪兽破坏 除外 送去墓地 回到手卡 回到卡组 手卡破坏 卡组破坏 抽 加入 加入 表示 控制权 攻击力 超过 次攻击 不能攻击 直接攻击 特殊召唤 衍生物 种族 属性 伤害 回复 不会 不受 指示物 幸运 融合 同调 超量 无效'.split()
OT = 'OCG TCG DIY CN'.split(' ')
YGOROOT = getenv('YGOROOT', './')
YGOROOTDIY = getenv('YGOROOTDIY', 'expansions/')
COLOR = int(getenv('COLOR', stdout.isatty()))
CLUSTER = int(getenv('CLUSTER', 0))
N = int(getenv('N', 100))
LF = {}
for i in open(f'{YGOROOT}lflist.conf').read().split('\n!')[:0:-1]:
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
SET = {int(i, 16): j for i in open(f'{YGOROOT}strings.conf').read().split('setname ')[1:]for i, j in [i.split()[:2]]}
DATE = {int(j): date.fromisoformat(i.split()[0].replace('misc.ydk', '01-01'))for i in listdir(f'{YGOROOT}pack')for j in open(f'{YGOROOT}pack/{i}')if j.strip().isdigit()}
CARD = {
    i: f'{name} {type}\t{desc}'
    for diy, i in enumerate([f'{YGOROOT}cards.cdb', f'{YGOROOTDIY}cards.cdb'])
    for i, alias, name, ot, type, set, att, race, lv, atk, Def, category, desc in connect(i).execute('select datas.id,alias,name,ot,type,setcode,attribute,race,level,atk,def,category,desc from datas join texts on datas.id=texts.id where not type&0x4000')
    for name in [f'{highlight(name, [SET.get(set >> i & 0xffff, hex(set >> i & 0xffff))for i in range(0, 64, 16)if set >> i])}({alias or i}{f'←{i}'if alias else ''},{','.join(k+'·'.join(f'{j}={k}'for j, k in LF.get(k, {}).get(i, {}).items())for j, k in enumerate(OT)if (ot | diy*4) & 1 << j)})']
    for type in [f'{''.join(j for i, j in enumerate(TYPE)if type & 1 << i and j)}{f'{lv >> 24 if type & 0x1000000 else ''}{''.join(LINK[i]for i in range(9)if type & 0x4000000 and Def & 1 << i)}·{RACE[race.bit_length()-1]}族·{ATT[att.bit_length()-1]}属性·{'连接'if type & 0x4000000 else ''}{lv & 15}{'阶'if type & 0x800000 else '·'if type & 0x4000000 else '星'}·攻击力{'?'if atk < 0 else atk}·守备力{'?'if Def < 0 else '-'if type & 0x4000000 else Def}'if type & 1 else ''}']
    for desc in [highlight('。'.join(i.strip('，。：')for i in desc.replace(' ', '').replace('\t', '').replace('\r', '').split('\n')), [j for i, j in enumerate(CAT)if category % 0x100000000 & 1 << i], True)]
}
if len(argv) < 2:
    print('''(YGOROOT=./ YGOROOTDIY=expansions/ COLOR=1(isatty) CLUSTER=0 N=100) ydkshow.py <file>.ydk|<ydkfolder>/|<cardregex>
    Show cards or top N cards per deck. Group decks into CLUSTER clusters if used''')
decks = [Counter(int(i)for i in open(i).read().split()if i.isdigit())for i in argv[1:]for i in ((i,)if i.endswith('.ydk')else iglob(f'{i}**/*.ydk', recursive=True)if i.endswith('/')else ())]
if CLUSTER:
    cards = {j: i for i, j in enumerate({i for i in decks for i in i})}
    deckmat = np.zeros((len(decks), len(cards)), 'f')
    for i, j in zip(deckmat, decks):
        i[list(map(cards.__getitem__, j))] = list(j.values())
    deckmat /= deckmat.sum(1, keepdims=True)
    decks = [reduce(lambda a, i: ([a.setdefault(i, stat(len(decks))).append(j)for i, j in decks[i].items()], a)[1], i.nonzero()[0], {})for i in KMeans(CLUSTER).fit(deckmat).labels_ == np.arange(CLUSTER)[:, None]]
for i in decks:
    print(*(f'{j} {CARD.get(i, i)}'for i, j in sorted(i.items(), key=lambda i: i[1])[:N]), sep='\n', end='\n\n')
for i in argv[1:]:
    if not (i.endswith('.ydk') or i.endswith('/')):
        i = compile(i)
        print(*(k for j in CARD.values()if (k := i.sub(f'{'\033[31m'if COLOR else '**'}\\g<0>{'\033[0m'if COLOR else '**'}', j)) != j), sep='\n', end='\n\n')
