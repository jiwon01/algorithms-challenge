"""
n개의 컴퓨터가 있고 네트워크가 연결된 여부를 computers 리스트로 제공된다.
n == len(computers)

형성된 네트워크 그룹의 개수를 반환하면 된다.

본 문제는 DFS 알고리즘을 통해 문제를 해결하였다. 마찬가지로 재귀함수가 사용된다.

이미 연결을 확인한 네트워크를 중복확인하지 않도록 길이가 n개인 visited 변수를 만들었다.
n번을 반복하는 for문에 한 번도 확인하지 않은 visited가 0이라면 새로운 네트워크라는 뜻이니 확인을 시작한다.

dfs 함수를 보면 computers[i]를 받고 나서 또다시 이것을 반복을 하면서 하나하나 연결성을 확인한다.
연결성이 있다면 visited에 1을 남겨서 answer에 1를 또 남기지 않도록 한다.
"""

def solution(n, computers):
    answer = 0
    visited = [0] * n
    
    def dfs(sub):
        for idx, value in enumerate(sub):
            if value == 1 and visited[idx] == 0:
                visited[idx] = 1
                dfs(computers[idx])
    
    for i in range(len(computers)):
        if visited[i] == 0:
            visited[i] = 1  # 방문함
            answer += 1  # 네트워크 +1
            dfs(computers[i])
        
    return answer