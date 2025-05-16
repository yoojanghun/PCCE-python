# 2차원 리스트: 리스트의 원소로 리스트를 사용한다.
# 리스트 이름[바깥쪽 리스트 인덱스][안쪽 리스트 인덱스]

person_info_list = [
    ["유재석", 51, "남"],
    ["노홍철", 44, "남"],
    ["하하", 44, "남"]
]

# 유재석 이름
print(person_info_list[0][0])

# 하하 나이
print(person_info_list[2][1])

# 새로운 리스트 추가
person_info_list.append(["정준하", 50, "남"])

print(person_info_list)