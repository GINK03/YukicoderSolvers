from collections import Counter
n=int(input())

ps = []
for _ in range(n):
    a,b=map(int,input().split())
    ps.append((a,b))

from itertools import combinations

pset = set()

special_x = set()
special_y = set()
for p1, p2 in combinations(ps,2):
    if p2[0] != p1[0]:
        katamuki = (p2[1] - p1[1])/(p2[0] - p1[0])
        takasa = p1[1] - katamuki*p1[0]
        pset.add((katamuki, takasa))
    if p2[0] == p1[0]:
        special_x.add(p1[0])
    if p2[1] == p1[1]:
        special_y.add(p1[0])
        
cs = []
for katamuki, takasa in pset:
    c = 0
    for p in ps:
        if abs(p[1] - (p[0]*katamuki + takasa)) < 0.0001:
            c += 1
    cs.append(c)
for special in special_x:
    c = 0
    for p in ps:
        if p[0] == special:
            c += 1
    cs.append(c)
for special in special_y:
    c = 0
    for p in ps:
        if p[1] == special:
            c += 1
    cs.append(c)
print(max(cs))


