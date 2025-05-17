# 문자열 함수: 문자열을 다루는 함수

# count: 문자열 안에서 문자 개수 찾기
message = "만나서 반갑습니다. 저는 이니만 입니다. 만나서 반갑습니다"
print(message.count("만나서"))
print(message.count("만"))

# find: 문자열 안에서 문자 위치 찾기
name = "YooJanghun"
print(name.find("hun"))
print(name.find("o"))
# 가장 처음 나오는 문자의 index를 반환

# replace: 문자열 안에서 문자 바꾸기
new_name = name.replace("o", "X")
print(new_name)
new_message = message.replace("반갑습니다", "안 반갑습니다")
print(new_message)

# split: 문자열 안에서 문자 자르기
text = "파이썬은 매우 쉽습니다."
text_list = text.split()
print(text_list)

fruits = "orange, strawberry, pineapple"
fruits_list = fruits.split("a")
print(fruits_list)
# 문자 a를 기준으로 자른다. a는 없애고 나머지들은 list에 넣어 놓는다.