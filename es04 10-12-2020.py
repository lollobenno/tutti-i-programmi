from math import pi
print('Programma area')
print('Le aree calcolabili sono: quadrato, rettangolo, cerchio, triangolo')
list = ['Quadrato', 'Rettangolo', 'Cerchio', 'Triangolo']
while True:
    area = input('Quale area vuoi calcolare? ')
    if area == 'quadrato':
        lato_q = int(input('Inserisci il lato del quadrato '))
        area_q = lato_q**2
        print('Area del quadrato: ', area_q)
        break
    if area == 'rettangolo':
        altezza_r = int(input('Inserisci altezza del rettangolo: '))
        base_r = int(input('Inserisci la base del rettangolo: '))
        area_r = altezza_r*base_r
        print('Area del rettangolo: ', area_r)
        break
    if area == 'triangolo':
        altezza_t = int(input('Inserisci altezza del triangolo: '))
        base_t = int(input('Inserisci la base del triangolo: '))
        area_t = (altezza_t*base_t)/2
        print('Area del triangolo: ', area_t)
        break
    if area == 'cerchio':
        raggio_c = int(input('Inserisci il raggio del cerchio: '))
        area_c = raggio_c*2*pi
        print('Area del cerchio: ', area_c)
        break
    if area == list:
        print('Riscrivi la figura geometrica in stampato minuscolo.')
    else:
        print('La parola scritta non è una figura che può essere calcolata in questo programma')