import heapq
import itertools


def knalltallene():
    yield 1
    vals = [1]

    index = ([2, 0], [3, 0], [5, 0])

    while True:
        min_index = min(index, key=lambda i: i[0] * vals[i[1]])
        new_val = min_index[0] * vals[min_index[1]]
        vals.append(new_val)
        yield new_val
        for i in index:
            if new_val == i[0] * vals[i[1]]:
                i[1] += 1


def solution():
    # knalltall nummer 10000
    return next(itertools.islice(knalltallene(), 9999, 10000))


if __name__ == '__main__':
    print(solution())

