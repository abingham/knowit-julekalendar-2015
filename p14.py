import functools
import itertools

REFLECTIONS = {
    0: 0,
    1: 1,
    6: 9,
    8: 8,
    9: 6
}

IDENTITY_REFLECTIONS = [k for k, v in REFLECTIONS.items() if k == v]


def mirrorables(size):
    if size < 1:
        raise ValueError("size argument must be positive.")

    yield from filter(
        lambda x: x[0] != 0 and x[-1] != 0,
        itertools.product(*([REFLECTIONS.keys()] * size)))


def make_mirror(s):
    return tuple(reversed([REFLECTIONS[c] for c in s]))


def _mirrored():
    yield from ((ir,) for ir in IDENTITY_REFLECTIONS)

    for size in itertools.count(1):
        for m in mirrorables(size):
            yield m + make_mirror(m)

        for m in mirrorables(size):
            for mid in IDENTITY_REFLECTIONS:
                yield m + (mid,) + make_mirror(m)


def to_int(s):
    return functools.reduce(
        lambda r, c: r * 10 + c, s, 0)


def mirrored():
    return map(to_int, _mirrored())


