def solution(spell, dic):
    answer = 0
    spell_set  = set(spell)


    for d in dic:
        d_tmp = set(d)
        if set(d) == spell_set:
            return 1

    return 2

spell = ["z", "d", "x"]
dic = 	["def", "dww", "dzx", "loveaw"]
print(solution(spell, dic))
