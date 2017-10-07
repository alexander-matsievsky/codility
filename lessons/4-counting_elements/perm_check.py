# noinspection PyPep8Naming
def solution(A):
    counter = len(A)
    freq = [0] * (len(A) + 1)
    for a in A:
        if a > len(A):
            return 0
        counter -= 1
        freq[a] += 1
        if freq[a] > 1:
            return 0
    return int(counter == 0)


assert solution([4, 1, 3, 2]) == 1
assert solution([4, 1, 3]) == 0
