from collections import deque

def check_diff(a, b):
    diff = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            diff += 1
    if diff == 1: return True
    return False

def BFS(begin, target, words):
    queue = deque([(begin, 0)])
    print(queue)
    while queue:
        value, depth = queue.popleft()
        
        for nv in words:
            if check_diff(value, nv):
                if nv == target:
                    return depth + 1
                else:
                    queue.append((nv, depth + 1))
    return 0
        

def solution(begin, target, words):
    if target not in words:
        return 0
    return BFS(begin, target, words)