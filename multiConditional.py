# 다중 조건문: 조건문 안에 조건문이 있는 것
score = int(input("필기시험 점수를 입력하세요: "))

if score >= 80:
    interview = input("면접 결과를 입력하세요: ")
    if interview == "pass":
        print("최종 합격")
    else:
        print("불합격")
else:
    print("불합격")