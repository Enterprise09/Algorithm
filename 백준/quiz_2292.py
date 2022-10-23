# https://www.acmicpc.net/problem/2292

n = int(input())
ctr = 1
column = 1
while n > column:
    column += 6 * ctr   # 6의 배수로 계속하여 증가
    ctr += 1
print(ctr)

# 증가를 진행하다가 입력된 수(n) 보다 column의 값이 커지면
# 즉, 해당줄(ctr)에서 가장 큰 수가 n(입력된 수)보다 커지면
# n은 해당줄(ctr)에 포함되어 있음으로 
# while문을 종료하고 몇번째 줄에 있는지 출력한다.