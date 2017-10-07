# noinspection PyPep8Naming
def solution(X, A):
    T_fall = [None] * (X + 1)
    for t, x in enumerate(A):
        T_fall[x] = min(t, T_fall[x] or t)
    t_max = None
    for t in T_fall[1:]:
        if t is None:
            return -1
        t_max = max(t, t_max)
    return t_max


assert solution(5, [1, 3, 1, 4, 2, 3, 5, 4]) == 6
