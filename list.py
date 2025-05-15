# 리스트(List): 여러 개의 데이터를 저장할 수 있는 자료형
# 데이터를 인덱스를 통해 접근 가능
# 데이터를 수정, 추가, 삭제 가능
company_list = ["삼성전자", "SK 하이닉스", "네이버"]
print(company_list[0])
print(company_list[1])
print(company_list[2])

company_list[0] = "애플"
company_list[1] = "구글"
company_list[2] = "테슬라"
print(company_list)

company_list.append("아마존")
print(company_list)

del company_list[0]
print(company_list)

print(len(company_list))

# 리스트 슬라이싱
print(company_list[0:2])    # 0 ~ 1 인덱스까지 가져옴
print(company_list[:2])     # 0 ~ 1 인덱스까지 가져옴
print(company_list[1:3])     # 1 ~ 2 인덱스까지 가져옴
print(company_list[::2])     # step이 2개. 구글, 아마존만 출력

number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(number[0:10:2])
print(number[0:10:3])
print(number[9:-1:-1])      # 아무것도 출력 안 됨. 인덱스 -1은 가장 마지막 요소의 인덱스
                            # 인덱스 9에서 가장 마지막 요소(인덱스: -1) 이전까지 출력하면 아무것도 안 나옴
print(number[9::-1])
print(number[9:0:-1])