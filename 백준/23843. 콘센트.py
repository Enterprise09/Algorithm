# 23843. 콘센트
# https://www.acmicpc.net/problem/23843

import sys
import heapq

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

arr.sort(reverse=True)
heap = []       # 콘센트 역할

for a in arr:
    if len(heap) < m:   # 충전 가능한 콘센트가 있는 경우
        heapq.heappush(heap, a)
    else:               # 모든 콘센트가 충전 중인 경우
        res = heapq.heappop(heap)
        heapq.heappush(heap, res + a)

print(max(heap))