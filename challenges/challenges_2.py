import random
random.seed()
sumaTotal = 0

numVeces = int(input("Escribe el número de veces que desea lanzar el dado: "))
for i in range(1, numVeces + 1, 1):
    dado1 = int(random.random() * 6)
    print("El valor otorgado No " + str(i) + " es de: " + str(dado1))
    sumaTotal = dado1 + sumaTotal
print("La suma total de los valores generadores es de: " + str(sumaTotal))
