from collections import deque

def solution(prices):
    answer = []
    prices = deque(prices)
    while prices:
        value = prices.popleft()
        answer_ = 0
        for i in prices:
            if value > i:
                answer_ += 1
                break
            else:
                answer_ += 1
        answer.append(answer_)
    return answer
