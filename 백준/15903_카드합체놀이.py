# 15903. 카드 합체 놀이
# https://www.acmicpc.net/problem/15903

n, m = map(int, input().split())
arr = list(map(int, input().split()))
res = 0

for i in range(m):
  arr.sort()
  s = arr[0] + arr[1]
  arr[0] = s
  arr[1] = s

for i in range(len(arr)):
  res += arr[i]

print(res)