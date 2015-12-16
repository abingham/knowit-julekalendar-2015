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
    return total + _slow_count(n[1:], k)


def slow_count(n, k):
    return _slow_count(str(n), str(k))


def count(n, k):
    """Count the number of times the digit `k` appears in the decimals numbers
    from `[0-n]`.
    """
    original = n
    power = 0
    total = 0

    while n > 0:
        magnitude = 10 ** power
        n, lsd = divmod(n, 10)

        total += lsd * (magnitude * power) // 10

        if lsd > k:
            total += magnitude
        elif lsd == k:
            total += original % magnitude + 1

        power += 1

    return total


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
