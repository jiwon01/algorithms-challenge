def solution(phone_book):
    phone_book.sort()
    #print(phone_book)
    for key, value in enumerate(phone_book):
        if key + 1 == len(phone_book):
            break
        elif value == (phone_book[key+1])[:len(value)]:
            return False
    return True

# 정렬 후 내 뒤에 있는 원소의 앞 글자와 비교. 동일하면 즉시 False return함.