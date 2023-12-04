# 2195. 문자열 복사
# https://www.acmicpc.net/problem/2195

import sys

S = list(sys.stdin.readline().strip())      # use .strip() to remove '\n' 
P = list(sys.stdin.readline().strip())

i = 0
ctr = 0

while i < len(P):
    j = 0
    tmp = 0
    maxV = 0
    while j < len(S) and tmp + i < len(P):
        if P[i + tmp] == S[j]:
            tmp += 1
            maxV = max(maxV, tmp)
        else:
            tmp = 0
        j += 1
    ctr += 1
    i += maxV
print(ctr)