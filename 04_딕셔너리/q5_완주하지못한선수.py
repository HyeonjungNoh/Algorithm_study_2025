from collections import Counter

def solution(participant, completion):
    answer = 0
    par_sort = sorted(participant)
    com_sort = sorted(completion)


    
    p = Counter(par_sort)
    c =  Counter(com_sort)
    no_comple = p-c
    answer = list(no_comple.keys())[0]

    return answer


participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]	
print(solution(participant, completion)) 