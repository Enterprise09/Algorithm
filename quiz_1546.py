# https://www.acmicpc.net/problem/1546

N = int(input())
scores = list(map(int, input().split()))
sum = 0
for i in range(N):
    sum += scores[i] / max(scores) * 100
print(sum / N)