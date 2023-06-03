def solution(nums):
    result = list(set(nums))  # 리스트 중복 제거
    len_result = len(result)  # 중복 제거한 리스트의 원소 개수
    if len_result > len(nums) / 2:  # nums/2 개수보다 중복 제거한 리스트의 개수가 더 크면
        return len(nums) / 2  #  nums/2 개수를 리턴
    else:
        return len_result  # 중복 제거한 리스트의 원소 개수 리턴