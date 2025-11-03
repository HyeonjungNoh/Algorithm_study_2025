from collections import Counter

def solution(array):
    answer = 0
    s = Counter(array)
    max_c = max(s.values()) 


    mode_list = [k for k,v in s.items() if v == max_c]
    
    if len(mode_list) > 1:
        return -1
    else:
        return mode_list[0]

    return answer

array = [1, 1, 2, 2]
print(solution(array))