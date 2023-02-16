n, l = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

start = data[0]
ctr = 1
for i in data[1:]:
  if i in range(start, start + l):
    continue
  start = i
  ctr += 1

print(ctr)
