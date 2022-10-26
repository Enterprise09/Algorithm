# 스택 구현 예제
stack = []

stack.append(2)
stack.append(6)
stack.append(1)
stack.pop()  # return 1

stack.append(9)
stack.append(3)
stack.pop()  # return 3

print(stack[::-1])  # 최상단 원소부터 출력(거꾸로)
print(stack)

# 9, 6, 2
# 2, 6, 9