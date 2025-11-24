Algoritmo challenges_5
	definir i, numVeces, dado1, dado2, acumPos, acumNeg Como Entero
	acumPos = 0
	acumNeg = 0
	Escribir "Escribe el número de veces que desea lanzar los dados"
	leer numVeces
	Para i<-1 Hasta numVeces Con Paso 1 Hacer
		dado1 = Aleatorio(1,6)
		dado2 = Aleatorio(1,6)
		Si (dado1+dado2) MOD 2 =0 Entonces
			acumPos = acumPos + 1
		SiNo
			acumNeg = acumNeg + 1
		Fin Si
	Fin Para
	Escribir "Los tiros pares fueron: " , acumPos
	Escribir "Los tiros Impares fueron: ", acumNeg
FinAlgoritmo
