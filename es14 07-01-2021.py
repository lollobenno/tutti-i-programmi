'''crea un programma che scriva la differenza di due numeri a e b
se il loro prodotto è maggiore di 10,
oppure la loro somma se il prodotto è minore o uguale a 10'''

print('Questo programma somma i due numeri se il loro prodotto è maggiore di 10' 
'e li sottrae se sono minori o uguali a 10')

a = int(input('Inserisci il primo numero: '))
b = int(input('Inserisci il secondo numero: '))

numero_moltiplicato = a*b

if numero_moltiplicato > 10:
    numero_sommato = a+b
    print('La loro somma è ', numero_sommato)
else:
    numero_sottratto = a-b
    print('La loro differenza è ', numero_sottratto)