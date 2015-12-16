"""
Tell antall forekomster av tallet 2 fra og med 0 til og med n.

Eksempel for n = 22:
Tall der ett eller flere siffer er 2 i [0, 22] er [2, 12, 20, 21, 22]. I denne lista kan vi se at det totalt er 6 sifre som er 2 (1 i 2, 1 i 12, 1 i 21 og 2 i 22), altså blir output 6 når n = 22.

Finn antall forekomster av tallet 2 for n = 12345678987654321
"""


def _slow_count(n, k):
    if not n:
        return 0

    size = len(n)
    hi_order = int(n[:1])
    total = 0

    n_num = int(n)
    k_num = int(k)

    if size > 1:
        total += hi_order * 10 ** (size - 2) * (size - 1)
    if hi_order > k_num:
        total += 10 ** (size - 1)
    elif hi_order == k_num:
        total += n_num - hi_order * 10 ** (size - 1) + 1
    return total + _count(n[1:], k)


def slow_count(n, k):
    return _count(str(n), str(k))


def count(n, k):
    original = n
    power = 1
    i = 0
    counter = 0

    while n > 0:
        n, d = divmod(n, 10)

        counter += d * (power * i) // 10

        if d > k:
            counter += power
        elif d == k:
            counter += original % power + 1

        power *= 10
        i += 1

    return counter


def timing():
    import timeit
    print('old', timeit.timeit('old_count(12345678987654321, 2)',
                               globals=globals(),
                               number=10000))
    print('new', timeit.timeit('count(12345678987654321, 2)',
                               globals=globals(),
                               number=10000))

if __name__ == '__main__':
    print(count(12345678987654321, 2))
