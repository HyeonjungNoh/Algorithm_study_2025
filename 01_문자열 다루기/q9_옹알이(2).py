def solution(babbling):
    answer = 0
 

    for word in babbling:
        for w in ["aya", "ye", "woo", "ma"]:
            if w*2 in word:
                word = "X"
                break

        if word == "X":
            continue

        for w in ["aya", "ye", "woo", "ma"]:
            word = word.replace(w, " ")

        if word.strip() == "":
            answer += 1
        
    return answer



babbling = ["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]
print(solution(babbling))