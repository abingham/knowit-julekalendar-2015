"""
På http://pastebin.com/raw.php?i=p1eVAM5H finner du en usortert liste med odde antall elementer.
Elementene kan være romertall, binærtall eller heltall. Hva er mediantallet i denne lista?

Svar oppgis i talltypen tallet faktisk er i (eks. er medianen ti i binær, skriver du 0b1010, er det ti i romertall skriver du X). Alle binærtall starter med 0b, f. eks er 0b1010 det samme som 10.
"""

# Roman numeral support taken from
# http://docutils.sourceforge.net/docutils/utils/roman.py
# Copyright (c) 2001 Mark Pilgrim
roman_numeral_map = (('M',  1000),
                     ('CM', 900),
                     ('D',  500),
                     ('CD', 400),
                     ('C',  100),
                     ('XC', 90),
                     ('L',  50),
                     ('XL', 40),
                     ('X',  10),
                     ('IX', 9),
                     ('V',  5),
                     ('IV', 4),
                     ('I',  1))


def from_roman(s):
    result = 0
    for rom, num in roman_numeral_map:
        while s.startswith(rom):
            result += num
            s = s[len(rom):]
    return result


def parse_number(n):
    if n.startswith('0b'):
        return int(n, base=2)
    elif n[0].isalpha():
        return from_roman(n)
    return int(n)


def read_data(stream):
    for line in filter(bool, (l.strip() for l in f)):
        yield (line, parse_number(line))


if __name__ == '__main__':
    with open('p11_input.dat', 'r') as f:
        data = list(read_data(f))
    data.sort(key=lambda x: x[1])
    median_index = len(data) // 2
    print(data[median_index][0])

