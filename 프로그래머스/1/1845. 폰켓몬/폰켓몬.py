def solution(nums):
    nums.sort()
    list = []
    lim = int(len(nums)/2)
    list.append(nums[0])
    for num in range(len(nums)-1):
        if nums[num + 1] not in list:
            list.append(nums[num+1])
        else: continue
    return len(list[:lim])