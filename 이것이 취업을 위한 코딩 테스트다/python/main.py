S = list(input())
ctr = 0

for i in S:
  if i.isalpha():
    continue
  ctr += int(i)
  S.remove(i)

if ctr != 0:
  S.append(str(ctr))

print(''.join(S))  # 문자열과 조인시켜서 str형으로 변환