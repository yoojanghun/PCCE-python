# 다중 반복문: 반복문 안에 또다시 반복문이 있는 것

for i in range(5):
    for j in range(5):
        print(f"i = {i}, j = {j}")

# 다음 모양의 별을 출력해보자 (단 곱셈연산을 이용하지 않는다)
for i in range(5):
    for j in range(i + 1):
        print("*", end="")
    print()

for i in range(5):
    for j in range(5 - i):
        print("*", end="")
    print()

for i in range(5):
    for k in range(4 - i):
        print(" ", end="")
    for j in range(2 * i + 1):
        print("*", end="")
    print()