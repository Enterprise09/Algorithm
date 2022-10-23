# https://www.acmicpc.net/problem/1929

def Prime(n):
    if(n == 1):
        return False
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if(n % i == 0):
                return False
        return True

m, n = map(int, input().split())
# 1 <= m <= 1000000

for i in range(m, n + 1):
    if(Prime(i)):
        print(i)