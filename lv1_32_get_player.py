def solution(participant, completion):
    answer = ""
    # participant.sort()
    # completion.sort()
    # completion.append("0")

    dic = {}
    temp = 0
    for p in participant:
        dic[hash(p)] = p
        temp += int(hash(p))

    # for i in range(0, len(participant)):
    #     if participant[i] != completion[i]:
    #         answer = participant[i]
    #         break

    # for p in participant:
    #     if p in completion:
    #         if participant.count(p) != completion.count(p):
    #             answer = p
    #             break
    #     else:
    #         answer = p
    #         break

    return answer


print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))
