# 문제 1: 다음 문자열 데이터를 변수에 저장하고 출력해보세요
from multiprocessing.context import set_spawning_popen

country = "South Korea"
capital = "Seoul"
city = "Gang-nam"

# 콤마가 들어간 자리에 sep를 대신 적용할 수 있다.
print(country, capital, city, sep="\n")

# 문제 2: 다음과 같이 화면에 출력하도록 코드를 완성
singer1 = "Justin Bieber"
singer2 = "Charlie Puth"
song1 = "Off My Face"
song2 = "That's Hilarious"

print("Best Pop Songs")
print(singer1, "-", song1, sep="")
print(singer2, "-", song2, sep="")

print("Best Pop Songs")
print(singer1 + "-" + song1)
print(singer2 + "-" + song2)

# 이름을 사용자로부터 입력 받아서 환영 메세지를 완성
name = input()
print("Hello.", name + "님 Nice to meet you")

your_name = input("이름을 입력하세요: ")
your_age = input("나이를 입력하세요: ")

print("제 이름은", your_name + "입니다.")
print("나이는", your_age + "살 입니다.")
