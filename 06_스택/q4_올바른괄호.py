def solution(s):
    answer = True
    stack = []
    

    for i in s:
        if i == '(':
            stack.append(i)

        else:
            if len(stack) == 0 and i == ')':
                return False
        
            else:
                stack.pop()

            
    if len(stack) == 0:
        return True
    else:
        return False



s = "()()"
print(solution(s))