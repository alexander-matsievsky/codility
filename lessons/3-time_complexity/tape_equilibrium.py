# noinspection PyPep8Naming
def solution(A):
    S = A[:1] + [0] * (len(A) - 1)
    for i in xrange(1, len(A)):
        S[i] = S[i - 1] + A[i]
    min_diff = abs(S[-1] - S[0] - S[0])
    for P in xrange(2, len(S)):
        min_diff = min(min_diff, abs(S[-1] - S[P - 1] - S[P - 1]))
    return min_diff


assert solution([3, 1, 2, 4, 3]) == 1
assert solution([1, 1]) == 0
