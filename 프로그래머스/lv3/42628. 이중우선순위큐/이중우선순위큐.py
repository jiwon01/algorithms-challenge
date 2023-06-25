import heapq

def solution(operations):
    heap = []  # 큐가 비는지 확인용
    
    while operations:
        task = operations.pop(0)
        # I와 D 구분
        if task[0] == "I":  # I (삽입)
            value = int(task[2:])
            heapq.heappush(heap, value)
        else:
            if heap:
                # D 1과 -1 구분
                if task[2] == "1":  # D1 (최댓값 (음수))
                    get_max = max(heap)
                    heap.remove(get_max)
                else:               # D-1 (최솟값)
                    heapq.heappop(heap)
    if len(heap) == 0:
        return [0, 0]
    else:
        max_value = max(heap)
        min_value = heapq.heappop(heap)
    return [max_value, min_value]