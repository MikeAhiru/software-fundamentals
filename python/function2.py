#2.	Funcion1. Crea un programa que pida un mensaje personalizado al usuario y a través de una función muestre ese mensaje.
def showGreeting (userName):
	print (f"Hello {userName} Welcome")
	
#here is main
print ("Enter your name: ")
user_name = input()
showGreeting(user_name)