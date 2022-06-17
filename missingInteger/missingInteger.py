def solution(A):
    smallest = 1
    numbers = set()
    for i in range(0, len(A)):
        numbers.add(A[i])
        if A[i] == smallest:
            while (smallest in numbers):
                smallest += 1
    return smallest
