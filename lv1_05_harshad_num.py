def solution(x):
    answer = True
    divided_x = x
    sum_number = 0
    divided_x, remainder = divmod(divided_x, 10)
    sum_number += remainder
    while divided_x != 0:
        divided_x, remainder = divmod(divided_x, 10)
        sum_number += remainder
    if x % sum_number == 0:
        answer = True
    else:
        answer = False
    return answer


x = 10
print(solution(x))

x = 12
print(solution(x))

x = 11
print(solution(x))

x = 13
print(solution(x))
