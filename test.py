scap = 0
for i in range(int(input())):
    a, b = map(int, input() .split())
    scap += b % a
print(scap)