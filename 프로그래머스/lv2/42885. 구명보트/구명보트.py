from collections import deque

def solution(people, limit):
    people_dq = deque(sorted(people, reverse=True))
    answer = 0
    
    while people_dq:
        if len(people_dq) == 1:
            answer += 1
            break
        if people_dq[0] + people_dq[-1] > limit and len(people_dq) >= 2:
            people_dq.popleft()
        else:
            people_dq.popleft()
            people_dq.pop()
        answer += 1
    return answer