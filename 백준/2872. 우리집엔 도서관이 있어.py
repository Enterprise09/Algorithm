# 2872. 우리집엔 도서관이 있어
# https://www.acmicpc.net/problem/2872

import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
data = []
target = N
ans = 0

# Get data
for i in range(N):
  data.append(int(input()))

# Reversed quest
for i in range(N - 1, -1, -1):
  if data[i] != target:
    ans += 1
  else:
    target -= 1
print(ans)