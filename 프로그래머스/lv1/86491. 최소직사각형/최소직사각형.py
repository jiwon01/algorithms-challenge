"""
가로 => 세로를 포함할 수 있는 가장 작은 수
세로 => 가로를 포함할 수 있는 가장 작은 수
"""

def solution(sizes):
    w = []
    h = []
    for value in sizes:
        w.append(max(value))
        h.append(min(value))
    return max(h) * max(w)
