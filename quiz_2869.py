# https://www.acmicpc.net/problem/2869

from math import ceil

a, b, v = map(int, input().split())
# a만큼 올라가고 b만큼 떨어지는 것을 n일 만큼 반복하고 
# 마지막 날에는 a만큼 올라가고 내려오지 않음
# (a - b) * n + a = v

result = ceil((v - a) / (a - b)) + 1
print(result)