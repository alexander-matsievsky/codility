# noinspection PyPep8Naming
def solution(A):
    return (len(A) + 1) * (len(A) + 2) / 2 - sum(A)


assert solution([2, 3, 1, 5]) == 4
assert solution([1]) == 2
