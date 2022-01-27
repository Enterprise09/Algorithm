# https://www.acmicpc.net/problem/2588

a = int(input())
b = int(input())

# 각 자리의 수를 구함
s = int(b % 10)
m = int((b % 100) / 10)
l = int(b / 100)

n3 = a * s
n4 = a * m
n5 = a * l
total = n3 + n4 * 10 + n5 * 100  # 총합 계산

print(n3)
print(n4)
print(n5)
print(total)