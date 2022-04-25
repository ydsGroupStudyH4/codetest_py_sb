def solution(n):
    answer = 0
    # for i in range(2,n+1):
    #     for j in range(2,i+1):
    #         if i%j == 0 and i != j:
    #             break
    #         elif i%j == 0 and i == j:
    #             answer += 1

    num = set(range(2, n + 1))
    for i in range(2, n + 1):
        if i in num:
            num -= set(range(2 * i, n + 1, i))
    return len(num)

    # num_list = range(2, n + 1)
    # prime_num_list = []
    # index = 0
    # while index < len(num_list):
    #     sqrt_num = math.sqrt(num_list[index])
    #     checker = True
    #     j = 0
    #     if num_list[index] == 2 or num_list[index] == 3:
    #         prime_num_list.append(num_list[index])
    #         index += 1
    #         continue
    #     while prime_num_list[j] <= sqrt_num:
    #         if num_list[index] % prime_num_list[j] == 0:
    #             checker = False
    #             break
    #         j += 1
    #     if checker == True:
    #         prime_num_list.append(num_list[index])
    #     index += 1
    # answer = len(prime_num_list)
    # return answer

    # # for i in range(2, n + 1):
    #     sqrt_num = math.sqrt(i)
    #     div_num = 2
    #     checker = True
    #     while div_num <= sqrt_num:
    #         if i % div_num == 0:
    #             checker = False
    #             break
    #         div_num += 1
    #     if checker == True:
    #         answer += 1
    # return answer


print(solution(2))
print(solution(3))
print(solution(10))
print(solution(5))
