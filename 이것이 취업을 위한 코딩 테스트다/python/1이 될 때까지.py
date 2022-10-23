# 작성한 코드 > 시간 복잡도 . . .
# n, k = map(int, input().split())
# count = 0

# while True:
#   if(n == 1):
#     break;
#   else:
#     if(n % k == 0):
#       n //= k
#     else:
#       n -= 1
#     print(n)
#     count += 1

# print(count)

#############################################
# 동빈나 선생님의 코드 - 시간 복잡도가 우수한 모범 코드
n, k = map(int, input().split())

count = 0
while True:
  # 나누어 떨어지는 값을 구함
  target = (n // k) * k

  # 1로 빼는d회수를 구함
  count += (n - target)
  n = target
  if n < k:
    break
  count += 1
  n //= k
  print("count: ", count, "\tn: ", n)

count += (n - 1)
print(count)