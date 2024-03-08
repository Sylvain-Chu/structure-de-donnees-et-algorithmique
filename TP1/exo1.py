class Noeud:
    def __init__(self, valeur):
        self.valeur = valeur
        self.suivant = None

    def __repr__(self):
        return str(self.valeur)


class ListeChainee:
    def __init__(self):
        self.tete = None

    def inserer(self, noeud):
        if self.tete is None:
            self.tete = noeud
        else:
            noeud.suivant = self.tete
            self.tete = noeud

    def supprimer(self, valeur):
        noeud = self.tete
        precedent = None
        while noeud is not None:
            if noeud.valeur == valeur:
                if precedent is None:
                    self.tete = noeud.suivant
                else:
                    precedent.suivant = noeud.suivant
                return
            precedent = noeud
            noeud = noeud.suivant

    def rechercher(self, valeur):
        noeud = self.tete
        while noeud is not None:
            if noeud.valeur == valeur:
                return True
            noeud = noeud.suivant
        return False

    def taille(self):
        noeud = self.tete
        taille = 0
        while noeud is not None:
            taille += 1
            noeud = noeud.suivant
        return taille

    def estVide(self):
        return self.tete is None

    def __repr__(self):
        valeurs = []
        noeud = self.tete
        while noeud is not None:
            valeurs.append(str(noeud.valeur))
            noeud = noeud.suivant
        return ' -> '.join(valeurs)


if __name__ == '__main__':
    liste = ListeChainee()

    # Créez et insérez des noeuds séparément
    liste.inserer(Noeud(1))
    liste.inserer(Noeud(2))
    liste.inserer(Noeud(3))

    # Créez et insérez des noeuds directement
    print(liste)  # Doit afficher 3 -> 2 -> 1
    print(liste.taille())  # Doit afficher 3
    print(liste.estVide())  # Doit afficher False
    print(liste.rechercher(3))  # Doit afficher True

    print('')

    # Supprimez des noeuds
    liste.supprimer(2)
    print(liste)  # Doit afficher 3 -> 1
    print(liste.taille())  # Doit afficher 2
    print(liste.estVide())  # Doit afficher False
    print(liste.rechercher(2))  # Doit afficher False
    print(liste.rechercher(3))  # Doit afficher True
    print(liste.rechercher(1))  # Doit afficher True
    liste.supprimer(3)
    liste.supprimer(1)
    print(liste)  # Doit afficher
    print(liste.taille())  # Doit afficher 0
    print(liste.estVide())  # Doit afficher True
    print(liste.rechercher(3))  # Doit afficher False
