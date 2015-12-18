"""Filen http://pastebin.com/sJVZp7BH inneholder liste av tall hvor det første tallet er prisen på en aksje på dag 1, og neste tallet er prisen på dag 2, osv. Dette er den samme lista som i luke 2.

Gitt at du har lov å gjøre nøyaktig to (2) transaksjoner, hva er den høyeste mulige profitten du kan oppnå?

En transaksjon vil si at du kjøper en aksje på en dag, for å så selge den igjen et vilkårlig antall dager senere.

Det finnes to begrensninger:

Du er nødt å selge den første aksjen før du kan kjøpe den andre aksjen.
Du har ikke lov å kjøpe og selge en aksje på samme dag. Det vil si at du må vente til minst dagen etter du fullfører den første transaksjonen før du kan starte den andre.

Svaret skal oppgis med fire desimaler, samt bruke punktum som desimalskilletegn. Eksempel: 12.3450
"""

from decimal import Decimal
from functools import reduce
from itertools import accumulate


def read_data(filename):
    with open(filename, 'r') as f:
        yield from (Decimal(l) for l in map(str.strip, f) if l)


def calc_before(prices):
    """Calculate the max profits for transactions completed on or before
    each day."""

    mins = list(accumulate(prices, min))
    return reduce(lambda b, s: b + [max(prices[s] - mins[s - 1], b[-1])],
                  range(1, len(prices)),
                  [prices[1] - prices[0]])


def calc_after(prices):
    """Calculate the max profits for transactions started on or after
    each day."""

    maxs = list(accumulate(reversed(prices), max))
    maxs.reverse()

    result = reduce(lambda a, b: a + [max(maxs[b + 1] - prices[b], a[-1])],
                    reversed(range(0, len(prices) - 1)),
                    [prices[-1] - prices[-2]])
    result.reverse()
    return result


def best_profit(prices):
    before = calc_before(prices)
    after = calc_after(prices)
    best = max(before[day] + after[day + 1]
               for day in range(1, len(prices) - 2))
    return best


if __name__ == '__main__':
    prices = list(read_data("p10_input.txt"))
    print(best_profit(prices))
