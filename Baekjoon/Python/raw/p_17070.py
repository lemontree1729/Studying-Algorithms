"""Dynamic programming"""
import sys


input = sys.stdin.readline
n = int(input())
dp = [
    [[0, 0, 0] for _ in range(n + 1)] for _ in range(n + 1)
]  # 0, 45, 90 degree pipe each
data = [[0] * (n + 1)]
for _ in range(n):
    data.append([0] + list(map(int, input().split())))
for y in range(1, n + 1):
    for x in range(1, n + 1):
        if x == 2 and y == 1:
            dp[y][x][0] = 1
        elif data[y][x] == 0:
            dp[y][x][0] = dp[y][x - 1][0] + dp[y][x - 1][1]
            dp[y][x][2] = dp[y - 1][x][1] + dp[y - 1][x][2]
            if data[y - 1][x] == 0 and data[y][x - 1] == 0:
                dp[y][x][1] = sum(dp[y - 1][x - 1])
print(sum(dp[n][n]))
