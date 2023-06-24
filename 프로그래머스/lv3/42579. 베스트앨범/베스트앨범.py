"""
1. 딕셔너리를 통해 종류별 정리
2. 분류 (당 2개)
 - 분류 내 합이 제일 큰 것
 - 분류 내 큰 순서대로 (sort)
3. 출력
"""

def solution(genres, plays):  # 장르, 재생횟수
    answer = []
    _dict = {}
    _dict_sum = []
    temp = 0
    # _dict
    for key, value in enumerate(genres):
        if value in _dict:
            _dict[value].append([plays[key], temp])
        else:
            _dict[value] = [[plays[key], temp]]
        temp += 1
    
    # _dict sort(정렬) / _dict_sum(합)
    for key1 in _dict:
        _dict[key1].sort(key=lambda x: x[0], reverse=True)
        _dict_sum.append([sum(sub[0] for sub in _dict[key1]), key1])
    _dict_sum.sort(key=lambda x: x[0], reverse=True)
    print(_dict, _dict_sum)
    # answer
    for i, j in _dict_sum:
        for k in range(0, 2):
            try:
                answer.append(_dict[j][k][1])
            except:
                print("Error")
    return answer