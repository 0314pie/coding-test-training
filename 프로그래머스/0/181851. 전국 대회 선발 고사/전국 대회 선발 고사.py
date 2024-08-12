def solution(rank, attendance):
    present = []
    for i in range(len(rank)):
        if attendance[i]:
            present.append((rank[i],i))
            
    present.sort()
    
    a = present[0][1]
    b = present[1][1]
    c = present[2][1]

    return 10000 * a + 100 * b + c



