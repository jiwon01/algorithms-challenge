"""
트럭은 1초당 1을 감 (모두 동일)
"""

from collections import deque

def solution(bridge_length, weight, truck_weights):
# 다리 트럭수int, 다리 무게int, 트럭별 무게list
    answer = 0
    trucks = deque(truck_weights)   # 트럭들
    on_bridge = deque([])           # 다리
    remaining_length = deque([])    # 남은 길이?
    
    while trucks or on_bridge:
        answer += 1    # 진행될때마다 1초 증가
        
        ### 다리에 차 땡겨주기 ###
        if on_bridge:  # 다리에 차가 있는가?
            # 다리에 올라간 차들의 남은 길이를 -1
            for i in range(0, len(remaining_length)):
                remaining_length[i] -= 1
            # 다 달린 트럭들 다리에서 빼주기
            if remaining_length[0] == 0:
                on_bridge.popleft()
                remaining_length.popleft()
                    
        ### 차 넣기 ###
        if trucks:
            value = trucks.popleft()
            # 다리가 무게 및 길이에서 여유가 있는가?
            if bridge_length > len(on_bridge) and weight >= sum(on_bridge) + value:
                on_bridge.append(value)
                remaining_length.append(bridge_length)
            else:
                trucks.appendleft(value)
            
    return answer