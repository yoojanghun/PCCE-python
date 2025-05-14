# 자료형 변환: 데이터끼리 형식이 같다면 자료형을 변환할 수 있다.
# 문자열 데이터 변환: 문자열 정수(실수) => 숫자 정수(실수)
a = "100"
b = int(a)
c = int("200")

print(type(a), type(b), type(c))

# 아래처럼 하면 오류
# d = int("200.0")
# print(type(d))

a = "3.14"
b = float(a)
c = float("-5.5")
print(type(a), type(b), type(c))

# 아래처럼 하면 오류 아님
# d = float("200")
# print(type(d))

# 실수는 정수를 포함하므로,
# 정수를 실수로 바꾸는 것은 되지만,
# 실수를 정수로 바꾸는 것은 불가능

# 숫자 데이터 변환: 숫자 정수(실수) => 문자열 정수(실수)
a = 100
b = 3.14
c = str(a)
d = str(b)
e = str(200.0)
print(type(a), type(b), type(c), type(d), type(e))