"""Filen http://pastebin.com/sJVZp7BH inneholder liste av tall hvor det første tallet er prisen på en aksje på dag 1, og neste tallet er prisen på dag 2, osv. Dette er den samme lista som i luke 2.

Gitt at du har lov å gjøre nøyaktig to (2) transaksjoner, hva er den høyeste mulige profitten du kan oppnå?

En transaksjon vil si at du kjøper en aksje på en dag, for å så selge den igjen et vilkårlig antall dager senere.

Det finnes to begrensninger:

Du er nødt å selge den første aksjen før du kan kjøpe den andre aksjen.
Du har ikke lov å kjøpe og selge en aksje på samme dag. Det vil si at du må vente til minst dagen etter du fullfører den første transaksjonen før du kan starte den andre.

Svaret skal oppgis med fire desimaler, samt bruke punktum som desimalskilletegn. Eksempel: 12.3450
"""

from decimal import Decimal


def read_data(filename):
    with open(filename, 'r') as f:
        yield from (Decimal(l) for l in map(str.strip, f) if l)


def calc_before(prices):
    before = [prices[1] - prices[0]]
    for sell_day in range(1, len(prices)):
        sell_price = prices[sell_day]
        max_on_sell_day = max(sell_price - prices[buy_day]
                              for buy_day in range(0, sell_day))

        if before[-1] < max_on_sell_day:
            before.append(max_on_sell_day)
        else:
            before.append(before[-1])
        assert before[-1] >= before[-2]
    return before


def calc_after(prices):
    after = [prices[-1] - prices[-2]]

    for buy_day in reversed(range(0, len(prices) - 1)):
        buy_price = prices[buy_day]
        max_on_sell_day = max(prices[sell_day] - buy_price
                              for sell_day in range(buy_day + 1, len(prices)))
        if after[-1] < max_on_sell_day:
            after.append(max_on_sell_day)
        else:
            after.append(after[-1])
        assert after [-1] >= after[-2]

    after.reverse()
    return after


def best_profit(prices):
    before = calc_before(prices)
    after = calc_after(prices)
    best = max(before[day] + after[day + 1]
               for day in range(1, len(prices) - 2))
    return best


if __name__ == '__main__':
    prices = list(read_data("p10_input.txt"))
    print(best_profit(prices))
