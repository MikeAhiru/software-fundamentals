import random
random.seed()   #Prepare random number generator

dado1 = int(random.random() * 6)
dado2 = int(random.random() * 6)
print("El número del primer dado es: " + str(dado1))
print("El número del segundo dado es: " + str(dado2))
if dado1 % 2 == 0:
    print("El valor del primer dado es un número par")
else:
    print("El valor del primer dado es un número impar")
if dado2 % 2 == 0:
    print("El valor del segundo dado es un número par")
else:
    print("El valor del segundo dado es un número impar")
if dado1 == dado2:
    print("Los números de los dados son iguales ---YOU WIN----")
else:
    print("los números de los dados no son iguales ---GAME OVER----")

