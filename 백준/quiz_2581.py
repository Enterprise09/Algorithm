# https://www.acmicpc.net/problem/2581

m = int(input())
n = int(input())
result = list()
for i in range(m, n + 1):
    check = 0
    if(i > 1):  # 1은 소수가 아니기 때문에 제외
        for num in range(2, i):
            if(i % num == 0):
                check += 1
                break
        if(check == 0):     # 소수이다.
            result.append(i)
if(len(result) > 0):
    print(sum(result))
    print(min(result))
else:
    print(-1)