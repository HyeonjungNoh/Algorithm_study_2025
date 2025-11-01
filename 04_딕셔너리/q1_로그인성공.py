def solution(id_pw, db):

    for id, pw in db:
        if id == id_pw[0] and pw == id_pw[1]:
            return 'login'
        elif id == id_pw[0] and pw != id_pw[1]:
            return 'wrong pw'
    return 'fail'
 
id_pw = ["rabbit04", "98761"]
db = [["jaja11", "98761"], ["krong0313", "29440"], ["rabbit00", "111333"]]
print(solution(id_pw,db))