from sqlite3 import connect
from itertools import groupby
from yaml import dump_all
from collections import Counter
R = '战魔天恶死机水炎岩鸟植昆雷龙兽士恐鱼海爬念神创幻电想'
A = '地水炎风光暗神'
ra = [(R[r.bit_length()-1], A[a.bit_length()-1])for r, a in connect('cards.cdb').execute('select race,attribute from datas where race and attribute')]
rn = dict(Counter(r for r, a in ra).most_common())
an = dict(Counter(a for r, a in ra).most_common())
print(dump_all((
    rn,
    an,
    {r: {a: -n for n, a in sorted((-n/an[a], a)for a, n in (dict.fromkeys(A, 0) | Counter(a for r, a in ra)).items())}for r, ra in groupby(sorted(ra), lambda ra: ra[0])},
    {a: {r: -n for n, r in sorted((-n/rn[r], r)for r, n in (dict.fromkeys(R, 0) | Counter(r for r, a in ra)).items())}for a, ra in groupby(sorted(ra, key=lambda ra: ra[1]), lambda ra: ra[1])},
), allow_unicode=True, sort_keys=False))
