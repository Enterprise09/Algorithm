# 팩토리얼 구현 예제


def factorial_recursive(n):
  if n <= 1:
    return 1
  return n * factorial_recursive(n - 1)


N = int(input())

print(factorial_recursive(N))
