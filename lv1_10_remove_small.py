def solution(arr):
    answer = []
    arr.remove(min(arr))
    answer = arr
    if len(arr) == 0:
        answer = [-1]
    return answer


arr = [4, 3, 2, 1]
print(solution(arr))

arr = [10]
print(solution(arr))
