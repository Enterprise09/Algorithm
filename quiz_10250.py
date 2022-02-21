# https://www.acmicpc.net/problem/10250

t = int(input())
for i in range(t):
    h, w, n = map(int, input().split())
    # 1 <= n <= h * w
    room = n // h + 1
    floor = n % h
    if(n % h == 0):
        room = n // h
        floor = h
    print(f'{floor * 100 + room}')
