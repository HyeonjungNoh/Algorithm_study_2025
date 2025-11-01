def solution(s):
    answer = []
    close_char = {}

    for i in range(len(s)):
        if s[i] not in close_char:
            close_char[s[i]] = -1
            answer.append(close_char[s[i]])
            close_char[s[i]] = i
        else:
            answer.append(i - close_char[s[i]])
            close_char[s[i]] = i
 
 
 
    return answer

s = 'banana'
print(solution(s))