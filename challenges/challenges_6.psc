Algoritmo challenges_6
	Definir dado1, dado2, totalTiros, sumaTotal, totalPar, totalImpar Como Entero
	definir veces Como Caracter
	totalTiros = 0
	sumaTotal = 0
	totalPar = 0
	totalImpar = 0
	veces = "S"
	Repetir
		totalTiros = totalTiros + 1
		dado1 = Aleatorio(1,6)
		dado2 = Aleatorio(1,6)
		sumaTotal = sumaTotal + dado1 + dado2
		Si (dado1 + dado2) MOD 2 = 0 Entonces
			totalPar = totalPar + 1
		SiNo
			totalImpar = totalImpar + 1
		Fin Si
		
		Escribir  "Lanzamiento No: ", totalTiros
		Escribir  "Resultado obtenido: "
		Escribir  "Dado No 1: ", dado1
		Escribir  "Dado No 2: ", dado2
		
		Escribir "Desea continuar lanzando los dados?(S/N)"
		leer veces
		veces <- Mayusculas(veces)
		
	Hasta Que veces <> "S"
	
	Escribir "Total de tiros efectuados: ", totalTiros
	Escribir "Suma total de tiros efectuados: ", sumaTotal
	Escribir "Total de tiros Pares efectuados: ", totalPar
	Escribir "Total de tiros Impares efectuados: ", totalImpar
	
	
FinAlgoritmo
