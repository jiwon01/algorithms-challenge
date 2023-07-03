"""
전형적인 BFS 해결 문제
상하좌우를 모두 움직여서 탐색해야하고,
딕셔너리를 통하여 현재 좌표는 몇 번 움직였는지를 계산하여 저장함.
따라서 정답을 리턴할 땐 좌표 딕셔너리 값에 +1을 리턴하면 됨.

출발 위치: (0, 0)
max_x = len(maps[0])
max_y = len(maps)
도착 위치: [max_x - 1, max_y - 1]
"""
from collections import deque

def solution(maps):
    answer = bfs(maps, 0, 0)
    return answer

def bfs(maps, x, y):
    max_x = len(maps)
    max_y = len(maps[0])
    queue = deque([[x, y]])
    visited = [[0 for _ in range(max_y)] for _ in range(max_x)]
    dist = {(x, y): 1}
    # 상, 하, 좌, 우
    m_x = [0, 0, -1, 1]
    m_y = [-1, 1, 0, 0]
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            mvd_x = x + m_x[i]
            mvd_y = y + m_y[i]
            # 아래 조건을 모두 만족
            # 0 <= mvd_x < max_x + 0 <= mvd_y < max_y + [mvd_x, mvd_y] not in visited + maps[mvd_x][mvd_y] 
            # 리스트 내인가? and 리스느내인가? and 방문했는가? and 벽이 아닌가?
            if 0 <= mvd_x < max_x and 0 <= mvd_y < max_y and visited[mvd_x][mvd_y] == 0 and maps[mvd_x][mvd_y]:
                # 여기가 마지막..?
                if mvd_x == max_x -1 and mvd_y == max_y -1: return dist[(x, y)] + 1
                # 큐 넣고 visited에도 넣음, dist에도 +1
                queue.append([mvd_x, mvd_y])
                visited[mvd_x][mvd_y] = 1
                dist[(mvd_x, mvd_y)] = dist[(x, y)] + 1
    return -1