# convert char to position number
def setX(pos_x):
  arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
  return int(arr.index(pos_x)) + 1


pos_list = list(input())
pos_x = setX(pos_list[0])
pos_y = int(pos_list[1])
max_x, max_y = 8, 8
move_type = ['LU', 'LD', 'RU', 'RD']
ctr = 0

# Ways => 8
#       LU  LD  UL UR RU RD DL DR
# dx = [-2, -2, -1, 1, 2, 2, -1, 1]
# dy = [-1, 1, -2, -2, -1, 1, 2, 2]

# go fast(?)
#     U, D
dx = [-2, 2, -1, 1]

#     L, R
dy = [-1, 1, -2, 2]

for i in range(2):
  nx = pos_x
  nx += dx[i]
  if nx < 1:
    continue
  for j in range(2):
    ny = pos_y
    ny += dy[j]
    if ny < 1:
      continue
    ctr += 1

for i in range(2, 4):
  ny = pos_y
  ny += dy[i]
  if ny < 1:
    continue
  for j in range(2, 4):
    nx = pos_x
    nx += dx[j]
    if nx < 1:
      continue
    ctr += 1

# for i in range(4):
#   nx = pos_x
#   ny = pos_y
#   nx += dx[i]
#   ny += dy[i]
#   if nx < 1 or ny < 1:
#     continue
#   ctr += 1
#   print(nx, ":", ny)
print(ctr)
