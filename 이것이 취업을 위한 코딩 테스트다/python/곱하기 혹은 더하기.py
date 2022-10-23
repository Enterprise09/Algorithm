data = input()

result = int(data[0])  # 초기값 지정

for i in range(1, len(data)):
  num = int(data[i])
  # result 값에 누적 계산
  if num <= 1 or result <= 1:  # 한쪽이라도 0, 1인 경우 더하기 연산
    result += num
  else:  # 나머지에 대해서는 곱셉 연산
    result *= num

print(result)
