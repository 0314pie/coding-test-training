import math

def solution(n, m):
    a = math.gcd(n, m)
    b = abs(n * m) // a
    return [a, b]