def solution(storey):
    array = list(map(int, str(storey))) 
    array.reverse()
    answer = 0
    i = 0
    while True:
        # 예외 처리 (현재 숫자가 10인 경우)
        if array[i] == 10:
            if i + 1 == len(array): # 현재 원소가 리스트에서 마지막인 경우 리스트에 1을 추가함. 아니면 그냥 다음 원소에 1을 더함.
                array.append(1)
            else:
                array[i + 1] += 1
        # 4 이하
        elif array[i] <= 4:
            if i + 1 == len(array):
                return answer + array[i]
            answer += array[i]
        # 5
        elif array[i] == 5:
            if i + 1 == len(array):  
                return answer + array[i]
            elif array[i + 1] <= 4:
                answer += array[i]
            elif array[i + 1] >= 5:
                if i + 1 == len(array):
                    array.append(1)
                else:
                    array[i + 1] += 1
                answer += 5
        # 6 이상
        elif array[i] >= 6:
            if i + 1 == len(array):
                array.append(1)
            else:
                array[i + 1] += 1
            answer += 10 - array[i]
        i += 1
    return "error"