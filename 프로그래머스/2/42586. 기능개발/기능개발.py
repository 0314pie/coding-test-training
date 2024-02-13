def solution(progresses, speeds):
    days = 0
    result = []
    while progresses:
        # 모든 작업에 대해 1일씩 경과시킴
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        
        # 완료된 작업 처리
        while progresses and progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            days += 1
        
        # 완료된 작업이 있을 때 결과에 추가
        if days > 0:
            result.append(days)
            days = 0
            
    return result