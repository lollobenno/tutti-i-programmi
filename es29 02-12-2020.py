list = []
print('Programma escursione termica')
print('Per interrompere il programma digitare -1 nella temperatura prefissata')
list2 = []
numero_città = 0
while True:
    nome = input('Nome della città: ')
    escursione = int(input('Temperatuta prefissata: '))
    if escursione == -1:
        print('Città con escursione termica sopra la norma: ', list)
        print('Numero di città sopra la norma: ', max(list2))
        break
    massima = int(input('Temparatura massima raggiunta: '))
    minima = int(input('Temperatura minima raggiunta: '))
    escursione_reale = (massima + minima)/2
    print('Escursione termica:', escursione_reale)
    if escursione_reale > escursione :
        list.append(nome)
        print('Escursione termica maggiore della norma per ', nome)
        numero_città = numero_città + 1
        list2.append(numero_città)
    if escursione_reale == escursione :
        print('Escursione termica nella norma per ', nome)
    if escursione_reale < escursione :
        print('Escursione termica inferiore alla norma per ', nome)