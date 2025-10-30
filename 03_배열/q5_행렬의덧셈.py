def solution(arr1, arr2):
    answer = []
    num_tmp = []
    for a1, a2 in zip(arr1, arr2):
        for aa1, aa2 in zip(a1, a2):
            num_tmp.append(aa1 + aa2)
        answer.append(num_tmp)
        num_tmp = []

            
    return answer

arr1 = [[1,2],[2,3]]
arr2 = [[3,4],[5,6]]

print(solution(arr1,arr2))