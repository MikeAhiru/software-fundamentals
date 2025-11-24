import random
random.seed()   #Prepare random number generator

acumPos = 0
acumNeg = 0
numVeces = int(input("Escribe el número de veces que desea lanzar los dados: "))
for i in range(1, numVeces + 1, 1):
    dado1 = int(random.random() * 6)
    dado2 = int(random.random() * 6)
    if dado1 + dado2 % 2 == 0:
        acumPos = acumPos + 1
    else:
        acumNeg = acumNeg + 1
print("Los tiros pares fueron: " + str(acumPos))
print("Los tiros Impares fueron: " + str(acumNeg))
