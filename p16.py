"""
Tell antall forekomster av tallet 2 fra og med 0 til og med n.

Eksempel for n = 22:
Tall der ett eller flere siffer er 2 i [0, 22] er [2, 12, 20, 21, 22]. I denne lista kan vi se at det totalt er 6 sifre som er 2 (1 i 2, 1 i 12, 1 i 21 og 2 i 22), altså blir output 6 når n = 22.

Finn antall forekomster av tallet 2 for n = 12345678987654321
"""


def brute_force(n):
    return sum(str(i).count('2') for i in range(0, n + 1))


def two_count(n):
    return brute_force(n)


if __name__ == '__main__':
    print(two_count(12345678987654321))

# # rank 10
# 2

# # rank 100
# 02
# 12
# 20 21 22 23 24 25 26 27 28 29
# 32
# 42
# 52
# 62
# 72
# 82
# 92

# 19

# previous-rank-count * 10 + (previous-rank - 1) * 

# # below 1000
# 002
# 012
# 020 021 022 023 024 . . .
# 032
# 042
# ...
# 092
# 102
# ...
# 200 201 202 203 204 ... 299
# 302
# 312
# 320 321 322

# so...

# 10 * previous-rank-size + (previous-rank - 1) 
