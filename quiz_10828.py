# https://www.acmicpc.net/problem/10828

import sys

n = int(sys.stdin.readline())
stack = list()
for i in range(n):
    c = sys.stdin.readline().split()
    order = c[0]
    if(order == "push"):
        stack.append(c[1])
    elif(order == "pop"):
        if len(stack):
            print(stack.pop())
        else:
            print(-1)
    elif(order == "size"):
        print(len(stack))
    elif(order == "empty"):
        if len(stack):
            print(0)
        else:
            print(1)
    elif(order == "top"):
        if len(stack):
            print(stack[-1])
        else:
            print(-1)