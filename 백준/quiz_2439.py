# https://www.acmicpc.net/problem/2439

c = int(input())
for i in range(1, c + 1):
    print(' ' * (c - i) + '*' * i)