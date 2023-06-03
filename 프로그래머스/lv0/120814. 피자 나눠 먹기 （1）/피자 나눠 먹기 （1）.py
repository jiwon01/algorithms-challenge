# 1판 당 7조각
# 1인당 1조각
# n명이 주어졌을 때 만들어야하는 최소 피자 개수 구하기
import math
def solution(n):
    return math.ceil(n / 7)  # 인원 수를 피자 개수(7개)로 나눈 뒤, 올림해서 리턴