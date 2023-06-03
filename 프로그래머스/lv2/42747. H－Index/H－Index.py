def solution(citations):
    answer = 0
    for h in range(1, len(citations) + 1):
        count = 0
        for val in citations:
            if val >= h:  # 원소가 h 이상인가?
                count += 1
        if count < h:  # 원소가 h보다 적은가? 적으면 Fail
            print("Done!")
            return h-1
        answer = h
    return answer