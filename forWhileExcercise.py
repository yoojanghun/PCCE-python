# 사용자로부터 자연수 n과 m을 입력 받으면, n부터 m까지의 합계를 계산

n = int(input())
m = int(input())

sum = 0
for i in range(n, m + 1):
    sum += i

print(sum)

# for을 while로 바꾸기
# for i in range(1, 11, 2):
#    print(i)

i = 1
while i < 11:
    print(i)
    i += 2

# 사용자로부터 출력할 구구단 입력 받음. 해당 구구단 출력
n = int(input("몇 단을 출력할까요?: "))

for i in range(1, 10):
    print(n, "*", i, "=", n * i)
print()

# f-string: 문자열과 변수를 조합해서 문자를 나타낼 수 있다.
# 문자열은 그대로
# 변수 자리엔 {변수}로 씀
for i in range(1, 10):
    print(f"{n} * {i} = {n * i}")