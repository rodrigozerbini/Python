def solution(X, A):
    pos_covered = set()
    for time in range(0, len(A)):
        position = A[time]
        if position not in pos_covered:
            pos_covered.add(position)
            if len(pos_covered) == X:
                break;
    if len(pos_covered) == X:
        return time
    else:
        return -1
