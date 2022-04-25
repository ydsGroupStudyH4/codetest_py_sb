def solution(n):
    answer = 0
    dc_list = [dc for dc in range(1, n+1) if n%dc == 0]
    answer = sum(dc_list)
    return answer

print(solution(12))