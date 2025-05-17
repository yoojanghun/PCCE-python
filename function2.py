# 함수 만들기
# def 함수 이름(매개변수1, 매개변수2):
#   명령 블록
#   return 반환 값

# 함수 호출
# 함수 이름(데이터1, 데이터2)

# 기본 함수 형태
def add_num(a, b):
    result = a + b
    return result

print(add_num(2, 3))

# return 문이 없는 함수
def div_num(a, b):
    print(a / b)

div_num(2, 5)

# 매개변수가 없는 함수
import random
def get_num():
    return random.randint(1, 100)

print(get_num())

# 결과값, 매개변수가 없는 함수
def say_hello():
    print("안녕하세요!!")
    print("반갑습니다!!")

say_hello()
say_hello()