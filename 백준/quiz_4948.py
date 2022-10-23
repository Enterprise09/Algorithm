# https://www.acmicpc.net/problem/4948

while True:
    c = int(input())
    sosu = []
    if(c == 0):
        break
    for i in range(c + 1, 2 * c + 1):
        check = 0
        for num in range(2, c):
            if(i % num == 0):
                check += 1
                break
        if(check == 0):
            sosu.append(i)
    print(len(sosu))
