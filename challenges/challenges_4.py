import random

def challenges_4():
    numveces = 0
    
    while True:
        numveces = numveces + 1
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        print(f"Lanzamiento No {numveces}")
        print(f"Resultado dado No 1: {dado1}")
        print(f"Resultado dado No 2: {dado2}")
        print("------------------------------") 
        
        # Condicion para que ambos dados den 6
        if dado1 == 6 and dado2 == 6:
            break
    
    print("Obtuviste un par de seis")

# Ejecutar challenger
challenges_4()