# https://www.acmicpc.net/problem/3052

arr = set()
for i in range(10):
    n = int(input())
    arr.add(n % 42)  # 중복되는 값을 set형을 이용하여 제거
print(len(arr))