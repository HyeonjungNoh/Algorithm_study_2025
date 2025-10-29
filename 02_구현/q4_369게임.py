def solution(order):
    answer = 0
    list_369 = ['3','6', '9']

    
    for i in str(order):
        if i == '3' or i == '6' or i == '9':
            answer += 1
    return answer

order = 29423
print(solution(order))