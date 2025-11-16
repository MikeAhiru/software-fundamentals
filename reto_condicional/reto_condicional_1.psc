Algoritmo Reto_condicional_1 
	//Escriba un Script en PseInt que permita lanzar un dado y determine si el número generado es par o impar. 
	Definir dado1, dado2 Como Entero
	dado1 = Aleatorio(1,6);
	dado2 = Aleatorio (1,6);
	Escribir "El número del primer dado es: ", dado1;
	Escribir "El número del segundo dado es: ", dado2;
	Si dado1 MOD 2=0 Entonces
		Escribir "El valor del primer dado es un número par"
	SiNo
		Escribir "El valor del primer dado es un número impar"
	Fin Si
	Si dado2 MOD 2=0 Entonces
		Escribir "El valor del segundo dado es un número par"
	SiNo
		Escribir "El valor del segundo dado es un número impar"
	Fin Si
	Si dado1 = dado2 Entonces
		Escribir "Los números de los dados son iguales ---YOU WIN----"
	SiNo
		Escribir "los números de los dados no son iguales ---GAME OVER----"
	Fin Si
	
FinFuncion
	
FinAlgoritmo
