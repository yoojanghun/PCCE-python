# python library: 누군가 미리 만들어 놓은 파이썬 코드
# 모듈: 라이브러리 안 파이썬 파일 하나
import random       # random 모듈

# 1 ~ 10 사이 랜덤한 정수 생성
print(random.randint(1, 10))

import time
print("Hello")
time.sleep(2)
print("이 메세지는 2초 뒤에 출력 됩니다.")
time.sleep(1.5)
print("이 메세지는 3.5초 뒤에 출력 됩니다.")

import turtle as t

# 거북이 모양으로 변경
t.shape("turtle")

# 거북이 색 변경
t.color("orange")

# 배경 색 변경
t.color("steelblue")

# 거북이 속도 조절 1 ~ 10
t.speed(1)

# 거북이 px 앞으로
t.forward(200)

# 방향 전환 (왼쪽으로 90도)
t.left(90)
t.forward(200)

# 특정 좌표로 이동
t.goto(0, 200)

# 펜 올리기 (이동 경로 안 그림)
t.penup()
t.forward(-200)

# 화면을 클릭할 때 종료
t.exitonclick()