# 13 - Star Triangle
n = int(input())
for line in range(1, n + 1):
    print(" " * (n - line) + "*" * (line * 2 - 1))
