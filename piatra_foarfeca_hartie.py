import random

victorii_utilizator = 0
victorii_calculator = 0


optiuni = ["piatra", "hartie", "foarfeca"]

while True:
    utilizator_input = input("Scrie Piatra/Hartie/Foarfeca sau Q pentru a renunța: ").lower()
    
    if utilizator_input == "q":
        break

    if utilizator_input not in optiuni:
        print("Opțiune invalidă, te rog mai încearcă!")
        continue

    numar_aleator = random.randint(0, 2)
   
    alegere_calculator = optiuni[numar_aleator]
    print("Calculatorul a ales " + alegere_calculator + ".")

    
    if utilizator_input == "piatra" and alegere_calculator == "foarfeca":
        print("Ai câștigat!")
        victorii_utilizator += 1

    elif utilizator_input == "hartie" and alegere_calculator == "piatra":
        print("Ai câștigat!")
        victorii_utilizator += 1

    elif utilizator_input == "foarfeca" and alegere_calculator == "hartie":
        print("Ai câștigat!")
        victorii_utilizator += 1
    
    elif utilizator_input == alegere_calculator:
        print("Egalitate!")

    else:
        print("Ai pierdut!")
        victorii_calculator += 1


print("Ai câștigat de", victorii_utilizator, "ori.")
print("Calculatorul a câștigat de", victorii_calculator, "ori.")
print("La revedere!")