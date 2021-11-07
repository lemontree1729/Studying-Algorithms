"""Dijkstra algorithm"""
import sys
import heapq


input = sys.stdin.readline
n, m = map(int, input().split())
k = int(input())
a = {i: dict() for i in range(1, n + 1)}
for _ in range(m):
    u, v, w = map(int, input().split())
    if w < a[u].get(v, 11):
        a[u][v] = w
result = [2 * 10 ** 6] * (n + 1)
result[k] = 0
weight = [(0, k)]
check = []
while weight:
    while check and weight[0] == check[0]:
        for things in (check, weight):
            heapq.heappop(things)
    if not weight:
        break
    x, y = heapq.heappop(weight)
    for i in a[y]:
        if result[i] > x + a[y][i]:
            if result[i] != 2 * 10 ** 6:
                heapq.heappush(check, (result[i], i))
            result[i] = x + a[y][i]
            heapq.heappush(weight, (result[i], i))
for num in range(1, n + 1):
    if result[num] == 2 * 10 ** 6:
        print("INF")
    else:
        print(result[num])
