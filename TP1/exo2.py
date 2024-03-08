class Noeud:
    def __init__(self, valeur):
        self.valeur = valeur
        self.suivant = None

    def __repr__(self):
        return str(self.valeur)


class Pile:
    def __init__(self):
        self.tete = None

    def push(self, noeud):
        noeud.suivant = self.tete
        self.tete = noeud

    def pop(self):
        if self.estVide():
            return None  # Ou lever une exception
        noeudsupprime = self.tete
        self.tete = self.tete.suivant
        noeudsupprime.suivant = None  # Détacher le noeud supprimé
        return noeudsupprime

    def peek(self):
        return self.tete if not self.estVide() else None

    def estVide(self):
        return self.tete is None

    def taille(self):
        noeud = self.tete
        taille = 0
        while noeud is not None:
            taille += 1
            noeud = noeud.suivant
        return taille

    def __repr__(self):
        valeurs = []
        noeud = self.tete
        while noeud is not None:
            valeurs.append(str(noeud.valeur))
            noeud = noeud.suivant
        return ' -> '.join(valeurs)


def analyse(expression):
    pile = []
    parenthese_correspondante = {')': '(', '}': '{', ']': '[', '>': '<'}

    for char in expression:
        if char in "([{<":
            pile.append(char)
        elif char in ")]}>":
            if not pile or pile[-1] != parenthese_correspondante[char]:
                return False
            pile.pop()

    return not pile


def analysev2(expression):
    pile = []
    positions = []  # Pour enregistrer les positions des caractères ouvrants
    parenthese_correspondante = {')': '(', '}': '{', ']': '[', '>': '<'}

    for i, char in enumerate(expression):
        if char in "([{<":
            pile.append(char)
            positions.append(i)  # Enregistre la position du caractère ouvrant
        elif char in ")]}>":
            if not pile:
                return f"Caractère fermant en trop '{char}' à la position {i}"
            if pile[-1] != parenthese_correspondante[char]:
                expected = "une des " + ", ".join(parenthese_correspondante.values())
                return (f"Mauvaise correspondance à la position {i}: "
                        f"attendu {expected}, mais trouvé '{char}' correspondant à '{pile[-1]}' à la position {positions[-1]}")
            pile.pop()
            positions.pop()

    if pile:
        # S'il reste des caractères ouvrants dans la pile, cela signifie qu'il y a des caractères ouvrants sans correspondance.
        return f"Caractère ouvrant sans correspondance '{pile[-1]}' à la position {positions[-1]}"

    return "L'expression est correctement parenthésée."

    # Exemple d'utilisation


expression = "(a + b] * c)"
print(analyse(expression))


# fais l'analyse pour un fichier
def analyse_fichier(file):
    with open(file, 'r') as f:
        file_content = f.read()
        return analysev2(file_content)


if __name__ == '__main__':
    # Test l'analyse pour une fichier
    print(analyse_fichier('TP1  - avance.html'))

