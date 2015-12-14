import functools
import itertools

REFLECTIONS = {
    '0': '0',
    '1': '1',
    '6': '9',
    '8': '8',
    '9': '6'
}

IDENTITY_REFLECTIONS = [k for k, v in REFLECTIONS.items() if k == v]


def mirrorables(size):
    products = itertools.product(*([REFLECTIONS.keys()] * size))
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
