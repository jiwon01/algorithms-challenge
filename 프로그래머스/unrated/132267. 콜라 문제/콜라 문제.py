def solution(a, b, n):  # 마트에 주는 수, 콜라 주는 수, 빈 병 수
    answer = 0
    # 내 병 = 내 병 - 마트에서 가져가는 병 + 빈 병
    while n >= a:  # (내가 가진 병이 마트에 주는 것보다 많을 때) == True 동안 구동
        n = n - a + b
        answer += b
    return answer