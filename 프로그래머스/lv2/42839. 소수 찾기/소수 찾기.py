from itertools import permutations

def prime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = []
    nums = []
    nums2 = []
    
    for i in range(1, len(numbers) + 1):
        nums.append(list(map(''.join, permutations(numbers, i))))
    for i in nums:
        for j in i:
            nums2.append(j)
    for i in nums2:
        value = int(i)
        if prime(value):
            print(value)
            if not value in answer:
                answer.append(value)
        
    
    return len(answer)