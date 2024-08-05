def solution(arr):
    cnt = 0
    while True:
        new = []
        for i in range(len(arr)):
            if arr[i] >= 50 and arr[i] % 2 == 0:
                new.append(arr[i] / 2)
            elif arr[i] <= 50 and arr[i] % 2 != 0:
                new.append(arr[i] * 2 + 1)
            else:
                new.append(arr[i])
        if new == arr:
            return cnt
        arr = new
        cnt += 1
        
            