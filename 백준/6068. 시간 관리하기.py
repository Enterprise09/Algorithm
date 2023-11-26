# 6068. 시간 관리하기
# https://www.acmicpc.net/problem/6068

import sys

n = int(sys.stdin.readline())
arr = []

for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

arr.sort(key=lambda x:-x[1])
play = arr[0][1] - arr[0][0]

for i in range(1, n, 1):
    if play < arr[i][1]:
        arr[i][1] = play
    play = arr[i][1] - arr[i][0]

if play < 0:
    play = -1

print(play)