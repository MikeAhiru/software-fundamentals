Algoritmo challenger_4
	Definir dado1, dado2, numveces Como Entero
	numveces <- 0
	Repetir
		numveces <- numveces+1
		dado1 <- Aleatorio(1,6)
		dado2 <- Aleatorio(1,6)
		Escribir 'Lanzamiento No ', numveces
		Escribir 'Resultado dado No 1: ', dado1
		Escribir 'Resultado dado No 2: ', dado2
		Escribir "-------------------------"
	Hasta Que dado1=6 Y dado2=6
	Escribir 'Obtuviste un par de seis'
FinAlgoritmo
