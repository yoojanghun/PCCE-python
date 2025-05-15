# 조건문 속의 반복문




# 반복문 속의 조건문
# break: 가장 가까운 반복문을 종료

while True:
    order = input("명령 내려주세요: ")
    if order == "go":
        print("계속 진행합니다.")
    elif order == "stop":
        print("종료합니다.")
        break
    else:
        print("잘못 입력했습니다.")

# 숫자 1 => 게임을 시작합니다 출력
# 숫자 2 => 실시간 랭킹 출력
# 숫자 3 => 게임을 종료합니다 출력 프로그램 종료
# 나머지 => 다시 입력해 주세요 출력

while True:
    # n = int(input("[메뉴를 입력하세요] \n1. 게입시작 2. 랭킹보기 3. 게임종료 >>> "))
    print("[메뉴를 입력하세요]")
    select = int(input("1. 게입시작 2. 랭킹보기 3. 게임종료 >>> "))

    if select == 1:
        print("-> 게임을 시작합니다")
    elif select == 2:
        print("-> 실시간 랭킹")
    elif select == 3:
        print("-> 게임을 종료합니다")
        break
    else:
        print("다시 입력해 주세요")