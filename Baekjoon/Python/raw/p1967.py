import sys
from copy import deepcopy


def dfs(info, a):
    newinfo = deepcopy(info)
    stack = [a]
    end = a
    temp = 0
    radius = 0
    checked = [False] * n
    checked[stack[-1]] = True
    while stack:
        if newinfo[stack[-1]]:
            c, w = newinfo[stack[-1]].popitem()
            if not checked[c]:
                checked[c] = True
                stack.append(c)
                temp += w
        else:
            if temp > radius:
                radius = temp
                end = stack[-1]
            last = stack.pop()
            if stack:
                temp -= info[stack[-1]][last]
    return (end, radius)


input = sys.stdin.readline
n = int(input())
info = [{} for _ in range(n)]
for _ in range(n - 1):
    p, c, w = map(int, input().split())
    info[p - 1][c - 1] = w
    info[c - 1][p - 1] = w
end, _ = dfs(info, 0)
_, radius = dfs(info, end)
print(radius)
