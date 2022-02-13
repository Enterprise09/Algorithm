# https://www.acmicpc.net/problem/1065

n = int(input())
ctr = 0
for number in range(1, n + 1):
    if(number < 100):
        ctr += 1
    else:
        lists = list(map(int, str(number)))
        if(lists[0] - lists[1] == lists[1] - lists[2]):
            ctr += 1
print(ctr)

