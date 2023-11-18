# 19598. 최소 회의실 개수
# https://www.acmicpc.net/problem/19598

import heapq
import sys

n = int(input())
res = 1
arr = []

for i in range(n):
    tmp_arr = list(map(int, sys.stdin.readline().split()))
    arr.append(tmp_arr)

# 우선순위큐 이용
arr.sort()
heap = []
heapq.heappush(heap, arr[0][1])

for i in range(1, n):
    if arr[i][0] >= heap[0]:
        heapq.heappop(heap)
    else:
        res += 1
    heapq.heappush(heap, arr[i][1])

print(res)


# 모든 케이스를 통과하지만 틀렸습니다. (시간초과 X)
# arr.sort(key=lambda x:x[0])

# for i in range(n-1):
#     start = arr[i+1][0]
#     endof = arr[i][1]
#     if endof > start:
#         res += 1

# print(res)