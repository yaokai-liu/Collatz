
from NumberTheoryTools import *

def A_B_derivation(A, B):
    cal_A = 1
    cal_B = alpha ** sum(B[:-1])
    frak_U = 0
    for i in range (0, len(A)):
        frak_U += cal_A * cal_B
        cal_A *= alpha**(A[i])
        cal_B //= alpha**(B[i])
    return frak_U

alpha, beta, gamma = 5, 2, 1

MAX_ZERO_COUNT = ord(beta * (alpha - 1), alpha)


def generate_splits_ordered(total_sum, slice_count, max_zero_count):
    results = []

    def backtrack(current_path, remain_sum, zero_count):
        if len(current_path) == slice_count:
            if remain_sum == 0: results.append(list(current_path))
            return
        if remain_sum < 0:
            return
        for i in range(0, remain_sum + 1):
            next_zero_count = zero_count + 1 if i == 0 else 0
            if next_zero_count > max_zero_count:
                continue
            current_path.append(i)
            backtrack(current_path, remain_sum - i, next_zero_count)
            current_path.pop()

    backtrack([], total_sum, 0)
    return results

def total_segments(total_sum, max_zero_count):
    segments = []
    slice_count = 1
    while True:
        new_segments = generate_splits_ordered(5, slice_count, max_zero_count)
        if len(new_segments) == 0:
            break
        segments += new_segments
        slice_count += 1
    return segments

def solve_pow_dif(m, n, c):
    """
    solve equation beta^m - alpha^n = c
    """
    derivations = []
    slice_count = 1
    while True:
        segmentsA = generate_splits_ordered(m, slice_count, 1)
        segmentsB = generate_splits_ordered(n, slice_count, 1)
        if len(segmentsA) == 0 or len(segmentsB) == 0: break
        for A in segmentsA:
            for B in segmentsB:
                for k in range(0, len(A)):
                    if A[k] == 0 and B[k] == 0: continue
                derivations.append((A_B_derivation(A, B), A, B))
        slice_count += 1
    return derivations


if __name__ == '__main__':
    m, n, c = 13, 4, 1
    d = beta**m - alpha**n
    print(d)
    for r in solve_pow_dif(m, n, c):
        U, A, B = r
        l = Fraction(c*U, d)
        if l.is_integer():
            print(l, U, A, B)
