# 바둑돌을 볼링 핀 처럼 쌓음
# n이 입력으로 주어질 때 n 단계에서 사용된 바둑돌의 갯수를 출력

# 몫의 계산법 //을 이용하면 int가 출력됨.
# 그냥 나눗셈하면 float가 출력됨.
n = int(input())
sum = (1 + n) * n // 2

print(sum)

# 1부터 5까지 자연수를 자연수 n으로 나눈 나머지를 출력
n = int(input())
print(1 % n)
print(2 % n)
print(3 % n)
print(4 % n)
print(5 % n)
