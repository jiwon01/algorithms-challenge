# 테스트 9: 7.92ms,  테스트 10: 5.67ms
def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)  # 크기가 큰 순대로 재배열 (내림차순)
    for i in range(0, len(score), m):  # 박스 개수만큼 반복
        if i + m <= len(score):  # i + m - 1한 값이 score의 길이를 초과하면 오류 발생
            answer += m * score[i + m - 1]  # 사과개수 * 최저값을 구하고 answer 변수에 더하기
        # del score[:m]
    return answer


# 박스의 개수를 따로 구하고 그 개수를 통해서 for문을 돌렸음. 
# 소스 짜는게 편의를 위해서 계산한 배열을 잘라가면서 구동하도록 구성함. -> 시간 초과의 원인
# 테스트 9: 68.09ms,  테스트 10: 50.47ms, 테스트 11~15 시간초과
def solution1(k, m, score):
    answer = 0
    score.sort(reverse=True)  # 크기가 큰 순대로 재배열 (내림차순)
    box = len(score) // m  # 박스의 개수를 계산하여 box 변수에 저장
    for _ in range(box):  # 박스 개수만큼 반복
        answer += m * score[m - 1]  # 사과개수 * 최저값을 구하고 answer 변수에 더하기
        del score[:m]
    return answer


########################### 참고한 소스
# 파이써닉하게 줄이기 전
# def solution(k, m, score):
#     answer = 0
#     score.sort(reverse=True) 
#     for i in range(0,len(score),m):
#         if i+m<=len(score):
#             answer += score[i+m-1]
#     answer = answer*m
#     return answer