# 12904. A와 B
# https://www.acmicpc.net/problem/3303

s = list(input())
t = list(input())

if len(s) != len(t):
  while True:
    tmp = t.pop()
    if tmp == "B":
      t.reverse()
    if len(s) == len(t):
      break

if s == t:
  print(1)
else:
  print(0)