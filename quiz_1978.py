# https://www.acmicpc.net/problem/1978

n = int(input())
nums = list(map(int, input().split()))
result = 0
for num in nums:
    checkSum = 0
    if(num > 1):
        for i in range(2, num):
            if(num % i == 0):   # 소수가 아님
                checkSum += 1
        if(checkSum == 0):
            result += 1
print(result)
