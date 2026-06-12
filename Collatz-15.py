
from NumberTheoryTools import *

def A_B_derivation(A, B):
    cal_A = alpha ** sum(B[:-1])
    cal_B = 1
    frak_U = 0
    R_A = []
    R_B = []
    for i in range (0, len(A)):
        frak_U += cal_A * cal_B
        a, b = alpha**(A[i]), beta**(B[i])
        cal_A //= a
        cal_B *= b
        _, r_a, r_b = extended_gcd(a, b)
        print(_)
        R_A.append(r_a)
        R_B.append(r_b)
    return frak_U, R_A, R_B

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
    series_a = [1, 2, 3, 4]
    series_b = [1, 2, 1, 1]
    m = sum(series_a)
    n = sum(series_b)
    d = beta**m - alpha**n
    D, A, B = A_B_derivation(series_a, series_b)
    print(d, D, D % d == 0)
    print(A, B)

