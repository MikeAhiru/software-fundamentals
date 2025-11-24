import random
random.seed()   #Prepare random number generator

totalTiros = 0
sumaTotal = 0
totalPar = 0
totalImpar = 0
veces = "S"
while True:    #This simulates a Do Loop
    totalTiros = totalTiros + 1
    dado1 = int(random.random() * 6)
    dado2 = int(random.random() * 6)
    sumaTotal = sumaTotal + dado1 + dado2
    if dado1 + dado2 % 2 == 0:
        totalPar = totalPar + 1
    else:
        totalImpar = totalImpar + 1
    print("Lanzamiento No: " + str(totalTiros))
    print("Resultado obtenido: ")
    print("Dado No 1: " + str(dado1))
    print("Dado No 1: " + str(dado2))
    veces = input("Desea continuar lanzando los dados?(S/N): ")
    veces = veces.upper()
    if veces != "S": break
print("Total de tiros efectuados: " + str(totalTiros))
print("Suma total de los tiros efectuados: " + str(sumaTotal))
print("Total de pares generados: " + str(totalPar))
print("Total de impares generados: " + str(totalImpar))
