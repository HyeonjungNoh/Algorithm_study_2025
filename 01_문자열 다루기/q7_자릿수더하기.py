def solution(n):
    answer = 0
    n_list = list(str(n))

    n_list_int = list(map(int, n_list))
    answer = sum(n_list_int)
    return answer

n = 1234
print(solution(n))