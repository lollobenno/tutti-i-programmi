x = int(input('Quanti voti ha ricevuto il 1° candidato? '))
y = int(input('Quanti voti ha ricevuto il 2° candidato? '))
z = x+y
d = (x/z)*100
u = (y/z)*100
print('Percentuale 1° candidato: ', d, '%')
print('percentuale 2° candidato: ', u, '%')
if d>u :
    print('Il primo candidato ha vinto!')
if d<u :
    print('il secondo candidato ha vinto!')
else :
    print('Sono pari!')