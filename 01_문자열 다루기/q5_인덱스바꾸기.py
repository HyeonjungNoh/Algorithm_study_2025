def solution(my_string, num1, num2):
    answer = ''

    char_list = list(my_string) 
    n1 = char_list[num1]
    n2 = char_list[num2]

    char_list[num1] = n2
    char_list[num2] = n1
    
    answer = ''.join(char_list)
               
    return answer

my_string = "hello"
num1 = 1
num2 = 2
print(solution(my_string,num1,num2))