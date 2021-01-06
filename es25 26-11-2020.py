l = input('Come si chima il primo candidato? ')
r = input('Come si chiama il secondo candidato? ')
x = int(input('Punteggio Primo candidato:'))
y = int(input('punteggio secondo candidato:'))
if x>y :
    print('Ordine decrescente del punteggio: ', y, x)
if x<y :
    print('Ordine decrescente del punteggio: ', x, y)
list = [l,r]
list.sort()
print('Ordine alfabetico: ', list)