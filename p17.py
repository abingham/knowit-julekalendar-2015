"""Da Kongeriket Norge har kommet frem til at de er best i verden har de
funnet ut at de skal redefinere epoken for Unixtid. Den nye epoken er definert
til å være 17. mai 1814 kl 13:37:14.

Finn ut hva timestampen for 17. september 2015 kl 17:15:00 er med denne
omdefinerte epoken. Vi antar at skuddsekunder ikke eksisterer, og at dagens
regler for skuddår har vært gjeldende hele perioden.

Hint: Det er ikke sikkert diverse kalenderverktøy er spesielt nøyaktige på
tidspunkter så langt tilbake i tid.
"""

from datetime import datetime


start = datetime(1814, 5, 17, hour=13, minute=37, second=14)
stop = datetime(2015, 9, 17, hour=17, minute=15, second=0)
print(int((stop - start).total_seconds()))
