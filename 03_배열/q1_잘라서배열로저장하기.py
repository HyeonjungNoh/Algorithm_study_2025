def solution(my_str, n):
    answer = []
    str_tmp = ""
    
    for i in my_str:
        str_tmp +=i
        if len(str_tmp) == n:
            answer.append(str_tmp)
            str_tmp = ""
        
    if len(str_tmp) != 0:
        answer.append(str_tmp)
    return answer



my_str = "abc1Addfggg4556b"
n = 6
print(solution(my_str,n))