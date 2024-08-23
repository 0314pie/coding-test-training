def solution(price, money, count):
    total_cost = sum(price * i for i in range(1, count + 1))
    
    if money < total_cost:
        return total_cost - money
    else:
        return 0