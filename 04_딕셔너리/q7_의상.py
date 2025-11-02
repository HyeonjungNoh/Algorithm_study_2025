def solution(clothes):
    answer = 1
    cloth_dic = {}

    for name,kind in clothes:
        if kind in cloth_dic:
            cloth_dic[kind].append(name)  
        else:
            cloth_dic[kind] = [name] 
    
    # 총 개수
    for v in cloth_dic.values():
        answer *= (len(v) + 1)

    return answer -1 



clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))
