# https://www.acmicpc.net/problem/4344

c = int(input())    # 테스트 케이스 개수
for i in range(c):
    n = list(map(int, input().split()))
    avg = sum(n[1:]) / n[0]
    ctr = 0
    
    for j in n[1:]:
        if(j > avg):
            ctr += 1    # 평균을 넘는 학생 카운트
    rate = ctr / n[0] * 100
    print(f'{rate:.3f}%')   # 소수점 3자리까지 출력