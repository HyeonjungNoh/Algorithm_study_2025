def solution(i, j, k):
    answer = 0
    
    for i in range(i, j+1):
        answer += str(i).count(str(k))
    return answer


i = 1
j = 13
k = 1
print(solution(i,j,k))