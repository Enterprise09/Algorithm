# 25391. 특별상
# https://www.acmicpc.net/problem/25391

import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
score = []
winner = []

# score
for i in range(n):
    score.append(list(map(int, input().split())))

# 주최자 점수 높은 순 정렬
score.sort(key=lambda x:-x[0])
winner = score[:m]

# 심판 점수 높은 순 정렬
score.sort(key=lambda x:-x[1])
idx = 0
# 중복 수상 여부 확인
while True:
    if score[idx] not in winner:
        winner.append(score[idx])
    if len(winner) >= m + k:    # 본상 선정완료 시 종료
        break
    idx += 1

res = 0
for i in range(len(winner)):
    res += winner[i][0]
print(res)