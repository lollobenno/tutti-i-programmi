parola = input('Inserisci la parola ')
parola_invertita = parola[::-1]
if parola == parola_invertita:
    print('La parola è un palindromo')
    print(parola_invertita)
else:
    print('la parola non è un palindromo')
    print(parola_invertita)