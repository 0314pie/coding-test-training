def solution(arr):
    i = 0
    stk = []
    while i < len(arr):
        if not stk:
            stk.append(arr[i])
        elif stk and stk[-1] == arr[i]:
            del stk[-1]
        elif stk and stk[-1] != arr[i]:
            stk.append(arr[i])
        i += 1
    if not stk:
        return [-1]
    return stk