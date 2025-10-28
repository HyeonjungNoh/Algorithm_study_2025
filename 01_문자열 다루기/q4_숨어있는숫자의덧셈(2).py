import re

def solution(my_string):
    answer = 0
    numbers = re.findall(r'\d+', my_string)
    
    int_numbers = list(map(int, numbers))
    answer = sum(int_numbers)
    return answer


my_string = "aAb1B2cC34oOp"
print(solution(my_string))