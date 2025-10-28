def solution(my_string):
    answer = 0
    parts = my_string.split()

    answer = int(parts[0])

    for i in range(1, len(parts),2):
        op = parts[i]

        if op == '+':
            answer += int(parts[i+1])
        else:
            answer -= int(parts[i+1])

    return answer

my_string = "3 + 4"
print(solution(my_string))





# add = my_string.find('+')
#     if add == -1:
#         nums.append(my_string.split(" - "))
#         answer = int(nums[0][0]) - int(nums[0][1])
#     else:
#         nums.append(my_string.split(" + "))
#         answer = int(nums[0][0]) + int(nums[0][1])

