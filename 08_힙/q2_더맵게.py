import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville) # 리스트 to 힙

    
    while scoville and scoville[0] < K:
        if len(scoville) < 2:
            return -1
        min_1 = heapq.heappop(scoville)
        min_2 = heapq.heappop(scoville)
        mix = min_1 + (min_2 * 2)
        
        heapq.heappush(scoville,mix)
        answer+=1
 

    return answer