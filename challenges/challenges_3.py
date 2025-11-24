import random
random.seed()   #Prepare random number generator

total1 = 0
total2 = 0
total3 = 0
total4 = 0
total5 = 0
total6 = 0
print("Escribe el número de veces que desea lanzar el dado")
numVeces = int(input())
for i in range(1, numVeces + 1, 1):
    dado1 = int(random.random() * 6)
    if dado1 == 1:
        total1 = total1 + 1
    else:
        if dado1 == 2:
            total2 = total2 + 1
        else:
            if dado1 == 3:
                total3 = total3 + 1
            else:
                if dado1 == 4:
                    total4 = total4 + 1
                else:
                    if dado1 == 5:
                        total5 = total5 + 1
                    else:
                        if dado1 == 6:
                            total6 = total6 + 1
    print("El valor del dado No " + str(i) + " es de: " + str(dado1))
print("-----------------------------")
print("el número 1 se genero: " + str(total1) + " veces")
print("el número 2 se genero: " + str(total2) + " veces")
print("el número 3 se genero: " + str(total3) + " veces")
print("el número 4 se genero: " + str(total4) + " veces")
print("el número 5 se genero: " + str(total5) + " veces")
print("el número 6 se genero: " + str(total6) + " veces")
