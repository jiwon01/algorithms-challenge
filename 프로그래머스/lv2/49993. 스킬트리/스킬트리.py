"""
순서대로 배워야하는 문자열 skill이 제공되고,
내가 배울 스킬트리의 여러개의 순서가 스킬트리로 제공이 될 때, 학습이 가능한 순서의 개수를 리턴하는 문제

skill_trees로 for문을 돌려 유효성을 확인,
  1. 
"""


def solution(skill, skill_trees):
    answer = 0
    skill = "1" + skill  # "1"을 붙여서 맨 처음임을 알도록함.
    #print(skill)
    for v_trees in skill_trees:
        result = 1
        used = "1"   # 만약 현재 처리하는 스킬이 skills를 요한다면 이전에 학습해야만하는 것을 했는지 확인하기 위해.
        for v in v_trees:
            if v in skill: # 만약 현재 처리하는 스킬이 순차 학습을 필요로 하는가?
                get_idx = skill.index(v)
                if used == skill[get_idx - 1]:  # 일치하므로 used를 v로 갱신
                    used = v
                else:  # 일치하지 않음 = 조건미충족으로 result를 -1로 수정 후 break
                    result = -1
                    break
        if result == 1:
            answer += 1
    return answer