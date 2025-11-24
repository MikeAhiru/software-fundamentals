Algoritmo challenges_3
	definir numVeces, dado1, i, total1, total2, total3, total4, total5, total6 Como Entero
	total1 = 0
	total2 = 0
	total3 = 0
	total4 = 0
	total5 = 0
	total6 = 0
	
	Escribir "Escribe el numero de veces que desea lanzar el dado: "
	Leer numVeces
	
	Para i<-1 Hasta numVeces Con Paso 1 Hacer
		dado1 = Aleatorio(1,6)
		Si dado1 = 1 Entonces
			total1 = total1 +1
		SiNo
			Si dado1 = 2 Entonces
				total2 = total2 +1
			SiNo
				Si dado1 = 3 Entonces
					total3 = total3 + 1
				SiNo
					Si dado1 = 4 Entonces
						total4 = total4 + 1
					SiNo
						Si dado1 = 5 Entonces
							total5 = total5 + 1
						SiNo
							Si dado1 = 6 Entonces
								total6 = total6 + 1
							SiNo
							Fin Si
						Fin Si
					Fin Si
				Fin Si
			Fin Si
		Fin Si
		Escribir "El valor otorgado de No ", i ," es de: ", dado1
	Fin Para
	Escribir "----------------------"
	Escribir "el número 1 se genero: " , total1 , " veces"
	Escribir "el número 1 se genero: " , total2 , " veces"
	Escribir "el número 1 se genero: " , total3 , " veces"
	Escribir "el número 1 se genero: " , total4 , " veces"
	Escribir "el número 1 se genero: " , total5 , " veces"
	Escribir "el número 1 se genero: " , total6 , " veces"
	
FinAlgoritmo
