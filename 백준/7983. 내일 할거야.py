# 7983. 내일 할거야
# https://www.acmicpc.net/problem/7983

import sys

n = int(sys.stdin.readline())
arr = []

for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

arr.sort(key=lambda x:-x[1])    # 마감일 기준으로 내림차순 정렬

play = arr[0][1] - arr[0][0]   # 노는 날을 첫 과제 기준으로 초기화
for i in range(n-1):
    if play < arr[i + 1][1]:   # 다음 과제 기간에 노는 경우
        arr[i + 1][1] = play 
    play = arr[i + 1][1] - arr[i + 1][0]   # 다음 과제 진행 후 다음 노는 날로 업데이트

print(play)