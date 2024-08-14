def solution(order):
    result = 0
    for i in order:
        if 'americano' in i:
            result += 4500
        if 'latte' in i:
            result += 5000
        if i == 'anything':
            result += 4500
    return result