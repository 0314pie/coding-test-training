from collections import deque

def solution(priorities, location):
    queue = deque([(i, p) for i, p in enumerate(priorities)])
    count = 0

    while queue:
        front = queue.popleft()
        if any(front[1] < q[1] for q in queue):
            queue.append(front)
        else:
            count += 1
            if front[0] == location:
                return count