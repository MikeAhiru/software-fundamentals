# limpiar pantalla 
import os
os.system("clear")

#Iniciar contadores:
contador_empleados = 0
contador_gender_f = 0
contador_gender_m = 0
contador_gender_o = 0
total_salario = 0
suma_edades = 0


# Iniciamos el ciclo

while True:

    #Tenemos que validar que el nombre es caracter o letras
    while True:
        name = input("Ingrese su nombre: ") 
        if name.replace(' ', '').isalpha(): # isalpha() verifica que todos los caracteres sean alfabeticos
            break
        print("Nombre invalido, solo se puede ingresar letras).")


    # validacion para el correo electronico, el cual contenga @
    while True:
        email = input("Ingrese su correo electronico: ")
        # Usamos el operador 'in' para verificar si el carácter '@' está en la cadena.
        if '@' in email:
            break
        print("Correo incorrecto,el correo debe contener el simbolo '@'.")


    # validacion de telefono el cual contenga 10 digitos
    while True:
        phone = input("Ingrese su número telefónico: ") # Verificamos que sea dígito (isdigit()) Y que la longitud sea 10
        if phone.isdigit() and len(phone) == 10:
            break
        print("Teléfono incorrecto, debe ingresar exactamente 10 digitos.")

    
    # Validación de genero 
    gender = input("Ingrese su género (M/F/O): ")
    
    while (gender != "M") and (gender != "F") and (gender != "O") and (gender != "m") and (gender != "f") and (gender != "o"):
        
        print("Genero incorrecto, por favor ingrese (M, F, O, m, f u o)")
        gender = input("Ingrese su género (M/F/O): ")
    
    # Normalizamos el genero, dato que se usara para contador 
    if gender == "M" or gender == "m":
        gender_norm = "M"
    elif gender == "F" or gender == "f":
        gender_norm = "F"
    else: 
        gender_norm = "O"


    # validamos salario, primero que sea entero y posterior positivo
    while True:
        try:
            salary = int(input("Ingrese su salario mensual (entero positivo): "))
            # Verificamos que sea positivo (mayor a cero)
            if salary > 0:
                break
            else:
                print("Salario inválido. Debe ser un número entero positivo.")
        except ValueError:
            print("Entrada inválida. Por favor ingrese un número entero.")


    # validamos el año de nacimiento 
    year_max = 2007 # Permite hasta 18 años cumplidos en 2025
    year_min = 1900 
    
    while True:
        try:
            birth_year = int(input(f"Ingrese su año de nacimiento (4 dígitos, entre {year_min} y {year_max}): "))
            
            # Verificamos 4 dígitos (opcional si ya es int, pero buena práctica de rango)
            es_valido = (birth_year >= year_min) and (birth_year <= year_max)
            
            if es_valido:
                break
            else:
                print(f"Año inválido. El año debe ser de 4 dígitos y estar entre {year_min} y {year_max} para ser mayor de edad.")
        except ValueError:
            print("Entrada inválida. Por favor ingrese un número entero de 4 dígitos.")
    #Calcular la edad actual 
    age = 2025 - birth_year

    #registro del empleado
    empleado = {
        "Nombre": name,
        "Correo": email,
        "Genero": gender,
        "Salario": salary,
        "Telefono": phone,
        "Año de nacimiento": birth_year,
        "Edad": age
    }
    #actualizamos contadores
    contador_empleados += 1
    total_salario += salary
    suma_edades += age

    if gender_norm == "M":
        contador_gender_m += 1
    elif gender_norm == "F":
        contador_gender_f += 1
    else:
        contador_gender_o += 1
    #validamos si desea agregar otro empleado
    agregar_otro = input("Desea registrar otro empleado (S/N): ")
    while agregar_otro != "s" and agregar_otro != "n" and agregar_otro != "S" and agregar_otro != "N":
        print("La entrada no es valida")
        agregar_otro = input("Desea registrar otro empleado (S/N): ")
    if agregar_otro == "n" or agregar_otro == "N":
        break
    print("-------")

#imprimimos resultados
print("---Resumen Resultados---")
print("Total de empleados registrados: ", contador_empleados)
print("Total de empleados masculinos: ", contador_gender_m)
print("Total de empleados femeninos: ", contador_gender_f)
print("Total de empleados otros: ", contador_gender_o)
print("Salario total de todos los empleados: ", total_salario)
promedio_edades = suma_edades/ contador_empleados if contador_empleados > 0 else 0
print(f"Promedio de edades: {promedio_edades}")
