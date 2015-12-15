from functools import reduce

MAP = [[34, 21, 32, 41, 25],
       [14, 42, 43, 14, 31],
       [54, 45, 52, 42, 23],
       [33, 15, 51, 31, 35],
       [21, 52, 33, 13, 23]]


def solve(m, coord):
    while True:
        yield coord
        row, col = divmod(coord, 10)
        coord, last_coord = m[row - 1][col - 1], coord
        if last_coord == coord:
            return

print(', '.join(map(str, solve(MAP, 11))))

