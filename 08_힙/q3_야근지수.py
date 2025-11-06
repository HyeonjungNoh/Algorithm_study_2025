import heapq
def solution(n, works):
    minus_heap = []
    plus_heap = []
    answer = 0

    for w in works:
        tmp = (-w)
        minus_heap.append(tmp)
    
    heapq.heapify(minus_heap) # 리스트 to 힙
    # print(minus_heap) 

    for _ in range(n):
        c = heapq.heappop(minus_heap)
        c += 1
        heapq.heappush(minus_heap, c)
        # print(n)
    

    print(minus_heap)

    for m in minus_heap:
        m = -(m)
        plus_heap.append(m)
    
    # print(plus_heap)

    for p in plus_heap:
        answer += (p **2)
    
    return answer

works = [4,3,3]
n = 4
print(solution(n,works))