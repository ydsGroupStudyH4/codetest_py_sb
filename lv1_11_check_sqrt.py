import math


def solution(n):
    answer = 0
    sqrt_val = math.sqrt(n)
    if sqrt_val == int(sqrt_val):
        answer = (int(sqrt_val) + 1) * (int(sqrt_val) + 1)
    else:
        answer = -1
    return answer


print(solution(121))
print(solution(3))
print(solution(1))
