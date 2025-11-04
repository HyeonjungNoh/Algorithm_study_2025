from collections import deque

def solution(priorities, location):
    count = 0

    queue = deque([(p, i) for i, p in enumerate(priorities)])



    while queue:
        prior ,idx = queue.popleft()

        if any(prior < q[0] for q in queue):
            queue.append((prior, idx))
        else:
            count += 1
            if idx == location:
                return count



priorities = [2, 1, 3, 2]
location = 2
print(solution(priorities,location))


# 넘 어렵다...