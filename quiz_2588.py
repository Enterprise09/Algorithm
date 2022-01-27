a = int(input())
b = int(input())

s = int(b % 10)
m = int((b % 100) / 10)
l = int(b / 100)

n3 = a * s
n4 = a * m
n5 = a * l
total = n3 + n4 * 10 + n5 * 100

print(n3)
print(n4)
print(n5)
print(total)