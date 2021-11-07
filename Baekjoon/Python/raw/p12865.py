""" solving problem 12865 with dynamic programming"""
from random import randint


def test(num: int, maxw: int):
    sample = []
    while len(sample) < num:
        sample.append((randint(0, 1000), randint(1, maxw)))
    return sample


def knapsack(data):
    global dp, k
    for num, (w, v) in enumerate(data):
        for maxw in range(k + 1):
            if w > k or w > maxw:
                dp[num + 1][maxw] = dp[num][maxw]
            else:
                dp[num + 1][maxw] = max(dp[num][maxw], dp[num][maxw - w] + v)


""" test code
n = 10
m = 10
k = 10
data = test(n, m)
"""


n, k = map(int, input().split())  # Given input variables
data = []
for _ in range(n):
    data.append(tuple(map(int, input().split())))
dp = [[0] * (k + 1) for _ in range(n + 1)]
knapsack(data)
print(dp[n][k])
