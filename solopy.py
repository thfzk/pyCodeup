n = int(input('입력 : '))
j = list(map(int, input('입력 : ') .split()))

j.sort()

hap = 0
cnt = 0

print(j)

for i in j:
  cnt = cnt + 1
  if cnt >= i:
    hap = hap + 1
    cnt = 0
    
print(hap)