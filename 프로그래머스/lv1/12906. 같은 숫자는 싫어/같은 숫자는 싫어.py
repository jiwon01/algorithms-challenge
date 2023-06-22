def solution(arr):
    answer = []
    is_used = None # 원소 값의 범위는 0~9라서 10이라고 가정
    for i in arr:
        if i != is_used:
            answer.append(i)
            is_used = i
    return answer