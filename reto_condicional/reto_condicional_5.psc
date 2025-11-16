Algoritmo reto_condicional_5
	Definir DI, year, phoneNumber, salary, salaryFinally, salaryTotal Como Real;
	Definir name, lastName, gender, address Como Caracter;
	Escribir "Escribe tipo de identificación (CC, PS, CE, CI:)";
	leer DI;
	Escribir "Escribe nombre:";
	leer name;
	Escribir "Escribe apellido";
	leer lastName;
	Escribir "Escribe tu género (F) o (M):"
	leer gender;
	Escribir "Escribe tu año de nacimiento";
	leer year;
	Escribir "Escribe tipo dirección";
	leer address;
	Escribir "Escribe tu número telefónico";
	leer phoneNumber;
	Escribir "Escribe tu salario";
	leer salary;
	Si salary >= 200000 Entonces
		Si gender = "F" Entonces
			salaryFinally = salary*0.03
		SiNo
			salaryFinally = salary*0.025
		Fin Si
	SiNo
		Si salary >= 1200000 Entonces
			salaryFinally = salary * 0.05
		SiNo
			Si salary <= 1200000 Entonces
				Si gender = "F" Entonces
					salaryFinally = salary*0.10
				SiNo
					salaryFinally = salary*0.08
				Fin Si
			SiNo
				
			Fin Si
		Fin Si
	Fin Si
	salaryTotal = salaryFinally + salary
	Escribir "El usuario registrado con ", name, lastName, " identificado con  ", DI, " con año de nacimiento:", year, " con dirección en: ", address,  " con número de teléfono: ", phoneNumber, " y con un salario inicial de: ", salary," su salario final es de: ", salaryTotal
	
	
FinAlgoritmo
