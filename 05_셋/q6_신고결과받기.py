def solution(id_list, report, k):
    answer = []
    report_by = {}

    # to 딕셔너리
    for id in id_list:
        report_by[id] = set()

    # 각 유저별 신고한 유저 정리
    for r in report:
        who, ban_id = r.split()
        report_by[who].add(ban_id)
    

    # 신고당한 횟수 count
    report_count = {u: 0 for u in id_list}
    for rpt in report_by.values():
        for target in rpt:
            report_count[target] += 1

    # 정지한 유저 
    ban_user = set()
    for user, cnt in report_count.items():
        if cnt >= k:
            ban_user.add(user)

    
    # 이메일 전송 count
    for iu in id_list:
        ban_count = 0
        for tu in report_by[iu]:
            if tu in ban_user:
                ban_count += 1
        answer.append(ban_count)
        
         

 
    return answer

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2
print(solution(id_list, report, k))

# return 각 유저별로 처리 결과 메일을 받은 횟수를 담은 배열
