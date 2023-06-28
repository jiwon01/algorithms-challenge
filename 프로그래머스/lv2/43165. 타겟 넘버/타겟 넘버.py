"""
DFS(Depth First Search) 알고리즘을 통한 구현

그래프는 + 또는 -로 구성된 자식 트리를 타고 타고 내려가게되어있음. 이걸 DFS로 풀거나 BFS로 풀거나는 니 마음대로임.

재귀를 타고 타서 정답에 도달함. 모든 경우의 수를 찾고 target과 동일하다면 만족하는 것임.
모든 시도를 해보고 정답에 도달한 것들은 answer의 변수를 +1함.
모든 시도가 끝났다면 반복을 종료하고 결과를 반환함.
"""

def dfs(numbers, target, depth, value):
    global answer
    if depth == len(numbers) and target == value:
        answer += 1
    if depth == len(numbers):
        return
    
    dfs(numbers, target, depth + 1, value + numbers[depth])
    dfs(numbers, target, depth + 1, value - numbers[depth])
    return answer

def solution(numbers, target):
    global answer
    answer = 0
    return dfs(numbers, target, 0, 0)