def isvaild(array, n):
    for i in array:
        if i % n == 0:
            return 0
    return 1

def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a%b)

def solution(arrayA, arrayB):
    answer = 0
    gcdA = arrayA[0]
    gcdB = arrayB[0]
    
    # 최대공약수 구하기.
    for i in range(1, len(arrayA)):
        gcdA = gcd(gcdA, arrayA[i])
    for i in range(1, len(arrayB)):
        gcdB = gcd(gcdB, arrayB[i])
        
    # 서로의 배열를 나눌 수 있는지 확인
    if isvaild(arrayB, gcdA):  # B 배열에 A 최대공약수 넣어보기
        answer = gcdA  # 정답 변수에 A 최대공약수 입력
    if isvaild(arrayA, gcdB):  # A 배열에 B 최대공약수 넣어보기
        if answer < gcdB:  # 기 입력된 A 최대공약수보다 크다면
            answer = gcdB  # B 최대공약수 입력
    
    return answer