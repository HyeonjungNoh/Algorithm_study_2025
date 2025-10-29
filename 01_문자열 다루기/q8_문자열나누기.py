def solution(s):
    answer = 0
    first = None
    same_c = 0
    diff_c= 0


    for c in s:
        if first is None:
            first = c

        if c == first:
            same_c += 1
        else:
            diff_c += 1
        
        if same_c == diff_c:
            answer += 1
            first = None
            same_c = 0
            diff_c = 0
        
    if first is not None:
        answer += 1
    return answer

s = "banana"
print(solution(s))