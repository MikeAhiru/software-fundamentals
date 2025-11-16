print("Escribe tipo de identificación (CC, PS, CE, CI:)")
dI = int(input())
print("Escribe nombre:")
name = input()
print("Escribe apellido")
lastName = input()
print("Escribe tu género (F) o (M):")
gender = input()
print("Escribe tu año de nacimiento")
year = int(input())
print("Escribe tipo dirección")
address = input()
print("Escribe tu número telefónico")
phoneNumber = int(input())
print("Escribe tu salario")
salary = int(input())
if salary >= 2000000:
    if gender == "F":
        salaryFinally = salary * 0.03
    else:
        salaryFinally = salary * 0.025
else:
    if salary >= 1200000:
        salaryFinally = salary * 0.05
    else:
        if salary <= 1200000:
            if gender == "F":
                salaryFinally = salary * 0.1
            else:
                salaryFinally = salary * 0.08
salaryTotal = salaryFinally + salary
print("El usuario registrado con " + name + lastName + " identificado con  " + str(dI) + " con año de nacimiento:" + str(year) + " con dirección en: " + address + " con número de teléfono: " + str(phoneNumber) + " y con un salario inicial de: " + str(salary) + " su salario final es de: " + str(salaryTotal))
