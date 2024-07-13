def solution(num_list):
    odd = []
    even = []
    for i in num_list:
        if i % 2 == 0:
            even.append(i)
        else :
            odd.append(i)

    odd_list = map(str, odd)
    even_list = map(str, even)
    
    odd_num = int("".join(odd_list))
    even_num = int("".join(even_list))
    
    return odd_num + even_num