def solution(food):
    arr = ""
    answer = ""
    for i in range(1, len(food)):
        value = int(food[i]) // 2
        if value == 0: continue
        for j in range(0, value):
            arr += str(i)
    
    arr += "0"
    answer = arr[:]
    
    for v in range(len(arr) - 2, -1, -1): 
        answer += arr[v]
    return answer