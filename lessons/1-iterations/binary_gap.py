# noinspection PyPep8Naming
def solution(N):
    max_gap = 0
    zeros = 0
    while not N & 1:
        N = N >> 1
    while N > 0:
        if N & 1:
            max_gap = max(max_gap, zeros)
            zeros = 0
        else:
            zeros += 1
        N = N >> 1
    return max_gap


assert solution(9) == 2
assert solution(529) == 4
assert solution(20) == 1
assert solution(15) == 0
assert solution(1041) == 5
