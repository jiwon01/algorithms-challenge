def solution(ingredient):
    answer = 0
    index = 0
    while index < len(ingredient) - 3:
        if ingredient[index:index+4] == [1,2,3,1]:  # 빵 조합이면 진행
            del ingredient[index:index+4]  # 해당 배열 삭제
            answer += 1  # answer +1
            index -= 3  # 다시 3자리 전으로 돌아가서 1이 있는지 확인
            continue  # index + 1하지 않고 다시 반복
        index += 1  # 다음번 계산을 위해 index 올림
    return answer