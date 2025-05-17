def solution(num_list):
    answer = []
    for num in num_list:
        is_decimal = True               # 소수인가? flag 변수 => True
        for i in range(2, num):
            if num % i == 0:
                answer.append(False)
                is_decimal = False
                break
        if is_decimal == True:
            answer.append(True)

    return answer