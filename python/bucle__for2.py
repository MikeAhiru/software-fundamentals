import random
random.seed()   #Prepare random number generator

i = 1
countPares = 0
countImpares = 0
acumTotal = 0


print("Hoy many numbers?: ")
n = int(input())
for i in range(1, n + 1, 1):
    randomNum = int(random.random() * 100)
    print(randomNum)
    if randomNum % 2 == 0:
        countPares = countPares + 1
    else:
        countImpares = countPares + 1
    acumTotal = acumTotal + randomNum
print("######## REPORTE FINAL ######")
print("Total de pares generados " + str(countPares))
print("Total de impares generados " + str(countImpares))
print("La suma de los numeros generados es: " + str(acumTotal))
