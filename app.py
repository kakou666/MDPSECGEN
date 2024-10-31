from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

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
        return None, "Vous devez sélectionner au moins un type de caractères."

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

    random.shuffle(mdp)  # Mélange
    return ''.join(mdp), None

@app.route('/', methods=['GET', 'POST'])
def index():
    password = None
    error_message = None
    if request.method == 'POST':
        length = request.form.get('length')
        try:
            length = int(length)
            if length <= 0:
                error_message = "Veuillez entrer une longueur positive."
                return render_template('index.html', password=password, error_message=error_message)
        except ValueError:
            error_message = "Veuillez entrer une longueur valide."
            return render_template('index.html', password=password, error_message=error_message)

        include_uppercase = 'include_uppercase' in request.form
        include_lowercase = 'include_lowercase' in request.form
        include_digits = 'include_digits' in request.form
        include_special = 'include_special' in request.form

        password, error_message = genere_mdp(length, include_uppercase, include_lowercase, include_digits, include_special)

    return render_template('index.html', password=password, error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)
