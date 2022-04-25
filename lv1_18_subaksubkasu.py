def solution(n):
    answer = ''
    temp = ['수' if i%2 == 0 else '박' for i in range(n)]
    answer = "".join(temp)
    # for i in range(n):
    #     if i % 2 == 0:
    #         answer += '수'
    #     else:
    #         answer += '박'
    return answer

print(solution(4))