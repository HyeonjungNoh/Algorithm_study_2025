def solution(num_list, n):
    answer = []
    answer_tmp = []

    for i in range(len(num_list)):
        answer_tmp.append(num_list[i])

        
        if len(answer_tmp) == n:
            answer.append(answer_tmp)
            answer_tmp = []
    return answer



num_list = [1, 2, 3, 4, 5, 6, 7, 8]
n = 2
print(solution(num_list,n))