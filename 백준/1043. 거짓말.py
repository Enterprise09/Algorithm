# 1043. 거짓말
# https://www.acmicpc.net/problem/1043

n, m = map(int, input().split())
true_grp = set(input().split()[1:])
part_grp = list()
ctr = 0

# get part_grp data
for _ in range(m):
  part_grp.append(set(input().split()[1:]))

# make true_grp
for _ in range(m):
  for part in part_grp:
    if true_grp & part:
      true_grp = true_grp.union(part)

# Scanning result
for part in part_grp:
  if true_grp & part:
    continue
  ctr += 1

print(ctr)