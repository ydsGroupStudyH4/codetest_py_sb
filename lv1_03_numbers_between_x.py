def solution(x, n):
    answer = []
    answer = [i * x + x for i in range(n)]
    return answer


print(solution(2, 5))
