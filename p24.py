"""Det er i dag julaften, og har besluttet å kjøre en ganske enkel siste luke. Dagens oppgave er:

Hva er summen av alle positive heltall fra og med 1 til og med 100 000 000 000

Vi takker alle som har vært med for deltagelsen, og God Jul! :)
"""


def sum_through(i):
    i = int(i)
    return (1 + i) * i // 2


if __name__ == '__main__':
    print(sum_through(1e11))
