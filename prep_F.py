def asterischi(lista):
    for elem in lista:
        print('*' * elem)

lista =  []

n = int(input("quanti numeri vuoi inserie?"))
for i in range(n):
    num = int(input("Dimmi un numero"))
    lista.append(num)

asterischi(lista)