# https://www.acmicpc.net/problem/1292

a, b = map(int, input().split())
numbers = list()
for i in range(1001):
    ctr = 1
    while True:
        numbers.append(i)
        ctr += 1
        if(ctr > i):
            break

print(sum(numbers[a:b+1]))