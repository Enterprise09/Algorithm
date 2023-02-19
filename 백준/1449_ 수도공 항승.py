# 1449. 수도공 항승
# https://www.acmicpc.net/problem/1449

n, l = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

start = data[0]
ctr = 1
for i in data[1:]:
  if i in range(start, start + l):
    continue
  else:  # else문을 사용하지 않으면 error가 나와버린다.
    start = i
    ctr += 1

print(ctr)
