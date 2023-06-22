from collections import deque

def solution(s):
    s = deque(s)
    result = deque([])
    
    for i in s:
        if i == "(":
            result.append("(")
        elif result and i == ")":
            result.popleft()
        else:
            return False
        
    if result:
        return False
    else:
        return True