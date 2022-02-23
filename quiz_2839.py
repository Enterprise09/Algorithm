# https://www.acmicpc.net/problem/2839

n = int(input())
ctr = 0
while n >= 0:
    if(n % 5) == 0:
        ctr += n // 5
        print(ctr)
        break
    n -= 3
    ctr += 1
else:
    print(-1)