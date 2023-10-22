# 3003. 킹, 퀸, 룩, 비숍, 나이트, 폰
# https://www.acmicpc.net/problem/3303

arr = list(map(int, input().split()))
fm = [1, 1, 2, 2, 2, 8]
res = []

for i in range(len(fm)):
  r = fm[i] - arr[i]
  res.append(r)

for i in range(len(res)):
  print(res[i], end=' ')
