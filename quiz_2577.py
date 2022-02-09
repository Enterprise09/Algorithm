# https://www.acmicpc.net/problem/2577

a = int(input())
b = int(input())
c = int(input())

result = list(str(a * b * c))   # int형을 str로 변환 -> list형태로 변환
for i in range(10):
    print(result.count(str(i)))