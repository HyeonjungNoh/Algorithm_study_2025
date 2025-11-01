def solution(survey, choices):
    answer = ''
    # RTCFJMAN
    p_type = {'R': 0,
            'T': 0,
            'C': 0,
            'F': 0,
            'J': 0,
            'M': 0,
            'A': 0,
            'N': 0}

    score = {'1':3, # 매우비동의
            '2':2,
            '3':1,
            '4':0,
            '5':1,
            '6':2,
            '7':3} # 매우 동의
 
    print(p_type)
    for sur, c in zip(survey, choices):
        if c == 1 or c == 2 or c == 3:
            scor_tmp = score[str(c)]
            p_type[sur[0]] += scor_tmp

        elif c == 5 or c == 6 or c == 7:
            scor_tmp = score[str(c)]
            p_type[sur[1]] += scor_tmp

        else:
            continue

    pairs = [('R','T'), ('C','F'), ('J','M'), ('A','N')]

    for a,b in pairs:
        if p_type[a] >= p_type[b]:
            answer += a
        else:
            answer += b
    
        
    return answer

survey = ["AN", "CF", "MJ", "RT", "NA"]	
choices = [5,3,2,7,5]
print(solution(survey,choices))


