def solution(s):
    numtoalpah = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}
    # 하나 문자
    for i in range(0, 10):
        s = s.replace(numtoalpah[i], str(i))
    return int(s)