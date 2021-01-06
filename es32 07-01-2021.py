'''implementa l'algoritmo per il calcolo della soluzione di un'equazione di primo grado ax + b = 0.'''

print('Programma algoritmo ax + b = 0')

a = int(input('Inserisci il valore di a: '))
b = int(input('Inserisci il valore di b: '))

if a == 0:
    if b == 0:
        print('Equazione indeterminata')
    if b != 0:
        print('Equazione impossibile')
if a != 0:
    if b == 0:
        print('La soluzione è x = 0')
    if b != 0:
        print('La soluzione è x = ', -(b/a))