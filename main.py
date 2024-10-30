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

def on_submit():
    length = int(length_entry.get())
    include_uppercase = uc.get()
    include_lowercase = lc.get()
    include_digits = dig.get()
    include_special = sp.get()

    mdp = genere_mdp(length, include_uppercase, include_lowercase, include_digits, include_special)
    result_label.config(text=f"Votre mot de passe généré est : {mdp}")

root = tk.Tk() #fenetre
root.title("Générateur de Mot de Passe")

tk.Label(root, text="Entrez la longueur du mot de passe :").pack()
length_entry = tk.Entry(root)
length_entry.pack()

uc = tk.BooleanVar()
tk.Checkbutton(root, text="Inclure des majuscules?", variable=uc).pack()

lc = tk.BooleanVar()
tk.Checkbutton(root, text="Inclure des minuscules?", variable=lc).pack()

dig = tk.BooleanVar()
tk.Checkbutton(root, text="Inclure des chiffres?", variable=dig).pack()

sp = tk.BooleanVar()
tk.Checkbutton(root, text="Inclure des caractères spéciaux?", variable=sp).pack()

submit_button = tk.Button(root, text="Générer", command=on_submit)
submit_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()



