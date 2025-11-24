import random
random.seed()   #Prepare random number generator

dado1 = int(random.random() * 6)
print("El numero otogado es: " + str(dado1))
if dado1 % 2 == 0:
    print("El numero es Par")
else:
    print("El numero es IMPAR")

