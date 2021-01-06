list = []
print('Programma del lanciatore')
print('Per interrompere il programma digitare nella distanza del lancio -1')
while True:
    lanci = 0
    lanci = lanci + 1
    nome = input('Nome del lanciatore: ')
    lancio = int(input('Distanza del lancio: '))
    list.append(lancio)
    list.sort()
    if lancio == -1:
        print('Valore massimo: ', list[lanci])
        break
    lanci = lanci + 1