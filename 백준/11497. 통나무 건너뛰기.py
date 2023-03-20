# 11497. 통나무 건너뛰기
# https://www.acmicpc.net/problem/11497

t = int(input())

for _ in range(t):
  k = int(input())
  data = list(map(int, input().split()))
  max = 0
  data.sort()

  for i in range(len(data) - 2):
    tmp = abs(data[i] - data[i + 2])
    if max < tmp:
      max = tmp
  print(max)
