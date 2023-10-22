# 15903. 행복 유치원
# https://www.acmicpc.net/problem/13164

n, k = map(int, input().split())
arr = list(map(int, input().split()))
res = 0
diff = []

for i in range(len(arr) - 1):
  d = arr[i + 1] - arr[i]
  diff.append(d)

diff.sort()
for i in range(n - k):
  res += diff[i]

print(res)
