def solution(wallpaper):
    answer = []
    file = [] 

    for windex, ss in enumerate(wallpaper):
        for sindex, cc in enumerate(ss):
            if cc == "#":
                file.append((windex,sindex))
            

    lux = min(x for x,y in file)
    luy = min(y for x,y in file)
    rdx = max(x for x,y in file) +1
    rdy = max(y for x,y in file) +1
    
    return [lux, luy, rdx, rdy]




wallpaper = [".#...", "..#..", "...#."]
print(solution(wallpaper))


# 컴퓨터 바탕화면의 상태 -격자판
# 빈칸: .
# 았는 칸: #
# return : 시작점과 끝점을 담은 정수 배열