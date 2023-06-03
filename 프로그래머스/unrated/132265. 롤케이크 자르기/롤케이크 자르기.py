from collections import Counter

def solution(topping):
    answer = 0
    man = Counter(topping)
    man2 = {}

    for i in range(len(topping)) :
        if topping[i] in man2 :
            man2[topping[i]] += 1
        else :
            man2[topping[i]] = 1
        man[topping[i]] -= 1

        if man[topping[i]] == 0 :
            del man[topping[i]]

        if len(man) == len(man2) :
            answer +=1
    return answer