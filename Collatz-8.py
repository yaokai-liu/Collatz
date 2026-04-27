from fractions import Fraction

alpha, beta, gamma = 3, 2, 1

def fraction_power(base, exponent):
    return Fraction(base**exponent, 1) if exponent > 0 else Fraction(1, base**abs(exponent))

def decompose_frak(a: Fraction):
    if a.is_integer(): return a.numerator, 0, 0
    s = a.denominator
    times_alpha, times_beta = 0, 0
    while s % alpha == 0:
        s //= alpha
        times_alpha += 1
    while s % beta == 0:
        s //= beta
        times_beta += 1
    return a.numerator, times_alpha, times_beta

def collatz_source_value(init_N, pre_reduces: list):
    cal_V = 0
    frak_a = 0
    for i in range(0, len(pre_reduces)):
        frak_a += Fraction((beta**cal_V), (alpha**i))
        cal_V += pre_reduces[i]
    N = Fraction((beta**cal_V), (alpha**len(pre_reduces))) * init_N - Fraction(gamma, alpha) * frak_a
    return N

def collatz_Delta_V(modify_reduces: list, origin_reduces: list):
    Delta_cal_V_n = sum(modify_reduces)
    cal_V_k = 0
    Delta_cal_V_k = 0
    Delta_frak_v: Fraction = 0
    for i in range(0, len(origin_reduces)):
        d_pow_cal_S = fraction_power(beta, Delta_cal_V_n) - fraction_power(beta, Delta_cal_V_k)
        Delta_frak_v += Fraction(fraction_power(beta, cal_V_k), fraction_power(alpha, i)) * d_pow_cal_S
        cal_V_k += origin_reduces[i]
        Delta_cal_V_k += modify_reduces[i]
    Delta_frak_V = Delta_frak_v * fraction_power(alpha, len(origin_reduces))
    return Delta_frak_V, Delta_frak_v, Delta_cal_V_n

def F_trans(reduces, adds: dict):
    return [r + adds[i] if adds.get(i) else r for i, r in enumerate(reduces)]

class CollatzTransformViewer:

    def __init__(self, basic_reduces: list, target_value: int):
        self.reduces = basic_reduces
        self.target_value = target_value
        self.step_count = len(basic_reduces)

    def modified_by(self, Delta_reduces: list):
        if len(Delta_reduces) > len(self.reduces):
            return None
        step_count = len(Delta_reduces)
        basic_reduces = self.reduces[self.step_count - step_count:]
        source_value = collatz_source_value(self.target_value, basic_reduces)
        Delta_frak_V, Delta_frak_v, Delta_cal_V_n = collatz_Delta_V(Delta_reduces, basic_reduces)
        A, B = source_value * fraction_power(beta, Delta_cal_V_n), Fraction(gamma, alpha) * Delta_frak_v
        new_source_value = A + B
        new_reduces = [basic_reduces[i] + Delta_reduces[i] for i in range(step_count)]
        return {
            "n": step_count,
            "b": self.target_value,
            "f_{n}(\\bm{v})": source_value,
            "\\Delta\\mathfrak{V}": Delta_frak_V,
            "\\Delta\\mathfrak{v}": Delta_frak_v,
            "\\beta^{\\Delta\\mathcal{V}_n}": fraction_power(beta, Delta_cal_V_n),
            "f_{n}(\\bm{v})\\cdot\\beta^{\\Delta\\mathcal{V}_n}": A,
            "\\frac{\\gamma}{\\alpha}\\cdot\\Delta\\mathfrak{v}": B,
            "f_{n}(\\bm{v} + \\Delta\\bm{v})[RHS]": new_source_value,
            "f_{n}(\\bm{v} + \\Delta\\bm{v})[LHS]": collatz_source_value(self.target_value, new_reduces),
            "\\PI\\Delta\\mathfrak{v}": decompose_frak(Delta_frak_v),
        }

if __name__ == '__main__':
    modify_reduce = [-1, -1, -1, -1, 0, 0, -1, 0, -1, -1, 0, -1, -1, -1, 0, 1, -1, -1, 0, -1, 0, -1, -1, -1, -1, -1, 1, -1, -1, -1, 2, 0, 0, 2, 1, -1, -1, 3, 2]
    viewer = CollatzTransformViewer([2] * len(modify_reduce), 1)
    for i in range(len(modify_reduce) - 1, -1, -1):
        result = viewer.modified_by(modify_reduce[i:])
        print(result['f_{n}(\\bm{v} + \\Delta\\bm{v})[LHS]'], result['f_{n}(\\bm{v} + \\Delta\\bm{v})[RHS]'], result['\\PI\\Delta\\mathfrak{v}'])
        print(result['f_{n}(\\bm{v})\\cdot\\beta^{\\Delta\\mathcal{V}_n}'] + result['\\frac{\\gamma}{\\alpha}\\cdot\\Delta\\mathfrak{v}'])
