# 9009. 피보나치
# https://www.acmicpc.net/problem/9009


# n보다 작은 수로 피보나치 수열 생성
def fibonacci(n):
  arr = [0, 1]
  i = 2

  while True:
    tmp = arr[i - 2] + arr[i - 1]
    if tmp > n:
      break
    else:
      arr.append(tmp)
    i += 1

  return arr


t = int(input())
for i in range(t):
  n = int(input())
  res = list()
  while n != 0:
    fi = fibonacci(n)
    n -= max(fi)
    res.append(max(fi))
  res.sort()
  for d in range(len(res)):
    print(res[d], end=' ')
