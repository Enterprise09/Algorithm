# 2212. 센서
# https://www.acmicpc.net/problem/2212

n = int(input())
k = int(input())
sum = 0

arr = list(map(int, input().split()))
arr.sort(reverse=True)

diff = []

for i in range(len(arr) - 1):
  diff.append(arr[i] - arr[i + 1])

diff.sort(reverse=True)
for i in range(k - 1, len(diff)):
  sum += diff[i]

print(sum)
