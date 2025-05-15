# 논리 연산: 다양한 조건을 만들 때 사용
# and, or, not

# 구독자 1000명 이상, 시청시간 4000시간 이상일 때 수익창출 가능
sub_count = int(input("현재 구독자 수: "))
watch_time = int(input("시청시간: "))

if sub_count >= 1000 and watch_time >= 4000:
    print("수익 창출 가능")
else:
    print("수익 창출 불가능")

# 팔굽혀펴기 30개 이상, 윗몸일으키기 35개 이상, 턱걸이 5개 이상.
# 셋 중 하나만 합격권에 들면 pass
push_up = int(input("팔굽혀 펴기: "))
sit_up = int(input("윗몸 일으키기: "))
chin_up = int(input("턱걸이: "))

if push_up >= 30 or sit_up >= 35 or chin_up >= 5:
    print("Pass!!")
else:
    print("Fail")