# 제어문: 반복문, 조건문
# 조건문: 조건에 따라 실행할 명령을 선택하는 것

orgin_pass = "1234"
input_pass = input("비밀번호 입력: ")

if orgin_pass == input_pass:    # 조건 A
    # 조건 A 참
    print("로그인 성공!")
    print("반갑습니다!")
elif input_pass == "":          # 조건 B
    # 조건 A 거짓, 조건 B 참
    print("당신은 아무것도 입력 안 함.")
else:
    # 조건 A 거짓, 조건 B 거짓
    print("로그인 실패!")
    print("반갑지 않습니다!")

print("프로그램 종료")

