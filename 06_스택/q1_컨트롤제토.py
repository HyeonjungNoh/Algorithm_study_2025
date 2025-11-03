def solution(s):
    answer = 0
    
    str_c = s.split(" ")
    for _ in range(len(str_c)):

        if not str_c:
            break

        num = str_c.pop()
        if num == 'Z':
            str_c.pop()
        else:
            answer += int(num)

    return answer


s = "1 2 Z 3"
print(solution(s))