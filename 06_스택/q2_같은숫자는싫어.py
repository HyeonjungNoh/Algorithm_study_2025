def solution(arr):
    answer = []
    answer.append(arr[0])
    # arr.reverse()

    for i in range(1, len(arr)):
        if arr[i] == arr[i-1]:
            continue
        else:
            answer.append(arr[i])
    
    return answer

arr = [1,1,3,3,0,1,1]
print(solution(arr))


# def solution(arr):
#     answer = []
#     prev = None
#     for n in arr:
#         if n != prev:
#             answer.append(n)
#         prev = n
#     return answer


# def solution(arr):
#     stack = []

#     for n in arr:
#         if not stack:         # 스택이 비어있다면
#             stack.append(n)
#         elif stack[-1] != n:  # 마지막 값과 다르면 새로 push
#             stack.append(n)
#         # 같으면 아무것도 안 함 (즉, skip)

#     return stack