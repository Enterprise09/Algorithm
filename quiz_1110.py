# https://www.acmicpc.net/problem/1110

n = int(input())
cur = n
ctr = 0
while True:
    sum = (cur // 10 + cur % 10)
    new = (cur % 10 * 10 + sum % 10)
    ctr += 1
    if(new == n):
        print(ctr)
        break
    cur = new


# tensPlace = int(n // 10)
# onesPlace = int(n % 10)
# 

# while True:
#     ctr += 1
#     newNumber = int(onesPlace * 10 + int((tensPlace + onesPlace) % 10))
#     print(tensPlace, onesPlace)
#     if(newNumber == n):
#         print(ctr)
#         break
#     tensPlace = int(newNumber // 10)
#     onesPlace = int(newNumber % 10)