import sys
sys.set_int_max_str_digits(2 ** 30)


class Collatz:

    def __init__(self, startswith):
        assert startswith % 2 == 1, "Require an odd number"
        self.start = startswith
        self.series: list[int] = [startswith]
        self.gammas: list[int] = [0]

    def __eval_till__(self, n):
        for m in range(len(self.series) - 1, n + 1):
            odd = self.series[m]
            col = odd * 3 + 1
            gam = 0
            while col % 2 == 0:
                col >>= 1
                gam += 1
            self.series.append(col)
            self.gammas.append(gam)

    def number_at(self, n):
        self.__eval_till__(n)
        return self.series[n]

    def gamma_at(self, n):
        self.__eval_till__(n)
        return self.gammas[n]

    def accumulate_at(self, n):
        self.__eval_till__(n)
        return sum(self.gammas[:n + 1])

    def pack_at(self, n):
        return self.number_at(n) * (1 << self.accumulate_at(n))

    def wire_at(self, n):
        result = 0
        for i in range(0, n):
            result += (1 << self.accumulate_at(i)) * (3**(n - i - 1))
        return result

if __name__ == '__main__':
    a = Collatz(3 ** 10086)
    i = 0
    print(a.accumulate_at(i))
    while a.number_at(i) != 1:
        i += 1
        print(a.accumulate_at(i))

