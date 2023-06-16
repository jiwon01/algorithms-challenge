def solution(arr):
    answer = []
    is_used = 10
    for i in arr:
        if i != is_used:
            answer.append(i)
            is_used = i
    return answer