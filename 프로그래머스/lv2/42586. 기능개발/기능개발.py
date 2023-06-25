def solution(progresses, speeds):
    # 며칠이 걸리는 지에 대한 array(Queue)를 만듦
    how_many_days = []
    for i, value in enumerate(progresses):
        # 100 - value = ?
        bbegi = 100 - value
        # ? % speeds[i] = ?
        if bbegi % speeds[i] == 0:
            how_many_days.append(bbegi // speeds[i])
        else:
            how_many_days.append((bbegi // speeds[i])+1)
    print(how_many_days)

    # 위 선입선출 방식의 큐를 이용하여 계산 수행
    current_pointer = 0  # answer array의 위치 표시
    current_num = None  # 현재 계산 중인 숫자 정보
    answer = []  # return할 정답 변수
    
    for i in range(0, len(how_many_days)):
        if current_num == None:  # 처음 돌아가나요
            current_num = how_many_days[i]
            answer.append(1)
            continue
        if current_num >= how_many_days[i]:  # 앞서 있는 원소보다 숫자가 작나요?
            answer[current_pointer] += 1
        else: # 큰 경우
            current_pointer += 1
            current_num = how_many_days[i]
            answer.append(1)
            
    return answer