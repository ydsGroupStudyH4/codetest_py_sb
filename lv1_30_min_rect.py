def solution(sizes):
    answer = 0
    sorted_sizes = [sorted(s) for s in sizes]
    max_x = max([sorted_sizes[i][0] for i in range(0,len(sorted_sizes))])
    max_y = max([sorted_sizes[i][1] for i in range(0,len(sorted_sizes))])
    answer = max_x*max_y
    return answer

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))