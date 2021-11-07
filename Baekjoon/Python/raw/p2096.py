import sys


input = sys.stdin.readline
x0, x1, y0, y1, z0, z1 = [0] * 6
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    x0, y0, z0 = min(x0, y0) + a, min(x0, y0, z0) + b, min(y0, z0) + c
    x1, y1, z1 = max(x1, y1) + a, max(x1, y1, z1) + b, max(y1, z1) + c
print(max(x1, y1, z1), min(x0, y0, z0))
