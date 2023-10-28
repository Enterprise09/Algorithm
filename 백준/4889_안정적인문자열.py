# 4889. 안정적인 문자열
# https://www.acmicpc.net/problem/4889

ans = []

while True:
  data = input()

  if '-' in data:
    break
  elif data == []:
    ans.append(0)
  else:
    ctr = 0
    stack = []
    for i in range(len(data)):
      if not stack and data[i] == '}':
        ctr += 1
        stack.append('{')
      elif stack and data[i] == '}':
        stack.pop()
      else:
        stack.append('{')
    ctr += len(stack) // 2
    ans.append(ctr)

for i in range(len(ans)):
  print(i + 1, '. ', ans[i], sep='')
