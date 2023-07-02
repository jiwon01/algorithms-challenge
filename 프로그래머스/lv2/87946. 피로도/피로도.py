"""
경우의 수를 계산하기 위해, itertools 라이브러리를 이용하여 순열(permutations)을 사용하였음.
순열을 구한 뒤 완전탐색답게 모든 경우의 수를 뒤졌음

answer_list를 reverse True 정렬하여 제일 큰 수를 리턴함.
 
"""
from itertools import *

def solution(k, dungeons):  # 현재 피로도, [최소 필요, 소모 피로]
    answer = -1
    answer_list = []
    lists = list(permutations([i for i in range(len(dungeons))], len(dungeons)))
    
    for idx in lists:
        hp = k
        result = 0
        for i in idx:
            if hp >= dungeons[i][0]:
                hp -= dungeons[i][1]
                result += 1
            else:
                continue
        if result > 0:
            answer_list.append(result)
        
    answer_list.sort(reverse=True)
    return answer_list[0]