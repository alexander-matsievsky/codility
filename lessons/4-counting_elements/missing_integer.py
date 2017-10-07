# noinspection PyPep8Naming
def solution(A):
    a_min, a_max = float("+inf"), float("-inf")
    counts = dict()
    for a in A:
        a_min, a_max = min(a, a_min), max(a, a_max)
        counts[a] = counts.get(a, 0) + 1
    if a_min > 1 or a_max < 1:
        return 1
    for a in xrange(max(1, a_min), max(1, a_max) + 1):
        if not counts.get(a, 0):
            return a
    return a_max + 1


assert solution([1, 3, 6, 4, 1, 2]) == 5
assert solution([1, 2, 3]) == 4
assert solution([-1, -3]) == 1
