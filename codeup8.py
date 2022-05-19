#8. 기초-논리연산
'''
[53]
1(true, 참) 또는 0(false, 거짓) 이 입력되었을 때
반대로 출력하는 프로그램을 작성해보자.

**참고**
파이썬에서 비교/관계 연산(==, !=, >, <, >=, <=)이 수행될 때,
0은 거짓(false)으로 인식되고, 0이 아닌 모든 수는 참(true)으로 인식된다.

참 또는 거짓의 논리값을 역(반대)으로 바꾸기 위해서는
논리(logical)연산자 'not'를 사용할 수 있다.
이러한 논리연산을 NOT 연산이라고 부른다.

참, 거짓의 논리값(boolean value)인 불 값을 다루어주는 논리연산자는
'not', 'and', 'or'가 있다.

** 불 대수(boolean algebra)는 수학자 불이 만들어낸 것으로
참/거짓만 가지는 논리값과 그 연산을 다룬다.

Tip:
참 또는 거짓의 논리값을 역(반대)으로 바꾸기 위해서는
논리(logical)연산자 'not'를 사용할 수 있다.
'''
i = int(input('입력 : '))
print(not i)

'''
[54]

두 개의 참(1) 또는 거짓(0)이 입력될 때,
모두 참일 때에만 참을 출력하는 프로그램을 작성해보자.

Tip:
파이썬에서는 AND연산값이 참이면 뒤에 있는 값을 출력하게 된다.
ex) '앞' and '뒤' >> '뒤'
'''
for i in range(4):
    a, b = map(int, input('입력 : ') .split())
    print(a and b)
    
'''
[55]
두 개의 참(1) 또는 거짓(0)이 입력될 때,
하나라도 참이면 참을 출력하는 프로그램을 작성해보자.

Tip:
파이썬에서는 OR연산값이 참이면 참인 값을 출력하게 된다.
ex) '참' or 0 >> '참
ex) 0 or True >> True
'''
for i in range(4):
      a, b = map(int, input('입력 : ') .split())
      print(a or b)
      
'''
[우리밋이 알려주는 Bonus 문제 (1)]
1개의 정수형 입력이 들어오면 논리 연산을 이용하여 '홀수'와 '짝수'를 판별하여라

Tip:
입력이 2로 나눠지면 짝수이고, 그렇지 않으면 홀수임을 이용한다.
파이썬에서의 AND와 OR의 특징을 이용한다.
=> 파이썬에서는 이러한 연산을 "삼항 연산"으로 정의한다.
(삼항연산은 Chapter 10에서 다룬다)
'''
i = int(input('입력 : '))
print(i%2 and '홀수' or '짝수')

'''
[56]
두 가지의 참(1) 또는 거짓(0)이 입력될 때,
참/거짓이 서로 다를 때에만 참을 출력하는 프로그램을 작성해보자.

Tip:
이러한 논리연산을 XOR(exclusive or, 배타적 논리합)연산이라고도 부른다.
이를 표현하기 위해서는 (a AND (NOT b)) OR ((NOT a) AND b)처럼 하면 된다.
'''
for i in range(4):
      a, b = map(int, input('입력 : ') .split())
      print((a and (not b)) or ((not a) and b))
      
'''
[57]
두 개의 참(1) 또는 거짓(0)이 입력될 때,
참/거짓이 서로 같을 때에만 참이 계산되는 프로그램을 작성해보자.

Tip:
AB | ?
00 | 1
01 | 0
10 | 0
11 | 1
notA and notB or A and B
'''
for i in range(4):
      a, b = map(int, input('입력 : ') .split())
      print(((not a) and (not b)) or (a and b))

'''
[58]
두 개의 참(1) 또는 거짓(0)이 입력될 때,
모두 거짓일 때에만 참이 계산되는 프로그램을 작성해보자.

Tip:
AB | ?
00 | 1
01 | 0
10 | 0
11 | 0
notA and notB = not(A or B)
'''
for i in range(4):
      a, b = map(int, input('입력 : ') .split())
      print(not(a or b))