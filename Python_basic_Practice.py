# 파이썬 주석처리
# #%%를 통해 셀을 나누어 프로젝트 내부에서 각각의 코드를 진행 가능함
# 자바와 달리 ;와 같은 콜론을 필요로 하지 않음

#%%
# 숫자 자료형 Integer
print(5)
print(-10)
print(3.14)
print(1000)

# 연산 calculation
print(5+3)
print(2+8)
print(3*(3+1))
print(4/2)

#%%
# 문자열 자료형 String
print('this is string data')
print("this is string data")
print("this is long string data+++++++++++++++++++++++++++")
# tring data 내부에 연산자를 통해 여러번 반복 출력 진행도 가능함
print("this code is print this string data"*9)

#%%
# 참거짓 boolean
print(5 > 10)
print(5231 < 123)
# true or false
print(True)
print(False)
# true => false, false => true
print(not True)
print(not False)
print(not (5>10))

#%%
# 변수 variable
name = "연탄이"
animal = "강아지"
age = 10
hobby = "산책"
is_adult = age >= 6

# +를 통해 사용 시 int형을 출력을 원하면 무조건 str()를 통해 문자열로 변경시켜야 가능함
print("이름은 : " + name)
print("동물의 종은 : " + animal)
print("나이는 : " + str(age))
print("취마는 : " + hobby)
print("성인인가? : " + str(is_adult))

# ,로 연결 시 자료형 변경 없이 바로 사용가능 하지만 공백이 생긴다는 점이 특징
print("이름은 :" , name)
print("동물의 종은 :" , animal)
print("나이는 :" , str(age))
print("취마는 :" , hobby)
print("성인인가? :" , str(is_adult))

#%%
# 주석 Comment
# 주석 처리는 #이나 '''를 통해 진행함
'''
print("우리집 강아지의 이름은 연탄이에요") # 이름 소개
print("연탄이는 4살이며, 산책을 아주 좋아해요") # 나이, 취미 소개
print("연탄이는 어른일까요? True") # 어른인지 여부 확인
'''

#%% 연습문제
station = ["사당", "신도림", "인천공항"]
i = 2
print(station[i]+ "행 열차가 들어오고 있습니다.")

#%%
# 연산자 Operator (+ ,- ,* ,/ ,%)
print(1+1) #덧셈
print(3-2) #뺄셈
print(5*2) #곱셈
print(10/2) #나눗셈(몫)
print(10%2) #나눗셈(나머지)

# 부등호 inequality sign (>, >=, <, <=)
print(10 > 3) #~보다 크다
print(5 >= 5) #~보다 크거나 같다
print(3 < 4) #~보다 작다
print(3 <= 4) #~보다 작거나 같다

# 등호 equal sign (==, !=)
print(3==3)
print(1!=3)

# 논리 연산 logical operation (and, or, not)
print((3>0) and (3>0)) # and는 true + true = true
print((3>0) or (3>12)) # or는 true + false or false + true의 경우에 = true
print(not(1!=3)) # not은 무조건 반대를 출력함 true => false, false => true
'''
참고사항
a > b > c == (a>b) and (b>c)
만약 (a>b)에서 false가 나오면 뒤의 (b>c)는 진행X
'''

#%%
# 연산자 우선순위
print(2+3*4)
print((2+3)*4)

# 변수에 연산자를 추가할 경우
number = ((2*9)+3)
number = number + 2 #연산자로 +, -, /, % 모두 사용 가능
print(number)

#%%
# 숫자 처리 함수 (abs, pow, max, min, round) + 모듈 사용방법
print(abs(-5)) # abs (절댓값)
print(pow(4,2)) # pow (제곱) (소수점은 빼고 제곱값을 출력)
print(min(5, 12)) # min (가장 작은 값)
print(max(5, 12)) # max (가장 큰 값)
print(round(3.14)) # round (반올림)
print(round(4.99)) # round (반올림)

# math 모듈 
from math import * # (*를 import문에 입력하면 관련 모듈의 내용을 모두 불러와 사용하겠다는 의미이다.)
# math 모듈의 숫자처리 (floor, cell, sqrt)

print(floor(4.99)) # floor (내림)
print(ceil(3.14)) # ceil (올림)
print(sqrt(16)) # sqrt (제곱근 root)
 
#%% 
# random 랜덤함수 
# 랜덤함수는 난수 생성, 확률성, 로또번호 등 여러 방식으로 사용이 가능하다.

# 1. random 모듈 호출 (학습 과정에는 *로 모두 불러 사용해도 무관하지만 현업에서 사용시에는 필요한 모듈만 명확하게 사용할 것)
from random import *

# 2. random 랜덤함수 사용 예시 (따로의 값 지정 없이 사용 시 0.0 ~ 1.0 사이에서 생성된다)
print(random()) 
print(random()* 5)
print(random() * 10)
print(int(random() * 10)) # int형으로 감싸서 결과 값을 정수로 진행
print(int(random() * 10) + 1) # 기존의 0 ~ 10 사이의 랜덤값에 1을 더하여 1 ~ 11 사이로 변경

