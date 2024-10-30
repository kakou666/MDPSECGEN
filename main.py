import random
import string
import tkinter as tk
from tkinter import simpledialog

def genere_mdp(length, include_uppercase, include_lowercase, include_digits, include_special):
    regle = ""
    if include_uppercase:
        regle += string.ascii_uppercase
    if include_lowercase:
        regle += string.ascii_lowercase
    if include_digits:
        regle += string.digits
    if include_special:
        regle += string.punctuation
    if not regle:
        print("Vous devez sélectionner au moins un type de charactères.")
        return ""

    mdp = []

    if include_uppercase:
        mdp.append(random.choice(string.ascii_uppercase))
    if include_lowercase:
        mdp.append(random.choice(string.ascii_lowercase))
    if include_digits:
        mdp.append(random.choice(string.digits))
    if include_special:
        mdp.append(random.choice(string.punctuation))
    
    while len(mdp) < length:
        mdp.append(random.choice(regle))

    random.shuffle(mdp) # Mélange
    return "".join(mdp)

def main():
    try:
        length = int(input("Entrez la longueur du mot de passe désirée : "))
    except ValueError:
        print("Veuillez rentrer un entier naturel.")
        return
    include_uppercase = input("Inclure des majuscules? (o/n) : ").lower() == "o"
    include_lowercase = input("Inclure des minuscules? (o/n) : ").lower() == "o"
    include_digits = input("Inclure des chiffres? (o/n) : ").lower() == "o"
    include_special = input("Inclure des caractères spéciaux? (o/n) : ").lower() == "o"

    mdp = genere_mdp(length, include_uppercase, include_lowercase, include_digits, include_special)

    if mdp :
        print(f"TADA : {mdp}")

if __name__ == "__main__":
    main()

