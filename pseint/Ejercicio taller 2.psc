Algoritmo Ejercicio_taller_2 
	//Escriba un Script en PseInt que solicite al jugador el número de veces que desea lanzar el dado, una vez finalice los tiros, debe mostrar por pantalla la suma total de los valores generados en los lanzamientos//  
	Definir n_veces,resultado,contador, lanzamiento, suma_total Como Entero
	suma_total<-0
	Escribir "Escribe el número de veces que desea lanzar el dado: ";
	Leer n_veces;
	Para contador<-1 Hasta n_veces Con Paso 1 Hacer;
		lanzamiento <- Aleatorio(1,6);
		Escribir "Lanzamiento No ", contador, "El resultaod es: " lanzamiento;
		suma_total <- suma_total + lanzamiento;
	Fin Para
	Escribir "la suma total de todos los valores generados es: " suma_total;	
FinFuncion
	
FinAlgoritmo
