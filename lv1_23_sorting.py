def solution(strings, n):
    answer = []
    answer = sorted(strings, key=lambda k: (k[n], k))
    # i = 0
    # for i in range(0, len(strings)):
    #     min = strings[i]
    #     if i == len(strings) - 1:
    #         answer.append(strings[i])
    #         break
    #     for j in range(i + 1, len(strings)):
    #         if min[n] == strings[j][n]:
    #             if min > strings[j]:
    #                 min, strings[j] = strings[j], min
    #         elif min[n] > strings[j][n]:
    #             min, strings[j] = strings[j], min
    #     answer.append(min)
    return answer


print(solution(["abce", "abcd", "cdx"], 2))
print(solution(["sun", "bed", "car"], 1))
