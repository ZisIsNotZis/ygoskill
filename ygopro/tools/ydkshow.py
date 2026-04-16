#!/bin/env python
from sqlite3 import connect
from sys import argv, stdout
from sys import argv
from glob import iglob
from os import getenv, listdir, path
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
        return len(self)>len(_) or(len(self)==len(_)and sum(self)>sum(_))
    def __str__(self):
        return f'{len(self)/self.n*100:.1f}%has({('%.2f'%(sum(self)/len(self))).strip('0').rstrip('.')or'0'}±{('%.2f'%np.std(self)).strip('0').rstrip('.')or'0'} q1-9={','.join('%.0f'%i for i in np.quantile(self,(.1,.3,.5,.7,.9)))})'
TYPE = '怪兽 魔法 陷阱  通常 效果 融合 仪式 陷怪 灵魂 同盟 二重 调整 同调 衍生  速攻 永续 装备 场地 反击 反转 卡通 超量 灵摆 特招 连接'.split(' ')
RACE = '战士 魔法师 天使 恶魔 不死 机械 水 炎 岩石 鸟兽 植物 昆虫 雷 龙 兽 兽战士 恐龙 鱼 海龙 爬虫类 念动力 幻神兽 创造神 幻龙 电子界 幻想魔'.split()
ATT = '地水炎风光暗神'
LINK = '↙↓↘← →↖↑↗'
CAT = '魔陷破坏 怪兽破坏 卡片除外 送去墓地 返回手卡 返回卡组 手卡破坏 卡组破坏 抽卡辅助 卡组检索 卡片回收 表示形式 控制权 攻守变化 穿刺伤害 多次攻击 攻击限制 直接攻击 特殊召唤 衍生物 种族相关 属性相关 LP伤害 LP回复 破坏耐性 效果耐性 指示物 幸运 融合相关 同调相关 超量相关 效果无效'.split()
OT = 'OCG TCG DIY 简中'.split(' ')
YGOROOT = getenv('YGOROOT', '.')
COLOR = int(getenv('COLOR', stdout.isatty()))
CLUSTER = int(getenv('CLUSTER', 0))
N = int(getenv('N', 100))
LF = {}
for diy, i in enumerate((f'{YGOROOT}/lflist.conf', f'{YGOROOT}/expansions/lflist.conf')):
    if path.exists(i):
        for i in open(i).read().split('\n!')[:0:-1]:
            ot, _, i = i.partition('\n')
            t, _, ot = ot.partition(' ')
            ot = 'DIY'if diy else ot or 'OCG'
            lf = {int(i):int(j)for i in i.split('\n')if i[:1]not in '#!'for i,j in[i.split()[:2]]}
            for i, j in lf.items():
                lfs = LF.setdefault(ot, {}).setdefault(i, {})
                if not lfs or list(lfs.values())[-1] != j:
                    lfs[t] = j
            for i, lfs in LF[ot].items():
                if i not in lf and lfs and list(lfs.values())[-1] != 3:
                    LF[ot][i][t] = 3
SET = {int(i, 16): j.split('|')for i in (f'{YGOROOT}/expansions/strings.conf', f'{YGOROOT}/strings.conf')if path.exists(i)for i in open(i).read().split('setname ')[1:]for i, j in [i.split()[:2]]}
SET = {i: '|'.join(set(k for j, k in SET.items()if i & 0xfff == j & 0xfff and i & j == j for k in k))for i in SET}
DATE = {int(j): date.fromisoformat(i.split()[0].replace('misc.ydk', '01-01'))for i in listdir(f'{YGOROOT}/pack')for j in open(f'{YGOROOT}/pack/{i}')if j.strip().isdigit()}
CARD = {i: f'{'\033[31m'if COLOR else''}{name}{'\033[0m'if COLOR else''}{f'({_})'if (_:='|'.join(SET.get(set>>i & 0xffff,hex(set>>i&0xffff))for i in range(0,64,16)if set>>i))else ''} {i}{f'→{alias}'if alias else''} {'|'.join(k+','.join(f'{j}={k}'for j,k in LF.get(k,{}).get(i,{}).items())for j,k in enumerate(OT)if(ot|diy*4)&1<<j)} {f'{_} 'if(_:=DATE.get(i,DATE.get(alias)))else''}{''.join(j for i,j in enumerate(TYPE)if type&1<<i)}{lv >> 24 if type & 0x1000000 else ''}{''.join(LINK[i]for i in range(9)if type & 0x4000000 and Def & 1 << i)}{f'({_})'if(_:='|'.join(j for i,j in enumerate(CAT)if category%0x100000000&1<<i))else''}{f' {f'连接{lv&15}'if type&0x4000000 else f'{lv%15}阶'if type&0x800000 else f'{lv&15}星'}·{ATT[att.bit_length()-1]}属性·{RACE[race.bit_length()-1]}族 {'?'if atk < 0 else atk}/{'?'if Def < 0 else '-'if type & 0x4000000 else Def}'if type & 0x101 else ''}\t{desc.replace('\r', '').replace('\n', '').strip()}'for diy,i in enumerate((f'{YGOROOT}/cards.cdb',f'{YGOROOT}/expansions/cards.cdb'))if path.exists(i)for i, alias, name, ot,type, set, att, race, lv, atk, Def, category, desc in connect(i).execute('select datas.id,alias,name,ot,type,setcode,attribute,race,level,atk,def,category,desc from datas join texts on datas.id=texts.id')}
if len(argv) < 2:
    print('''(YGOROOT=. COLOR=1 CLUSTER=0 N=100) ydkshow.py <file>.ydk|<ydkfolder>/|<cardregex>
    Show cards or top N cards per deck. Group decks into CLUSTER clusters if used''')
decks = [Counter(int(i)for i in open(i).read().split()if i.isdigit())for i in argv[1:]for i in((i,)if i.endswith('.ydk')else iglob(f'{i}**/*.ydk',recursive=True)if i.endswith('/')else())]
if CLUSTER:
    cards = {j:i for i,j in enumerate({i for i in decks for i in i})}
    deckmat = np.zeros((len(decks),len(cards)),'f')
    for i,j in zip(deckmat,decks):
        i[list(map(cards.__getitem__,j))] = list(j.values())
    deckmat /= deckmat.sum(1,keepdims=True)
    decks = [reduce(lambda a,i:([a.setdefault(i,stat(len(decks))).append(j)for i,j in decks[i].items()],a)[1],i.nonzero()[0],{})for i in KMeans(CLUSTER).fit(deckmat).labels_==np.arange(CLUSTER)[:,None]]
for i in decks:
    print(*(f'{j} {CARD.get(i,i)}'for i,j in sorted(i.items(),key=lambda i:i[1])[:N]),sep='\n',end='\n\n\n')
for i in argv[1:]:
    if not(i.endswith('.ydk')or i.endswith('/')):
        i = compile(i)
        print(*(j for j in CARD.values()if i.match(j)), sep='\n', end='\n\n\n')