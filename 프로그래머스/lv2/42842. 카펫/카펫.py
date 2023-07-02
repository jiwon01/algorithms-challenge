def solution(brown, yellow):
    total = brown + yellow
    
    for x in range(1, total + 1):
        if total % x == 0:
            y = total / x
            
            if x >= y and brown == (x + y) * 2 - 4:  # brown의 테두리
                return [x, y]