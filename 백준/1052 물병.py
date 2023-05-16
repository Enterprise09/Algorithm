# 1052. 물병
# https://www.acmicpc.net/problem/1052

n, k = map(int, input().split())
ctr = 0

while bin(n).count('1') > k:
  n += 1
  ctr += 1

print(ctr)