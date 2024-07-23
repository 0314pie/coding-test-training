import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0
    while scoville:
        a = heapq.heappop(scoville)
        if a >= K:
            return cnt
        
        if not scoville:
            return -1
        
        b = heapq.heappop(scoville)
        c = a + 2 * b
        heapq.heappush(scoville, c)
        
        cnt += 1
        
    return -1
        