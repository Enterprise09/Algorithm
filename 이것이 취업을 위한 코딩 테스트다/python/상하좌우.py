n = int(input())  # 공간의 크기
x, y = 1, 1  # 시작하는 좌표
plans = input().split()  # 이동할 경로 입력
type = ['L', 'R', 'U', 'D']  # 이동 방향 리스트에 정의

# 리스트에 저장돤 이동 방향을 방향 벡터로 저장
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for plan in plans:
  # 바로 가져오지 않는 이유는 인덱스를 활용해야 하기 때문이다.
  for i in range(len(type)):
    if plan == type[i]:
      nx = x + dx[i]
      ny = y + dy[i]
  if nx < 1 or ny < 1 or nx > n or ny > n:
    continue
  x, y = nx, ny
  print("TEMP: ", x, y)
print(x, y)