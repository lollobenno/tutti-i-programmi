'''verifica se un numero è pari o dispari'''

from math import modf

numero_utente = int(input('Che numero inserisci? '))
numero_diviso = numero_utente/2
decimale,intero = modf(numero_diviso)
if decimale == 0:
    print('Il numero inserito è pari')
if decimale != 0:
    print('Il numero inserito è dispari')
