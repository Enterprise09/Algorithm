n = int(input())
data = list(map(int, input().split()))
data.sort()  # 오름차순 정렬

#  1 2 2 2 4

result = 0
ctr = 0

for i in data:
  ctr += 1
  if ctr >= i:
    result += 1
    ctr = 0

print(result)