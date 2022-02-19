# https://www.acmicpc.net/problem/2869

a, b, v = map(int, input().split())
sum = 0
ctr = 0
while sum < v:
    sum += a - b
    if(sum == v):
        break
    ctr += 1
print(ctr)