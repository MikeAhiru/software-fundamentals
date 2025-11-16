print("Escribe un número entero (positivo o negativo)")
num1 = int(input())
if num1 >= 0:
    if num1 % 2 == 0:
        print(" El número ingresado es par positivo")
    else:
        print(" El número ingresado es impar positivo")
else:
    if num1 % 2 == 0:
        print(" El número ingresado es impar negativo")
    else:
        print(" El número ingresado es impar negativo")
