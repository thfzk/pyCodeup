# 021 ~ 030
'''
021 문자열 인덱싱
letters가 바인딩하는 문자열에서 첫번째와 세번째 문자를 출력하세요.
>> letters = 'python'
실행 예
p t
'''
py = 'python'
print(py[0], py[2])

'''
022 문자열 슬라이싱
자동차 번호가 다음과 같을 때 뒤에 4자리만 출력하세요.
>> license_plate = "24가 2210"
실행 예: 2210
'''
license_plate = '24가 2210'
print(license_plate[-4:])

'''
023 문자열 인덱싱
아래의 문자열에서 '홀' 만 출력하세요.
>> string = '홀짝홀짝홀짝'
실행 예:
홀홀홀

tip:
시작인덱스:끝인덱스:오프셋
'''
str = '홀짝홀짝홀짝'
print(str[::2])

'''
024 문자열 슬라이싱
문자열을 거꾸로 뒤집어 출력하세요.
>> string = "PYTHON"
실행 예:
NOHTYP
'''
str = 'PYTHON'
print(str[::-1])

'''
025 문자열 치환
아래의 전화번호에서 하이푼 ('-')을 제거하고 출력하세요.
>> phone_number = "010-1111-2222"
실행 예
010 1111 2222
'''
num = '010-1111-2222'
num1 = num.replace('-', ' ')
print(num1)

'''
026 문자열 다루기
25번 문제의 전화번호를 아래와 같이 모두 붙여 출력하세요.
실행 예
01011112222
'''
num = '010-1111-2222'
num = num.replace('-', '')
print(num)

'''
027 문자열 다루기
url 에 저장된 웹 페이지 주소에서 도메인을 출력하세요.
>> url = "http://sharebook.kr"
실행 예
kr
'''
url = 'http://sharebook.kr'
dom = url.split('.')
print(dom[-1])

'''
028 문자열은 immutable
아래 코드의 실행 결과를 예상해보세요.
>> lang = 'python'
>> lang[0] = 'P'
>> print(lang)
'''
# >> lang[0] = 'P' 부분에서 오류

'''
029 replace 메서드
아래 문자열에서 소문자 'a'를 대문자 'A'로 변경하세요.
>> string = 'abcdfe2a354a32a'
실행 예:
Abcdfe2A354A32A
'''
str = 'abcdfe2a354a32a'
str = str.replace('a', 'A')
print(str)

'''
030 replace 메서드
아래 코드의 실행 결과를 예상해보세요.
>> string = 'abcd'
>> string.replace('b', 'B')
>> print(string)
'''
# 그대로 출력됨