# 3. random 함수에 범위를 더한 함수들 (randrange, randint)
print(randrange(1, 256)) # 범위 마지막 숫자 미포함
print(randint(1,256)) # 범위 마지막 숫자 포함

# ++) 랜덤함수를 통해 로또 번호 생성을 만들고자 할 경우에는 각각의 랜덤함수를 6개 만들면 번호는 나오지만 
# 중복된 사건 즉 중복 숫자가 나올 가능성이 존재하기 때문에 이럴 경우에는 random 모둘 내의 simple() 함수를 사용하여 진행한다.

#%%
# 연습문제

# 조건 1 = 랜덤으로 날짜를 뽑아야 함 (랜덤 모듈 호출)
from random import *

# 조건 2 = 월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함 (randint 사용 시 28, randrange 사용 시 29로 설정)
# 조건 3 = 매월 1~3일은 스터디 준비를 해야 함으로 제외

date = randrange(4, 29)
# date = randint(4, 28)

print(" 오프라인 스터디 모임 날짜는 매월 " + str(date) + " 일로 선정되었습니다. ")
# print(" 오프라인 스터디 모임 날짜는 매월 " + date + " 일로 선정되었습니다. ")

#%%
# String 문자열
# 문자열은 문자들의 집합으로서 " ", '', ''' ''' 으로 묶어 사용이 가능하다

string_sentence1 = "파이썬 문자열은 string 으로서 여러 문자들의 집합을 표현이 가능하다."
string_sentence2 = '파이썬 문자열은 string 으로서 여러 문자들의 집합을 표현이 가능하다.'
string_sentence3 = '''
파이썬 문자열은 string 으로서 여러 문자들의 집합을 표현이 가능하다.
파이썬 문자열은 string 으로서 여러 문자들의 집합을 표현이 가능하다.
파이썬 문자열은 string 으로서 여러 문자들의 집합을 표현이 가능하다. '''

print(string_sentence1)
print(string_sentence2)
print(string_sentence3)

# %%
# Variable index 변수 인덱스 (슬라이싱 Slicing)
# 파이썬에서 data를 불러올 경우에 인덱스 형태를 통해 data에 번호를 붙여 필요할 경우 data[번호]를 통해
# 필요한 데이터를 가져와 사용이 가능하다. ++) 인덱스의 값은 0부터 시작하기 때문에 0 1 2 3 4 5 순으로 카운팅 해야 한다.

# 1. 변수명[인덱스] 구조
eulho = "001207-323456"
print("성별 : " + eulho[7])

# 2. 변수명[시작인덱스:종료인덱스] (:콜론 사용)
eulho = "001207-123456"
print("연 : " + eulho[0:2])
print("월 : " + eulho[2:4])
print("일 : " + eulho[4:6])

# 3. Slicing(슬라이싱) 변수명[:인덱스], 변수명[인덱스:], 변수명[:]
eulho = "001207-123456"

# 변수명[:인덱스] = 처음부터 인덱스 입력값 까지 슬라이싱
print("생년월일 : " + eulho[:6])

# 변수명[인덱스:] = 인덱스 입력값 부터 끝까지 슬라이싱
print("뒤 7자리 : " + eulho[7:])

# 변수명[:] = 처음부터 끝까지 슬라이싱
print("주민번호 : " + eulho[:])

#%%
# Using String Options 문자열 처리 함수 (lower, upper, isupper, islower, replace, index, find, count)
python_string = "Python is Amazing"

# 1. lower (소문자로 변환) 
print(python_string.lower())

# 2. upper (대문자로 변환)
print(python_string.upper())

# 3. isupper (대문자인지 확인)
print(python_string[0].isupper())
# print(python_string.isupper()) 문자열 전체로 검사 가능

# 4. islower (소문자인지 확인)
print(python_string[0].islower())
# print(python_string.islower()) 문자열 전체로 검사 가능

# 5. replace (문자열 바꾸기)
print(python_string.replace("Python","Java"))

# 6. index (찾을려는 문자열의 인덱스(없으면 에러))
index = python_string.index("n") # 처음으로 발견된 n의 인덱스
print(index)

index = python_string.index("n", index + 1) # 6번째 인덱스 이후의 발견된 n
print(index)

# print(python_string.index("Java")) Java 값이 없으면 오류 발생

# 7. find (찾으려는 문자열의 인덱스(없으면 -1))
find = python_string.index("n") # 처음으로 발견된 n의 인덱스
print(find)

find = python_string.index("n", index + 1) # 6 번째 인덱스 이후에 발견된 n의 인덱스
print(find)

print(python_string.find("Java")) # Java 값이 없으면 출력값 -1을 출력 후 다음 프로그램 진행

# 8. count (문자열이 나온 횟수)
print(python_string.count("n"))

# ++) len (문자열의 전체 길이 (띄어쓰기 포함)) 
# len은 문자열(string), 튜플(tuple), 리스트(list)에서 사용 가능하다. 
print(len(python_string))

#%%
# String Format (문자열 포멧)

# 1. %를 통한 문자열 삽입 (%d = (decimal)정수, %c = (character)문자, %s)
# 
#
#

# 2. .format

# 3. 문자열 내부에 {변수명}으로 지정 후 .format(변수명 = 변환할 data값)
