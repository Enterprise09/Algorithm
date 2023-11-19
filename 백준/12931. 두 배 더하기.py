# 12931. 두 배 더하기
# https://www.acmicpc.net/problem/12931

import sys

n = int(sys.stdin.readline())
arr_B = list(map(int, sys.stdin.readline().split()))

tmp = []
res = 0

while sum(arr_B) != 0:
    for i in range(n):
        if arr_B[i] % 2 != 0:
            res += 1
            arr_B[i] -= 1
    if sum(arr_B) == 0:
        break
    for i in range(n):
        arr_B[i] = arr_B[i] // 2
    res += 1
print(res)