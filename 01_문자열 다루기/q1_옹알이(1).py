def solution(babbling):
    answer = 0

    for i in babbling:
        tj = ""
        for  j in i:
            tj += j
            if tj in [ "aya", "ye", "woo", "ma"]:
                tj = ""
                
        if len(tj) == 0:
            answer += 1
    return answer


babbling = ["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]
print(solution(babbling))