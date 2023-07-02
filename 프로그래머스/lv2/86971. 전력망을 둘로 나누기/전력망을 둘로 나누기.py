"""
BFS 알고리즘 해석
colletions 라이브러리 사용... deque 함수를 이용해 queue 구성.
"""


from collections import deque

def BFS(graph, start):
    visited = [start]
    queue = deque([start])
    result = 0
    
    while queue:
        x = queue.popleft()
        
        for v in graph[x]:
            if not v in visited:
                queue.append(v)
                visited.append(v)
                result += 1
    
    return result

def solution(n, wires):
    answer = n
    dict_ = {}
    
    # dict_
    for idx in range(1, n + 1):
        dict_[idx] = []
    
    # make a host info
    for n1, n2 in wires:
        dict_[n1].append(n2)
        dict_[n2].append(n1)
        
    # run with BFS
    for n1, n2 in wires:
        # 선 끊기
        dict_[n1].remove(n2)
        dict_[n2].remove(n1)
        
        answer = min(abs(BFS(dict_, n1) - BFS(dict_, n2)), answer)
        
        dict_[n1].append(n2)
        dict_[n2].append(n1)
        
    return answer

