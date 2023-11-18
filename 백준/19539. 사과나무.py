# 19539. 사과나무
# https://www.acmicpc.net/problem/19539

import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

sum = sum(arr)

if sum % 3 == 0:
    ctr = 0
    for i in range(len(arr)):
        ctr += arr[i] // 2
    if ctr >= sum / 3:
        print("YES")
    else:
        print("NO")
else:
    print("NO")