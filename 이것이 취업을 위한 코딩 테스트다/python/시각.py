#  완전 탐색 - 경우의 수가 매우 많아짐

n = int(input())
ctr = 0

for h in range(n + 1):
  for m in range(60):
    for sec in range(60):
      if '3' in str(h) + str(m) + str(sec):
        ctr += 1

print(ctr)