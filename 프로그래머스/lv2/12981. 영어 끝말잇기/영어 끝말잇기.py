"""
n = 몇 명인가?

이미 말한 단어를 또 말하는 사람이 지는데 게임에서 진 사람의 번호와 자신이 몇 번째에 말한게 탈락한 건지를 리턴하면 됨.
이미 말했던 단어를 저장하는 used 리스트를 만들어서 하면 될 듯

이 문제는 몇 번째의 사람인지, 자신이 말 한 것 중에서 몇 번째의 탈락한 것인지를 어떻게 알아내는게 포인트인 문제
"""

def solution(n, words):
    used = []  # 사용한 단어를 저장
    cnt = 0  # 몇 번째 사람인지
    cnt_arr = [0 for i in range(n)]  # n 번째 사람이 외친 횟수
    
    for i, w in enumerate(words):
        if cnt >= n: # 몇 번째 사람이죠? 한 번 돌았으면 0으로 재정의
            cnt = 0
        cnt += 1  # 다음 사람으로
        cnt_arr[cnt - 1] += 1  # n번째 사람이 외친 횟수 +1
        
        if used: # 두 번째부터 실행됨.
            used_word = used[-1]
            if w in used or used_word[-1] != w[0]:  # 탈락 조건 성립쓰
                answer = [cnt, cnt_arr[cnt - 1]]
                print("RETURN: ", answer)
                return answer
        
        used.append(w) # 사용한 단어 used에 이어붙임
            
    print("Everyone successed")
    return [0, 0]