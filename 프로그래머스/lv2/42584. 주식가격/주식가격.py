"""
prices popleft()하여 확보한 값을 v라고 하고, result를 1이라고 하면,
prices for로 반복하여 값이 같거나 크면 result + 1를, 작아지면 그냥 result 값을 answer에 append함.


"""
from collections import deque

def solution(price):
    answer = []
    price = deque(price)
    
    while price:
        v = price.popleft()
        result = 0
        
        for vv in price:
            if v <= vv:
                result += 1
            else:
                result += 1
                break
        
        answer.append(result)
    return answer

















"""
이전 풀이

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
"""