from collections import deque

def solution(numbers, direction):
    answer = []

    my_queue = deque(numbers)

    if direction == "right":
        my_queue.rotate(1)
    else:
        my_queue.rotate(-1)
    return list(my_queue)
