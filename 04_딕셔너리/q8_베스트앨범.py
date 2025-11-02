def solution(genres, plays):
    answer = []
    sing_list = []
    album = {}

    # 1. 딕셔너리 만들기
    for index ,sing in enumerate(plays):
        sing_list.append((index,sing))

    # print(sing_list)

    for gener, play in zip(genres,sing_list):
        if gener in album:
            album[gener].append(play)
        else:
            album[gener] = [play]

    # print(album)



    # 2. 장르 정렬을 위한 재생 수 카운팅
    gener_play_count = {}
    for gg, ss in album.items():
        total = sum(s_num for _, s_num in ss)
        gener_play_count[gg] = total

    # print(gener_play_count)

    # 3. 장르 내림차순
    sorted_genres = sorted(gener_play_count, key=gener_play_count.get, reverse=True)

    # print(sorted_genres)


    # 4. 노래 정렬 
    for gg, ss in album.items():
        album[gg] = sorted(ss, key=lambda x: x[1], reverse=True) # 내림차순 정렬
        total = sum(s_num for _, s_num in ss)

    # 5. 상위 2개 추출
    for g in sorted_genres:
        for idx, _ in album[g][:2]:
            answer.append(idx)






    return answer

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
print(solution(genres,plays))






# def solution(clothes):
#     answer = 1

#     cloth_dic = {}

#     for name,kind in clothes:
#         if kind in cloth_dic:
#             cloth_dic[kind].append(name)  
#         else:
#             cloth_dic[kind] = [name] 
    
#     # 총 개수
#     for v in cloth_dic.values():
#         answer *= (len(v) + 1)

#     return answer -1 

