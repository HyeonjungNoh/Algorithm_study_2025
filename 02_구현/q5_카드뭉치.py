def solution(cards1, cards2, goal):
    answer = ''
    i = 0
    j = 0
    for w in goal:
        if i < len(cards1) and cards1[i] == w:
            i += 1
        elif j < len(cards2) and cards2[j] == w:
            j += 1
        else:
            return "No"
    return "Yes"


cards1 = ["i", "drink", "water"]
cards2 = ["want", "to"]
goal = ["i", "want", "to", "drink", "water"]
print(solution(cards1, cards2, goal))