"""
AB 중 부정시 0번, 동의시 1번째 
"""

def solution(survey, choices):
    scores_ = [0 for i in range(0, 8)]
    print(scores_)
    scores = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}
    answer = ""
    
    for i, v in enumerate(survey):
        score = choices[i]
        if 0 < score < 4:  # v[0]
            if score == 1:
                getScore = 3
            elif score == 2:
                getScore = 2
            elif score == 3:
                getScore = 1
            scores[v[0]] += getScore
        elif 4 < score < 8:  # v[1]
            getScore = score - 4
            scores[v[1]] += getScore
    print(scores)
        
    if scores["R"] >= scores["T"]:
        answer += "R"
    else: answer += "T"
    if scores["C"] >= scores["F"]:
        answer += "C"
    else: answer += "F"
    if scores["J"] >= scores["M"]:
        answer += "J"
    else: answer += "M"
    if scores["A"] >= scores["N"]:
        answer += "A"
    else: answer += "N"
    return answer