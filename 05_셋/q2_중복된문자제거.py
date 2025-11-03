def solution(my_string):
    answer = ''
    for c in my_string:
        if c not in answer:
            answer += c
        else:
            continue
    return answer

my_string = "people"
print(solution(my_string))