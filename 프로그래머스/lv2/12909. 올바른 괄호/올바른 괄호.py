"""
popleft를 두 번 해서 만약 ()가 나오는 경우에는 그냥 그대로 날려버리면 됨.

만약 ((처럼 (가 연속으로 나오는 경우 하나를 sub_s에 보관하도록 함.
다음에 일단 (하나는 다시 appendleft해서 다시 넣어줌.

)가 나온 경우 sub_s에 (가 보관되어있는지 확인해봄. 없다면 false를 반환하고 있다면 둘 다 그대로 날리면 됨.
"""

from collections import deque

def solution(s):
    # s를 deque함. [] 리스트가 담긴 deque를 result로 정의
    s = deque(s)
    sub_s = deque([])
    
    while s:
        x = s.popleft()
        #print(s, sub_s)
        
        if x == "(":
            if s:  # s가 유효한가? 뽑은게 마지막이면 return False
                x2 = s.popleft()
                if x2 == ")": 
                    continue # 일치하기 때문에 그대로 ㄱㄱ
                elif x2 == "(":
                    s.appendleft(x)
                    sub_s.append(x2)
            else: return False
        else:   # x == ")"
            if sub_s:  # sub_s가 유효한가?
                sub_s.popleft()
            else: return False
    if sub_s: return False
    return True  # 모두 일치하여 사라져서 while이 끝났기 때문에 return True 반환