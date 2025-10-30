def solution(array):
    answer = []
    M = max(array)

    for index, value in enumerate(array):
        if value == M:
            answer.append(value)
            answer.append(index)
    return answer



array = [1,8,3]
print(solution(array))