def solution(a, b):
    answer = 0
    if a > b:
        a, b = b, a
    answer = sum(list(range(a, b + 1)))
    return answer


print(solution(3, 5))
print(solution(5, 3))
