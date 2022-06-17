def solution(N, A):
    counters = [0] * N
    max = 0
    for i in range (0, len(A)):
        v = A[i]
        if v <= N:
            counters[v-1] += 1
            if counters[v-1] > max:
                max = counters[v-1]
        else:
            for j in range(0, len(counters)):
                counters[j] = max
    return counters
