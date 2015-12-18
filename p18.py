"""Gitt en liste med positive heltall, finn det største tallet det er mulig å lage ved å sette sammen alle tallene i lista i valgfri rekkefølge.

Eksempel 1: [3, 30, 34, 5, 9] => 9534330
Eksempel 2: [128,12] => 12812
Eksempel 3: [824,938,1399,5607,6973,5703,9609,4398,8247] => 9609938824824769735703560743981399

Finn størst mulig tall for listen: [2907, 6165, 6129, 3468, 2040, 4331, 7935, 5683, 6004, 9694, 8092, 188, 5796, 1184, 8873, 3200, 1981, 9556, 9981, 1387, 7802, 8387, 9970, 7326, 5372, 28, 628, 3408, 6, 3425, 3071, 6021, 9989, 5077, 824, 938, 1399, 5607, 6973, 5703, 9609, 4398, 8247, 5164, 2026, 4, 4468, 9524, 8, 9227, 8969, 1746, 5593]
"""

from itertools import permutations


def solve_slow(l):
    return max(int(''.join(p)) for p in permutations(map(str, l)))


def _solve_fast(l):
    if not any(x[2] for x in l):
        return ''

    # 1. Find natural largest unclaimed element
    # 2. Options at this level are (1) and any smaller element which is a
    #    prefix of it.
    # 3. Try each in turn, claiming it as you go, and recurse.
    largest = ''

    anchor = max((x for x in l if x[2]), key=lambda x: x[1])
    options = [x for x in l if anchor[1].startswith(x[1]) and x[2]]
    for option in options:
        option[2] = False
        rest = _solve_fast(l)
        largest = max(largest, option[1] + rest)
        option[2] = True
    return largest


def solve_fast(l):
    vals = sorted(([i, str(i), True] for i in l),
                  key=lambda i: i[1], reverse=True)
    result = _solve_fast(vals)
    assert len(result) == sum(map(len, map(str, l)))
    assert all(str(i) in result for i in l)
    return result


solve = solve_fast


if __name__ == '__main__':
    l = [2907, 6165, 6129, 3468, 2040, 4331, 7935, 5683, 6004, 9694, 8092,
         188, 5796, 1184, 8873, 3200, 1981, 9556, 9981, 1387, 7802, 8387,
         9970, 7326, 5372, 28, 628, 3408, 6, 3425, 3071, 6021, 9989, 5077,
         824, 938, 1399, 5607, 6973, 5703, 9609, 4398, 8247, 5164, 2026, 4,
         4468, 9524, 8, 9227, 8969, 1746, 5593]
    print(solve(l))
