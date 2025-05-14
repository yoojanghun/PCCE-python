# 다음 연산의 결과 예상
# integer + float = float
result = 100 + 20 / (4 - 2) * 5
print(result)

# 연산 우선순위
# 1. 괄호
# 2. 지수
# 3. 곱셈, 나눗셈, 몫, 나머지
# 4. 덧셈, 뺄셈
# 5. 같은 우선순위에서는 왼쪽 -> 오른쪽

# 시급, 일일 근무시간, 한달 동안 일한 날의 수, 이번 달 보너스 입력 => 이번달 급여 계산
# input으로 입력 받은 정보는 string
hour_wage = int(input())
work_hour = int(input())
day_work = int(input())
bonus = int(input())

total_wage = hour_wage * work_hour * day_work + bonus
print(total_wage)

# 4개 과목 점수 입력 => 과목의 중간고사 평균점수 출력
english = int(input())
math = int(input())
korean = int(input())
science = int(input())

avg_score = (english + math + korean + science) / 4
print(avg_score)