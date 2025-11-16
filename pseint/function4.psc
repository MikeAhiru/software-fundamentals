Funcion msg <- showGreeting ( userName )
	Escribir "Hola " , userName, " Welcome"
Fin Funcion


Algoritmo Function3
	definir user_name, message Como Caracter
	Mostrar "Enter your name: "
	leer user_name
	message = showGreeting(user_name)
	Escribir message
	
FinAlgoritmo
