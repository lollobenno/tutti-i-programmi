print('Programma numeri binari')
print('Per interrompere il programma inserire 2')
binario = int(input('Quanti numeri binari vuoi inserire? '))
n = 0
numero_decimale = 0
if binario > 1 :
    while True:
       binario3 = int(input('Inserisci una cifra del numero binario partendo da destra: '))
       if binario3 == 2:
           print('Numero decimale:', list)
           break
       if binario3 > 2:
           print('Non è un numero binario')
       if binario3 < 0:
           print('Non è un numero binario')
       binario_decimale2 = binario3*2**n
       numero_decimale = numero_decimale + binario_decimale2
       n = n + 1
if binario == 1:
    binario2 = int(input('Inserisci una cifra del numero binario partendo da destra: '))
    binario_decimale = binario2*2**n
    numero_decimale = numero_decimale + binario_decimale
    print('Numero decimale: ', numero_decimale)
else :
    print('Il numero inserito non è valido, inserire un numero intero superiore a 0')