def solution(phone_book):
 
    phone_book_sort = sorted(phone_book)

    fp = phone_book_sort[0]
    for i in range(len(phone_book_sort)-1):
        if phone_book_sort[i+1].startswith(phone_book_sort[i]):
            return False
    return True 
        


phone_book = ["119", "97674223", "1195524421"]
print(solution(phone_book))