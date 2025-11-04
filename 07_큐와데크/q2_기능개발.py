import math

def solution(progresses, speeds):
    answer = []
    remain_day = []



    for p, s in zip(progresses, speeds):
        day_count= math.ceil((100 - p) / s)
        remain_day.append(day_count)

    Current = remain_day[0]
    count = 1
    for day in remain_day[1:]:
        if day <= Current:
            count += 1
        else:
            answer.append(count)
            count = 1
            Current = day
    answer.append(count)

    return answer

progresses = [93, 30, 55]
speeds = [1,30,5]
print(solution(progresses, speeds))