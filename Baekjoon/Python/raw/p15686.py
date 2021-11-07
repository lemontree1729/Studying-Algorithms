"""
bruteforce
"""


import sys
from itertools import combinations as cb


input = sys.stdin.readline
n, m = map(int, input().split())
data = []
hscrd = []
chicrd = []
for y in range(n):
    sect = list(map(int, input().split()))
    for x, inf in enumerate(sect):
        if inf == 1:
            hscrd.append((x, y))
        elif inf == 2:
            chicrd.append((x, y))
    data.append(sect)
chislct = cb(chicrd, m)
result = 10000
for chiset in chislct:
    dissum = 0
    for hx, hy in hscrd:
        dis = 100
        for cx, cy in chiset:
            dis = min(dis, abs(hx - cx) + abs(hy - cy))
        dissum += dis
    result = min(result, dissum)
print(result)
