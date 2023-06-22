def solution(priorities, location):  # 우선순위, 내가알고싶은것
    answer = 0  # 실행 횟수
    while priorities:
        print(priorities)
        print(location, answer)
        is_continue = 1
        front = priorities.pop(0)
        for i in priorities:
            if i > front:  # 우선순위 미충족, 뒤로 보내기(append) 조건.
                priorities.append(front)
                if location == 0:  # location의 위치가 front인 경우 location 값을 맨 뒤로 보냄
                    location = len(priorities) - 1
                else:  # location이 맨 뒤가 아니라면 1을 빼줌
                    location -= 1
                is_continue = 0
                break
        if is_continue == 1:  # 위 for문에서 검사 결과 우선순위 조건 충족
            if location == 0:  # 목적 달성 프로그램 종료 조건
                answer += 1
                break
            else:  # 실행은 됐으나 목적을 달성 못함
                answer += 1
                location -= 1
    return answer