# 1374. 강의실
# https://www.acmicpc.net/problem/1374

import sys
import heapq
input = sys.stdin.readline

n = int(input())
arr = []
heap = []

# get input
for i in range(n):
    arr.append(list(map(int, input().split())))
# arr = [[no, start, end], ...]

# 시작 시간 기준 ASC
arr.sort(key=lambda x:x[1])
res = 0
for i in arr:
    # 진행중인 강의 종료시간과 다음 강의 시작 시간 비교
    while heap and heap[0] <= i[1]:
        heapq.heappop(heap)
    heapq.heappush(heap, i[2])
    res = max(res, len(heap))

print(res)
