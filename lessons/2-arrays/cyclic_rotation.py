# noinspection PyPep8Naming
def solution(A, K):
    if not A:
        return A
    return A[-(K % len(A)):] + A[:-(K % len(A))]


assert solution([3, 8, 9, 7, 6], 1) == [6, 3, 8, 9, 7]
assert solution([3, 8, 9, 7, 6], 3) == [9, 7, 6, 3, 8]
assert solution([-1, -2, -3, -4, -5, -6], 10) == [-3, -4, -5, -6, -1, -2]
