def solution(n):
    answer = []
    number_str = str(n)
    num_str_list = list(number_str)
    num_str_list.reverse()
    answer = list(map(int, num_str_list))
    return answer


print(solution(12345))
