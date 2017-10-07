from math import ceil


# noinspection PyPep8Naming
def solution(X, Y, D):
    return int(ceil(float(Y - X) / D))


assert solution(10, 85, 30) == 3
