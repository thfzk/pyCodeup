#9 기초-비트단위 논리연산
'''
[59]
입력 된 정수를 비트단위로 참/거짓을 바꾼 후 정수로 출력해보자.

예를 들어 1이 입력되었을 때 저장되는
1을 32비트 2진수로 표현하면 00000000 00000000 00000000 00000001 이고,
~1은 11111111 11111111 11111111 11111110 가 되는데 이는 -2를 의미한다.

Tip:
비트단위(bitwise)연산자 ' ~ ' 를 붙이면 된다.
(~ : tilde, 틸드라고 읽는다.)

**비트단위(bitwise) 연산자**
~(bitwise not),  
&(bitwise and),  
|(bitwise or),  
^(bitwise xor),
<<(bitwise left shift),  
>>(bitwise right shift)
틈새 자료구조(오버플로우 설명)

**참고**
컴퓨터에 저장되는 모든 데이터들은 2진수 형태로 바뀌어 저장된다.
0과 1로만 구성되는 비트단위들로 변환되어 저장되는데,
양의 정수는 2진수 형태로 바뀌어 저장되고,
음의 정수는 "2의 보수 표현"방법으로 저장된다.

예를 들어 파이썬에서는 int형(4바이트(byte), 32비트)으로
선언된 변수에 양의 정수 5를 저장하면
5의 2진수 형태인 101이 32비트로 만들어져
00000000 00000000 00000000 00000101
로 저장된다.(공백은 보기 편하도록 임의로 분리)

int 형의 정수 0은
00000000 00000000 00000000 00000000

그리고 -1은 0에서 1을 더 빼고 32비트만 표시하는 형태로
11111111 11111111 11111111 11111111 로 저장된다.

-2는 -1에서 1을 더 빼면 된다.
11111111 11111111 11111111 11111110 로 저장된다.

그래서 int 형으로 선언된 변수에는 최소 -2147483648 을 의미하는
10000000 00000000 00000000 00000000 부터

최대 +2147483647 을 의미하는
01111111 11111111 11111111 11111111 로 저장될 수 있는 것이다.

그렇다면 -2147483648
10000000 00000000 00000000 00000000 에서 1을 더 뺀다면?

01111111 11111111 11111111 11111111 이 된다.
즉 -2147483649 가 아닌 +2147483647 이 되는 것이다.

이러한 것을 "오버플로우(overflow, 넘침)"라고 한다.

이러한 내용을 간단히 표시하면, 정수 n이라고 할 때,

~n = -n - 1
-n = ~n + 1 과 같은 관계로 표현된다.
'''
i = ~int(input('입력 : '))
print(i)

'''
[60]
입력된 정수 두 개를 비트단위로 and 연산한 후 그 결과를 정수로 출력해보자.

예를 들어 3과 5가 입력되었을 때를 살펴보면
3 : 00000000 00000000 00000000 00000011
5 : 00000000 00000000 00000000 00000101
3 & 5 : 00000000 00000000 00000000 00000001
이 된다.

Tip:
비트단위(bitwise)연산자 &를 사용하면 된다.
(and, ampersand, 앰퍼센드라고 읽는다.)
비트단위 and 연산은 두 비트열이 주어졌을 때,
둘 다 1인 부분의 자리만 1로 만들어주는 것과 같다.
이 연산을 이용하면 어떤 비트열의 특정 부분만 모두 0으로도 만들 수 있는데
192.168.0.31   : 11000000.10101000.00000000.00011111
255.255.255.0 : 11111111.11111111.11111111.00000000

두 개의 ip 주소를 & 연산하면
192.168.0.0 : 110000000.10101000.0000000.00000000 을 계산할 수 있다.

실제로 이 계산은 네트워크에 연결되어 있는 두 개의 컴퓨터가 데이터를 주고받기 위해
같은 네트워크에 있는지 아닌지를 판단하는데 사용된다.

이러한 비트단위 연산은 빠른 계산이 필요한 그래픽처리에서
마스크연산(특정 부분을 가리고 출력하는)을 수행하는 데에도 효과적으로 사용된다
'''
a, b = map(int, input('입력 : ') .split())
print(a & b)

'''
[우리밋이 알려주는 Bonus 문제 (2)]
1개의 정수형 입력이 들어오면 비트 연산을 이용하여 '홀수'와 '짝수'를 판별하여라

Tip:
'짝수'와 '홀수'를 리스트에 담고 짝수일 때는 '짝수'를,
홀수일 때는 '홀수'를 출력하게 한다.
0이 아닌 어떠한 정수일지라도 1과 비트단위 논리곱(&)을 수행하게 되면
1이 되는 특성을 이용한다.
'''
i = int(input('입력 : '))
print(['짝수', '홀수'][i & 1])

