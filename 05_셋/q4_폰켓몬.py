def solution(nums):
    answer = 0
    
    unique_p = len(set(nums))
    take_p = len(nums) // 2

    answer = min(unique_p, take_p)

    return answer


nums = [3,1,2,3]
print(solution(nums))

# return 폰켓몬 종류 번호의 개수