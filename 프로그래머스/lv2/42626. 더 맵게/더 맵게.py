"""
섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
K 이상이 될 때까지 계속 섞음

최소횟수를 구하는 것이니,, 최소힙을 쓰면되나?
자동으로 최소값이 위로 정렬이되니까. 0번째 두 번 뽑아서 연산시키면되겟네,, 그리고 다시 넣고
이건 큐로도 다시 할 수 있으려나

(본 문제는 큐로도 해결할 수 있지만 힙 방식을 쓰는게 복잡도상 제일 나음)

heapq.heappush(h, value)  # 원소 삽입
heapq.heappop(h)  # 원소 제거
"""

from heapq import heappush, heappop, heapify

def solution(scoville, K):
    low = 0
    answer = 0
    heapify(scoville)  # heap 자료구조로
    while scoville[0] < K:  # low가 더 작으면(true) 돌아감
        if len(scoville) == 1:  # 하나 남았는데 
            return -1
        val_1 = heappop(scoville) # 최소값 1 추출
        val_2 = heappop(scoville) # 최소값 2 추출 이게 더 큼
        result = val_1 + (val_2 * 2)
        heappush(scoville, result)
        answer += 1

    return answer