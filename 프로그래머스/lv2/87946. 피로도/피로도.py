"""
경우의 수를 계산하기 위해, itertools 라이브러리를 이용하여 순열(permutations)을 사용하였음.
순열을 구한 뒤 완전탐색답게 모든 경우의 수를 뒤졌음

answer_list를 reverse True 정렬하여 제일 큰 수를 리턴함.
 
"""
from itertools import permutations  # 수열 사용

def solution(k, dungeons):  # 현재 피로도, [최소 필요, 소모 피로]
    answer_list = []
    # dungeons 길이만큼 리스트를 생성[0, 1, 2], 이 리스트를 dungeons의 길이 만큼 순열 생성하여 lists에 리스트 저장.
    lists = list(permutations([i for i in range(len(dungeons))], len(dungeons)))
    #print(lists)
    
    for idx in lists:  # lists 원소 만큼 반복. idx = [0, 1, 2] ... 
        hp = k  # k를 hp 변수에 매번 저장함.
        result = 0  # 각 경우의 수에서 나온 result
        for i in idx:  # 경우의 수가 담긴 idx(0, 1, 2) 또는 (0, 2, 1) 같이... 반복
            if hp >= dungeons[i][0]:  # 현재 hp가 던젼의 최소로 요구하는 피로도가 충분한가?
                hp -= dungeons[i][1]  # 던전에서 사용한 피로도를 hp에서 깎음
                result += 1  # result +1 해줌
            else:  # 피로도에 만족하지 못하므로 걍 다음으로
                break
        if result > 0:  # 위 계산 결과가 0을 초과하는가?
            answer_list.append(result)  # answer_list에 추가
        
    answer_list.sort(reverse=True)  # 제일 큰 값이 앞으로 오도록 정렬
    #print(answer_list)
    return answer_list[0]  # 제일 큰 값이 리턴됨.