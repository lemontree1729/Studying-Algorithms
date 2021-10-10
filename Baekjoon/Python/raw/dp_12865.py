
""" test code
from random import *


def test(n, m):
    a = []
    while len(a) < n:
        a.append((randint(0, 1000), randint(1, m)))
    return a
"""


def knapsack(a):
    global dp, k
    for i, (w, v) in enumerate(a):
        for j in range(k+1):
            if w > k or w > j:
                dp[i+1][j] = dp[i][j]
            else:
                dp[i+1][j] = max(dp[i][j], dp[i][j-w]+v)


""" test code
n = 10
m = 10
k = 10
a = test(n, m)
print(a)
print(n, m, k)
"""

n, k = map(int, input().split())
a = []
for _ in range(n):
    a.append(tuple(map(int, input().split())))
dp = [[0]*(k+1) for _ in range(n+1)]
knapsack(a)
print(dp[n][k])
