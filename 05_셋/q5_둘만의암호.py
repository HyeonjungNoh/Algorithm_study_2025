def solution(s, skip, index):
    answer = []
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    skip_set = set(skip)

    for c in s:
        pos = alphabet.index(c) # 시작 인덱스
        move = 0 
        while move < index:
            pos = (pos + 1) % 26
            if alphabet[pos] in skip:
                continue
            move +=1

        answer.append(alphabet[pos])
    return ''.join(answer)

s = "aukks"	
skip = "wbqd"
index = 5
print(solution(s,skip, index))