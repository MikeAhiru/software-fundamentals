Algoritmo challenges_2
	definir numVeces, dado1, sumaTotal, i Como Entero
	sumaTotal <- 0
	Escribir "Escribe el numero de veces que desea lanzar el dado: "
	Leer numVeces
	
	Para i<-1 Hasta numVeces Con Paso 1 Hacer
		dado1 = Aleatorio(1,6)
		Escribir "El valor otorgado de No ", i ," es de: ", dado1
		sumaTotal = sumaTotal + dado1
		
	Fin Para
	Escribir "El resultado final es de: " ,  sumaTotal
FinAlgoritmo
