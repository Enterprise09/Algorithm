# https://www.acmicpc.net/problem/8958

n = int(input())
result = []
for i in range(n):
    ctr = 0
    score = 0
    arr = list(map(str, input()))
    for j in range(len(arr)):
        if(arr[j] == 'O'):
            ctr += 1
            score += ctr * 1
        else:
            ctr = 0
    result.append(score)

for i in range(len(result)):
    print(result[i])