# 정수들을 담은 nums 리스트가 있다.
# nums 안의 원소들 중에서 가장 작은 수를 찾는 프로그램

nums = [5, 15 ,2, -8, -12, -29, 43, 1]

min = nums[0]
for num in nums:
    if num < min:
        min = num

print(f"최솟값은 {min} 이다")

# 홀수 번째 원소들의 합계를 구하는 프로그램
sum = 0
for i in range(0, len(nums), 2):
    sum += nums[i]
print(sum)

i = 1
sum = 0
for num in nums:
    if i % 2 == 1:
        sum += num
    i += 1
print(sum)

# 로또 번호 추출기. 1~45 중 6개의 번호를 추출 (단 번호 중복 X)
# 리스트와 파이썬 멤버십 연산자 이용
# import random
# list = [0]
#
# i = 0
# while True:
#     if list[i] not in list:           항상 False. list[i]는 list안에 반드시 포함되기 때문
#         list.append(random.randint(1, 45))
#     i += 1
#     if len(list) == 6:
#         break
#
# print(list)
import random
lotto = []

while len(lotto) < 6:
    num = random.randint(1, 45)
    if num not in lotto:
        lotto.append(num)

for num in lotto:
    print(num, end=" ")