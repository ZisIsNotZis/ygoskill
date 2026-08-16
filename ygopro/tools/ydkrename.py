#!/bin/env python
from sqlite3 import connect
from re import compile
from collections import Counter
from typing import cast, Iterable
from os import getenv, mkdir, listdir, remove, rename
from sys import argv
from xxhash import xxh64_hexdigest


def gram(a: str) -> Iterable[str]:
    for i in range(len(a)):
        for j in range(i+1+(len(a) > 1), len(a)+1):
            yield a[i:j]


def mkdir_(a: str, cache: set[str] = set()):
    if a not in cache:
        cache.add(a)
        try:
            mkdir(a)
        except FileExistsError:
            pass


DATE = {int(j): (max(int(_)if (_ := i[:4]).isdigit()else 0, 2000) % 100)*10000+(int(_)if (_ := i[5:7]).isdigit()else 0)*100+(int(_)if (_ := i[8:10]).isdigit()else 0)for i in listdir('../pack')for j in open(f'../pack/{i}')if j.strip().isdigit()}
SET = {int(i, 16): j.split('|')[0]for i in open('../strings.conf').read().split('setname ')[1:]for i, j in [i.split()[:2]]}
SEP = compile(getenv('SEP', '[- ·/]'))
CNT = int(getenv('CNT', 4))
TXT = {i: tuple({i for i in {name, *(i.split('」')[0]for i in dsc.split('「')[1:]), *(SET[i]for i in (0, 16, 32, 48)for i in [set >> i & 65535]if i in SET)}for i in SEP.split(i)for i in gram(i)})for i, name, dsc, set in cast(Iterable[tuple[int, str, str, int]], connect('../cards.cdb').execute('select texts.id,name,desc,setcode from texts join datas on texts.id=datas.id'))}

for file in argv[1:]:
    deck = [i for i, j in sorted(Counter(int(i)for i in open(file, errors='ignore').read().split('!')[0].split()if i.isdigit()).items())for _ in range(min(j, 3))][:75]
    if not deck:
        continue
    txts = [i for i in deck for i in [TXT.get(i)]if i]
    name = '%06d' % max(DATE.get(i, 0)for i in deck)
    while txts:
        txt, cnt = max(Counter(sum(txts, ())).items(), key=lambda i: (i[1], len(i[0]), i[0]))
        if cnt < CNT:
            break
        name += txt
        txts = [i for i in txts if txt not in i]
    mkdir_(name)
    name += f'/{xxh64_hexdigest('\n'.join(map(str, deck)).encode())}.ydk'
    if file != name:
        print(name)
        try:
            rename(file, name)
        except FileExistsError:
            pass