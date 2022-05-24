n = int(input('입력 : '))
number = list(map(int, input('입력 : ') .split()))

def goto(number, n, i):
  if i == n: return
  print( number[i] )
  i += 1
  goto(number, n, i)

goto(number, n, 0)