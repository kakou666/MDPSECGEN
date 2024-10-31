# MDPSECGEN - Générateur de mot de passe (KAWAII version)

Ce projet est un générateur de mot de passe simple qui permet aux utilisateurs de créer des mots de passe sécurisés en spécifiant la longueur et les types de caractères à inclure (majuscules, minuscules, chiffres et caractères spéciaux).

## Version : app.py

### Description

Ce projet est une application web qui génère des mots de passe forts en fonction des critères spécifiés par l'utilisateur, tels que :

- La longueur du mot de passe.
- L'inclusion de majuscules.
- L'inclusion de minuscules.
- L'inclusion de chiffres.
- L'inclusion de caractères spéciaux.

### Fonctionnalités

- **Génération de mots de passe sécurisés** : Personnalisez votre mot de passe en fonction de vos besoins.
- **Interface utilisateur intuitive** : Une interface web conviviale avec des éléments interactifs stylisés.
- **Validation des entrées** : Gestion des erreurs pour les entrées invalides ou manquantes.
- **Aucune dépendance externe complexe** : Seulement Python et Flask nécessaires.

### Prérequis

- **Python 3.x**
- **Flask**

### Installation

1. **Cloner le dépôt ou télécharger les fichiers**

   ```bash
   git clone https://github.com/votre-utilisateur/generateur-mots-de-passe.git
   ```

   *(Remplacez `votre-utilisateur` par votre nom d'utilisateur GitHub.)*

2. **Naviguer dans le répertoire du projet**

   ```bash
   cd MDPSECGEN
   ```

3. **Créer un environnement virtuel (optionnel mais recommandé)**

   ```bash
   python -m venv venv
   ```

   - **Sur Windows** :

     ```bash
     venv\Scripts\activate
     ```

   - **Sur macOS/Linux** :

     ```bash
     source venv/bin/activate
     ```

4. **Installer les dépendances**

   ```bash
   pip install flask
   ```

### Utilisation

1. **Lancer l'application**

   ```bash
   python app.py
   ```

   L'application démarrera en mode debug sur le port par défaut 5000.

2. **Accéder à l'application**

   Ouvrez votre navigateur web et allez à l'adresse :

   ```
   http://127.0.0.1:5000
   ```

3. **Générer un mot de passe**

   - **Entrez la longueur du mot de passe** : Saisissez un nombre entier positif.
   - **Sélectionnez les critères souhaités** : Cochez les cases correspondant aux types de caractères que vous souhaitez inclure.
   - **Cliquez sur "Générer"** : Le mot de passe généré s'affichera sous le formulaire.

### Exemple

<img width="849" alt="image" src="https://github.com/user-attachments/assets/69e83452-b220-4cd8-a522-52372ce94b47">


## Version : main.py

### Fonctionnalités 

- **Interface Utilisateur Graphique (GUI)** : Fournit une interface facile à utiliser pour la configuration des mots de passe.
- **Personnalisation** : Permet aux utilisateurs de choisir la longueur du mot de passe et les types de caractères à inclure.
- **Sécurité** : Utilise une méthode de mélange robuste pour assurer que les mots de passe générés sont aléatoires et sécurisés. 🥸

### Prérequis

Pour exécuter ce programme, vous devez avoir Python installé sur votre machine. Python 3.6 ou une version plus récente est recommandé.

### Installation

Clonez ce dépôt sur votre machine locale en utilisant la commande suivante :

```bash
git clone https://example.com/nomutilisateur/mdp.git
```

### Utilisation

1. Naviguez dans le dossier du projet cloné.
2. Lancez le programme avec la commande suivante :

```bash
python main.py
```

3. Utilisez l'interface graphique pour sélectionner les options de mot de passe désirées et cliquez sur "Générer" pour obtenir votre mot de passe.

### Exemple

<img width="486" alt="image" src="https://github.com/user-attachments/assets/4bff7d5e-1522-4909-8a7a-dfd2ee1e1f3a">


## Contributions

Les contributions à ce projet sont bienvenues. Voici comment vous pouvez contribuer :
- **Rapporter des bugs** : Utilisez l'onglet Issues pour signaler des bugs.
- **Proposer des améliorations** : Vous pouvez également proposer des améliorations ou de nouvelles fonctionnalités.
- **Soumettre des pull requests** : Les PR sont bienvenues pour des corrections de bugs, des améliorations de documentation, et plus encore.

## Licence

Ce projet est distribué sous la Licence MIT. 
