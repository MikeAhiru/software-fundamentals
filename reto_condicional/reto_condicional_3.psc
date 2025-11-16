Algoritmo reto_condicional_3
	Definir num1 Como Real
	Escribir "Escribe un número entero (positivo o negativo)"
	Leer num1;
	Si num1 >= 0 Entonces
		Si num1 MOD 2 = 0 Entonces
			Escribir " El número ingresado es par positivo"
		SiNo
			Escribir " El número ingresado es impar positivo"
		Fin Si
	SiNo
		Si num1 MOD 2 = 0 Entonces
			Escribir " El número ingresado es impar negativo"
		SiNo
			Escribir " El número ingresado es impar negativo"
		Fin Si
	Fin Si
	
	
	
FinAlgoritmo
