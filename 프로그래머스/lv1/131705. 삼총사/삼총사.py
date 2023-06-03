def solution(number):
    answer = 0
    without_current_array = []
    without_current_array2 = []
    current_count = 0

    for i in number: # 한 원소가 선택이 됨.
        without_current_array = number[:]
        without_current_array.remove(i)  # number 리스트에서 i만 쏙 뺌.
        # print(without_current_array)
        for j in without_current_array:
            without_current_array2 = without_current_array[:]
            without_current_array2.remove(j)  # number 리스트에서 i만 쏙 뺌.
            # print(without_current_array2)
            for k in without_current_array2:
                if i + j + k == 0:
                    answer += 1
    return answer // 6