MAP = [[34, 21, 32, 41, 25],
       [14, 42, 43, 14, 31],
       [54, 45, 52, 42, 23],
       [33, 15, 51, 31, 35],
       [21, 52, 33, 13, 23]]


def solve(m, coord):
    last_coord = None
    while last_coord != coord:
        yield coord
        row, col = divmod(coord, 10)
        coord, last_coord = m[row - 1][col - 1], coord

if __name__ == '__main__':
    print(', '.join(map(str, solve(MAP, 11))))
