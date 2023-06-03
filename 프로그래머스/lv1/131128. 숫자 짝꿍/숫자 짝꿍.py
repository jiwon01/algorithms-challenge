def solution(X, Y):
    answer = ''
    dic_x = {str(n):0 for n in range(10)}
    dic_y = {str(n):0 for n in range(10)}
    
    # X 문자열의 한자리 수 숫자마다 알맞는 0~9범위의 딕셔너리에 저장
    for i in X:
        dic_x[i] += 1
    for i in Y:
        dic_y[i] += 1
        
    # dic_x와 dic_y를 비교하여 더 작은 숫자의 개수를 저장
    for i in range(9, -1, -1):  # 9~0까지 반복 (내림차순으로 반복)
        i = str(i)  # 문자열 형 변환
        num = min(dic_x[i], dic_y[i])
        
        answer = ''.join([answer, i*num]) # i*3 = iii
    
    if answer == '':  # 짝꿍없음 
        return '-1'
    elif len(answer) == answer.count('0'):  # answer의 길이가 0의 개수와 똑같다면 0
        return '0'
    return answer