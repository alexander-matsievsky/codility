# noinspection PyPep8Naming
def solution(A):
    unpaired = 0
    for a in A:
        unpaired ^= a
    return unpaired


assert solution([9, 3, 9, 3, 9, 7, 9]) == 7
