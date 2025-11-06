def solution(n):
    answer = []
    for i in str(n):
        answer.append(i)
    
    
    
    answer.reverse()
    return list(map(int, answer))
n = 12345
print(solution(n))