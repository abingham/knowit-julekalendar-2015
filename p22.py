"""Et palindrom er ord som kan leses likt baklengs og forlengs (se https://en.wikipedia.org/wiki/Palindrome). Et eksempel på et slikt ord er agnesisenga.
Din oppgave er å finne minimum antall operasjoner som må til for å konvertere en streng til et palindrom gitt følgende regler:
* Du kan redusere verdien av en bokstav. For eksempel så kan d endres til c, men du kan ikke endre c til d.
* For å konstruere et palindrom kan du redusere verdien på bokstav gjentatte ganger inntil bokstaven blir a. Når bokstaven er blitt a så kan den ikke endres
* Hver redusering av verdien til en bokstav telles som en operasjon.

Noen eksempler:
Strengen abc kan konverteres til et palindrom med 2 operasjoner: abc -> abb -> aba.
Strengen qywo kan konverteres med 4 operasjoner: qywo -> pywo -> oywo -> oxwo -> owwo

Hva er det minste antallet operasjoner som trengs for å konverte strengen  "evdhtiqgfyvcytohqppcmdbultbnzevdbakvkcdpbatbtjlmzaolfqfqjifkoanqcznmbqbeswglgrzfroswgxoritbw" til et palindrom?
"""


def convert(word):
    return sum(abs(ord(a) - ord(b))
               for a, b
               in zip(word[:len(word) // 2],
                      reversed(word)))


if __name__ == '__main__':
    print(convert('evdhtiqgfyvcytohqppcmdbultbnzevdbakvkcdpbatbtjlmzaolfqfqjifkoanqcznmbqbeswglgrzfroswgxoritbw'))
