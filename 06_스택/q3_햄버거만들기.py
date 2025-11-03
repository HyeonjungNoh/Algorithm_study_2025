def solution(ingredient):
    answer = 0
    stack = []
    
    for i in ingredient:
        stack.append(i)
        if len(stack) >= 4 and stack[-4:] == [1,2,3,1]:
            for _ in range(4):
                stack.pop()
            answer +=1
        
    return answer





ingredient = [2, 1, 1, 2, 3, 1, 2, 3, 1]
print(solution(ingredient))