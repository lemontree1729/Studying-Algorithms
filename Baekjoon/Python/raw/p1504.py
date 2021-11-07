"""Using dijkstra algorithm """
import sys
from heapq import heapify as hp, heappush as hppush, heappop as hppop


input = sys.stdin.readline
n, e = map(int, input().split())
INF = sys.maxsize
data = [[INF]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    data[i][i] = 0
for _ in range(e):
    v1, v2, w = map(int, input().split())
    data[v1][v2] = min(data[v1][v2], w)
    data[v2][v1] = min(data[v2][v1], w)
t1, t2 = map(int, input().split())
for start in 1, t1, t2:
    heap = []
    for i in range(1, n+1):
        if data[start][i] != INF:
            hppush(heap, (data[start][i], i))
    while heap:
        _, trans = hppop(heap)
        for end in range(1, n+1):
            if data[start][end] > data[start][trans] + data[trans][end]:
                data[start][end] = data[start][trans] + data[trans][end]
                hppush(heap, (data[start][end], end))
result = min(data[1][t1] + data[t1][t2] + data[t2][n], data[1][t2] + data[t2][t1] + data[t1][n])
if result >= INF:
    print(-1)
else:
    print(result)
