def solution(array):
    answer = 0 
    word = ''
    for i in array:
        word += str(i)

    for i in word:
        if i == '7':
            answer += 1

    return answer

array = [7, 77, 17]
print(solution(array))