'''
[61]
입력된 정수 두 개를 비트단위로 or 연산한 후 그 결과를 정수로 출력해보자.

예를 들어 3과 5가 입력되었을 때를 살펴보면
3 : 00000000 00000000 00000000 00000011
5 : 00000000 00000000 00000000 00000101
3 | 5 : 00000000 00000000 00000000 00000111
이 된다.

Tip:
비트단위(bitwise) 연산자 |(or, vertical bar, 버티컬바)를 사용하면 된다.
| 은 파이프(pipe)연산자라고도 불리는 경우가 있다.
비트단위 or 연산은 둘 중 하나라도 1인 자리를 1로 만들어주는 것과 같다.
이러한 비트단위 연산은 빠른 계산이 필요한 그래픽처리에서도 효과적으로 사용된다.
'''
a, b = map(int, input('입력 : ') .split())
print(a | b)

'''
[62]
입력된 정수 두 개를 비트단위로 xor 연산한 후 그 결과를 정수로 출력해보자.

예를 들어 3과 5가 입력되었을 때를 살펴보면
3 : 00000000 00000000 00000000 00000011
5 : 00000000 00000000 00000000 00000101
3 ^ 5 : 00000000 00000000 00000000 00000110
이 된다.

Tip:
비트단위(bitwise) 연산자 ^(xor, circumflex/caret,
서컴플렉스/카릿)를 사용하면 된다.
주의 ^은 수학식에서 거듭제곱(power)을 나타내는 기호와 모양은 같지만,
파이썬에서는 전혀 다른 배타적 논리합(xor, 서로 다를 때 1)의 의미를 가진다.

대체 텍스트
ex1) 10001010 => 138
     11111111 => 255
//=  01110101 => 117

ex2) 10001010 => 138
     00000000 => 0
//=  10001010 => 138

ex3) 10001010 => 138
     00001111 => 15
//=  10000101 => 133

이러한 비트단위 연산은 빠른 계산이 필요한 그래픽처리에서도 효과적으로 사용된다.

구체적으로 설명하자면,
두 장의 이미지가 겹쳐졌을 때 색이 서로 다른 부분만 처리할 수 있다.
배경이 되는 그림과 배경 위에서 움직이는 그림이 있을 때,
두 그림에서 차이만 골라내 배경 위에서 움직이는 그림의 색으로 바꿔주면
전체 그림을 구성하는 모든 점들의 색을 다시 계산해 입히지 않고
보다 효과적으로 그림을 처리할 수 있게 되는 것이다.
비행기 슈팅게임 등을 상상해보면 된다.
'''
a, b = map(int, input('입력 : ') .split())
print(a ^ b)

'''
[우리밋이 알려주는 Bonus 문제 (2-2]
해당 문제는 '카카오'와 '우아한 테크코스(이하 우테코)'의
실제 코딩 테스트 데모 문제였음을 알려드립니다.
카카오에서는 이 보다 훨씬 어려운 난이도의 코딩 문제들이 출제되며,
우테코에서는 우테코의 최고 난이도를 10으로 봤을 때 4~5 정도
(지극히 주관적 평가임을 유의)에 해당합니다.

참고 : 필자는 해당 사에서 출제된 문제들을 풀어봤을 뿐
실제 코딩 시험은 치뤄본 적이 없습니다.
문제 직사각형을 만드는 데 필요한 4개의 점 중 3개의 좌표가 주어질 때,
나머지 한 점의 좌표를 구하려고 합니다.
점 3개의 좌표가 들어있는 배열 v가 매개변수로 주어질 때,
직사각형을 만드는 데 필요한 나머지 한 점의 좌표를
return 하도록 solution 함수를 완성해주세요.

단, 직사각형의 각 변은 x축, y축에 평행하며,
반드시 직사각형을 만들 수 있는 경우만 입력으로 주어집니다.

제한사항

v는 세 점의 좌표가 들어있는 2차원 배열입니다.
v의 각 원소는 점의 좌표를 나타내며, 좌표는 [x축 좌표, y축 좌표] 순으로 주어집니다.
좌표 값은 1 이상 10억 이하의 자연수입니다.
직사각형을 만드는 데 필요한 나머지 한 점의 좌표를
[x축 좌표, y축 좌표] 순으로 담아 return 해주세요.
입력(1)

[[1,4], [3,4], [3,10]]
출력(1)

[1,10]
입력(2)

[[1,1], [2,2], [1,2]]
출력(2)

[2,1]
Tip:
나머지 한 점의 좌표는 기존에 좌표에서 없는 좌표이니,
1번만 입력된 좌표들을 찾아서 반환해주면 된다.
XOR 연산을 통해 구현할 수도 있으며, 이 경우 코드의 실행 속도가 굉장히 빠르다.
'''
# 기본 풀이
coordinates = [[1,4], [3,4], [3,10]]

answer = []
for i in range(2):
  if coordinates[0][i] == coordinates[1][i]:
    answer.append(coordinates[2][i])
  elif coordinates[0][i] == coordinates[2][i]:
    answer.append(coordinates[1][i])
  elif coordinates[1][i] == coordinates[2][i]:
    answer.append(coordinates[0][i])

print(answer)

# XOR 적용
coordinates = [[1,4], [3,4], [3,10]]

result = []
result.append(coordinates[0][0] ^ coordinates[1][0] ^ coordinates[2][0])
result.append(coordinates[0][1] ^ coordinates[1][1] ^ coordinates[2][1])

print(result)