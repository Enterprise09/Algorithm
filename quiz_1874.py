# https://www.acmicpc.net/problem/1874

import sys


n = int(sys.stdin.readline())
seq = list()
stack = list()
cur = 1
for i in range(n):
    num = int(sys.stdin.readline())
    while cur <= num:
        stack.append(cur)
        print("+")
        cur += 1
    if stack[-1] == num:
        stack.pop()
        print("-")
    else:
        print("NO")
        break
    # if num in stack:
    #     cur = len(stack) - stack.index(num)
    #     if cur == 0:
    #         stack.pop()
    #         print("-")
    #     else:
    #         for k in range(cur):
    #             stack.pop()
    #             print("-")
    # else:
    #     for j in range(num):
    #         stack.append(j + 1)
    #         print("+")
    #     stack.pop()
    #     print("-")
    #     # print(stack)