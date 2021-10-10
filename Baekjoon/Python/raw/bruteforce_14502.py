from itertools import combinations as comb
import copy
from collections import deque


def bfs(data):
    global n, m, vircrd, blknum
    cnt = 0
    deq = deque(vircrd)
    while deq:
        x, y = deq.popleft()
        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            nx, ny = x+dx, y+dy
            if 0 <= nx < m and 0 <= ny < n and data[ny][nx] == 0:
                deq.append((nx, ny))
                data[ny][nx] = 2
                cnt += 1
    return blknum - 3 - cnt
            
        
n, m = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))
blkcrd = []
vircrd = []
for j in range(n):
    for i in range(m):
        if data[j][i] == 0:
            blkcrd.append((i, j))
        elif data[j][i] == 2:
            vircrd.append((i, j))
blknum = len(blkcrd)
blkcho = list(comb(blkcrd, 3))
maxblk = 0
for i in blkcho:
    newdata = copy.deepcopy(data)
    for j in range(3):
        newdata[i[j][1]][i[j][0]] = 1
    maxblk = max(maxblk, bfs(newdata))
print(maxblk)
