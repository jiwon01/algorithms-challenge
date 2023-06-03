def solution(N, stages):
    answer = []
    users = [0] * (N+2)
    failure_rates = []
    total_users = 0
    
    # users(스테이지당 인원수) 변수에 인원 업데이트
    for j in stages:
        users[j] += 1
    
    # 실패율 계산
    for i in range(1, N+1):
        total_users = sum(users[i:])
        if total_users == 0:
            failure_rate = 0
        else:
            failure_rate = users[i] / total_users
        failure_rates.append((i, failure_rate))
    
    # 정렬 및 (1, 2)중 1만 리턴
    failure_rates.sort(key=lambda x: (-x[1], x[0]))
    return [stage for stage, _ in failure_rates]