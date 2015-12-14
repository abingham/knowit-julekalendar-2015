import collections
import itertools

REFLECTIONS = collections.OrderedDict([
    ('0', '0'),
    ('1', '1'),
    ('6', '9'),
    ('8', '8'),
    ('9', '6'),
])

IDENTITY_REFLECTIONS = [k for k, v in REFLECTIONS.items() if k == v]


def mirrorables(size):
    products = itertools.product(*([sorted(REFLECTIONS.keys())] * size))
    return (''.join(s) for s in products)


def make_mirror(s):
    return ''.join(reversed([REFLECTIONS[c] for c in s]))


def mirrored():
    yield from (ir for ir in IDENTITY_REFLECTIONS)

    for size in itertools.count(1):
        yield from (
            m + make_mirror(m)
            for m in mirrorables(size)
            if m[0] != '0'
        )

        yield from (
            m + mid + make_mirror(m)
            for m in mirrorables(size)
            for mid in IDENTITY_REFLECTIONS
            if m[0] != '0'
        )


def mirrored_short():
    return (x for x in map(str, range(100001)) if x == x[::-1].translate(x.maketrans('69', '96', '23457')))


def solution():
    return len([x for x in map(str, range(100001)) if x == x[::-1].translate(x.maketrans('69', '96', '23457'))])


if __name__ == '__main__':
    print(solution())
