# https://www.acmicpc.net/problem/4673

numbers = set(range(1, 10001))  # 1 - 10000
create_numbers = set()  # 생성자 저장소

for number in numbers:
    sum = number
    for n in str(number):
        sum += int(n)
    create_numbers.add(sum)     # 생성자 저장
result = (numbers - create_numbers)     # set형 차집합 연산
for i in sorted(result):
    print(i)