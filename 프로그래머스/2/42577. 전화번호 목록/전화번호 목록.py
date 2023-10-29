def solution(phone_book):
    phone_book.sort()
    for idx, num in enumerate(phone_book[:-1]):
        if num == phone_book[idx+1][:len(num)]:
            return False
    return True