N = int(input('Inserire il n. di parole: '))
A = []
B = []
n = 1
while True:
    parola = input('inserire la parola: ')
    A.append(parola)
    B.append(len(parola))
    if N == n :
        print('il n. di lettere è ', B)
        break
    n = n + 1