def solution(lottos, win_nums):
    answer = []
    win_count = 0
    hidden_count = 0
    rank = {
        "6": 1,
        "5": 2,
        "4": 3,
        "3": 4,
        "2": 5,
        "1": 6,
        "0": 6

    }
    
    for i in lottos:
        if i in win_nums:
             win_count += 1
        elif i == 0:
            hidden_count += 1
        else:
            continue
         

    Max = str(win_count + hidden_count)
    min = str(win_count)
    answer.append(rank[Max])
    answer.append(rank[min])
    return answer

lottos = [44, 1, 0, 0, 31, 25]	
win_nums = [31, 10, 45, 1, 6, 19]
print(solution(lottos,win_nums))