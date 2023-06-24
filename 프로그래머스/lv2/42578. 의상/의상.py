# 딕셔너리를 이용한 정리
# [key][values] 
# 옷의 종류를 제공하지 않았으므로 빈 공간으로 생성 후 알맞게 정리하는 작업을 수행할 것임

# 분류 후 계산식은 아래와 같음
# a * b * ...
# 단 상의를 입어도 하의는 생략이 가능하기 때문에 각 원소마다 +1를 해줘야함. 
# (생략) 원소끼리 만나면 안되기 때문에 이에 대한 경우의 수 -1을 원소개수-1개만큼 빼면 됨.

def solution(clothes): # [[이름, 종류] ...]
    dict_clothes = {}
    hap2 = []
    hap = 0
    answer = 1
    for name, categories in clothes:
        hap += 1
        if categories in dict_clothes:
            dict_clothes[categories].append(name)
        else:
            dict_clothes[categories] = [name]
    for values in dict_clothes:
        hap2.append(len(dict_clothes[values])+1)
    print(hap2)
    for i in hap2:
        answer *= i
    return answer - 1