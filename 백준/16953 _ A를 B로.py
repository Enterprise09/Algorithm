# 16953. A -> B
# https://www.acmicpc.net/problem/16953

# B를 A로 만든다는 접근 방식으로 풀이한 모범답안
# 같은 문제를 BFS탐색을 이용하여 풀이할 수 있다.
a, b = map(int, input().split())
r = 1
while (b != a):
  r += 1
  temp = b
  if b % 10 == 1:  # 일의 자리가 1
    b //= 10
  elif b % 2 == 0:  # 짝수
    b //= 2

  if temp == b:
    print(-1)
    break
else:
  print(r)
