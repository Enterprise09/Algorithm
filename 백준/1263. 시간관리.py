# 1263. 시간 관리
# https://www.acmicpc.net/problem/1263

n = int(input())
data = list()
ans = 1000000

for _ in range(n):
  data.append(list(map(int, input().split())))
data.sort(key=lambda x: -x[1])
for i in range(n):
  temp = data[i][1]
  if ans <= temp:
    ans = ans - data[i][0]
  else:
    ans = temp - data[i][0]
if ans < 0:
  ans = -1

print(ans)
