def solution(answers):
    answer = []
    samples = [1,2,3,4,5]
    samples2 = [2,1,2,3,2,4,2,5]
    samples3 = [3,3,1,1,2,2,4,4,5,5]
    # t1 = samples*(len(answers)//5) + samples[0:len(answers)%5]
    # t2 = [2 if i%2==0 else samples2[(i)%8] for i in range(len(answers))]
    # t3 = [samples3[i%10] for i in range(len(answers))]

    scores = [0, 0, 0]
    # dic_scores = {k:v for k,v in enumerate(scores)}
    # for i in range(len(answers)):
    #     if answers[i]==t1[i]:
    #         scores[0] += 1
    #     if answers[i]==t2[i]:
    #         scores[1] += 1
    #     if answers[i]==t3[i]:
    #         scores[2] += 1
    # scores.sort(reverse=True)
    # dic_scores = sorted(dic_scores.items(), key=lambda v:v[1], reverse=True)
    # max_score = 0
    # for k, v in dic_scores:
    #     if v >= max_score:
    #         answer.append(k+1)
    #         max_score = v
    #     else:
    #         break
    
    for i in range(len(answers)):
        if answers[i]==samples[i%len(samples)]:
            scores[0] += 1
        if answers[i]==samples2[i%len(samples2)]:
            scores[1] += 1
        if answers[i]==samples3[i%len(samples3)]:
            scores[2] += 1
    for idx, score in enumerate(scores):
        if score == max(scores):
            answer.append(idx+1)
        else:
            break

    return answer

print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))