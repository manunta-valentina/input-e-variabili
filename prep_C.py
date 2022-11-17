lista=[ ]
for x in range (5):
    numero = input ("inserire numero:")
    numero = int(numero)
    lista.append(numero)
lista.reverse()
for x in lista :
    q=int (x/2)
    if q*2==x :
       print(x)