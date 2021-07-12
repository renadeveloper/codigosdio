def notas_media(x, y):
    media=(x+y)/2
    print('media = %.2f' %media)

def notas_validas():
    x = float(input())
    if x <= 10 and x>=0:
        return x
    else:
        print('nota invalida')
        return notas_validas()

choice = 1
while choice == 1:
    j = -1
    k = -1
    while k==-1:
        k = notas_validas()
    while j==-1:
        j = notas_validas()
    notas_media(k,j)
    choice =3
    while choice<1 or choice>2:
        choice = eval(input('novo calculo (1-sim 2-nao)\n'))