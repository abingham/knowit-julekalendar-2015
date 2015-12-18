"""Filen http://pastebin.com/sJVZp7BH inneholder liste av tall hvor det første tallet er prisen på en aksje på dag 1, og neste tallet er prisen på dag 2, osv. Dette er den samme lista som i luke 2.

Gitt at du har lov å gjøre nøyaktig to (2) transaksjoner, hva er den høyeste mulige profitten du kan oppnå?

En transaksjon vil si at du kjøper en aksje på en dag, for å så selge den igjen et vilkårlig antall dager senere.

Det finnes to begrensninger:

Du er nødt å selge den første aksjen før du kan kjøpe den andre aksjen.
Du har ikke lov å kjøpe og selge en aksje på samme dag. Det vil si at du må vente til minst dagen etter du fullfører den første transaksjonen før du kan starte den andre.

Svaret skal oppgis med fire desimaler, samt bruke punktum som desimalskilletegn. Eksempel: 12.3450
"""

from decimal import Decimal
from itertools import islice


def read_data(filename):
    with open(filename, 'r') as f:
        yield from (Decimal(l) for l in map(str.strip, f) if l)


prices = list(read_data("p10_input.txt"))

before = [prices[1] - prices[0]]
for sell_day in range(1, len(prices)):
    for buy_day in range(0, sell_day):
        assert sell_day > buy_day
        value = prices[sell_day] - prices[buy_day]
        if before[-1] < value:
            before.append(value)
        else:
            before.append(before[-1])
        assert before[-1] >= before[-2]

print(before)
