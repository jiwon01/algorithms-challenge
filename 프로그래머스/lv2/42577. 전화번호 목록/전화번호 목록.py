def solution(phone_book):
    phone_book.sort()
    #print(phone_book)
    for key, value in enumerate(phone_book):
        if key + 1 == len(phone_book):
            continue
        if value == (phone_book[key+1])[:len(value)]:
            return False
    return True

# 이 문제는 for문이 두 번 이루어짐. 너무 비효율적임. 