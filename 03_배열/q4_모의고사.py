

def solution(answers):
    answer = [0, 0, 0]
    result = []
    
    
    arr1 = [1, 2, 3, 4, 5] * 10000
    arr2 = [2, 1, 2, 3, 2, 4, 2, 5] * 10000
    arr3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 10000

    
    
    arr1 = arr1[:len(answers)]
    arr2 = arr2[:len(answers)]
    arr3 = arr3[:len(answers)]



    for ar1, ar2, ar3, ans in zip(arr1,arr2,arr3,answers):
        if ar1 == ans:
            answer[0] += 1
        if ar2 == ans:
            answer[1] += 1
        if ar3 == ans:
            answer[2] += 1

  
    
    max_score = max(answer)
    for i, v in enumerate(answer):
        if v == max_score:
            result.append(i+1)


    return result

answers = [1,3,2,4,2]
print(solution(answers))
