def solution(my_string, n):
    answer = ""
    skip = len(my_string) - n
    for idx, v in enumerate(my_string):
        if idx >=skip:
            answer += v
    return answer