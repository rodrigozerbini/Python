#  If the array is sorted,
#  A[i+2] + A[i+1] > A[i] is always true and
#  A[i+2] + A[i] > A[i+1] is always true.
#  So, I just need to check if
#  A[i+1] + A[i] > A[i+2].
#  Since in case of A[i] + A[i + 1] > MAXINT the code 
#  would strike an overflow (the result would be greater
#  than allowed integer limit), we´ll modify the formula
#  to an equivalent A[i] > A[i+2] - A[i+1]

def solution(A):
    A  = sorted(A)
    for i in range(0, len(A)-2):
        if (A[i] > A[i+2] - A[i+1]):
            return 1
    return 0
