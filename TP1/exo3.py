class AuthHashTable:
    def __init__(self, size=11):
        self.size = size
        self.table = [None] * self.size

    def simple_hash(self, key):
        return sum(ord(c) for c in key) % self.size

    def insert(self, login, password):
        index = self.simple_hash(login)
        if self.table[index] is None:
            self.table[index] = [(login, password)]
        else:
            for pair in self.table[index]:
                if pair[0] == login:
                    return False  # Le login est déjà utilisé
            self.table[index].append((login, password))
        return True

    def authenticate(self, login, password):
        index = self.simple_hash(login)
        if self.table[index] is not None:
            for pair in self.table[index]:
                if pair[0] == login and pair[1] == password:
                    return True
        return False
def main():
    hash_table = AuthHashTable()
    while True:
        action = input("Voulez-vous créer un compte (c) ou vous authentifier (a) ? (c/a) ")
        if action.lower() == 'c':
            login = input("Entrez votre login : ")
            password = input("Entrez votre mot de passe : ")
            if hash_table.insert(login, password):
                print("Compte créé avec succès.")
            else:
                print("Erreur : ce login est déjà utilisé.")
        elif action.lower() == 'a':
            login = input("Entrez votre login : ")
            password = input("Entrez votre mot de passe : ")
            if hash_table.authenticate(login, password):
                print("Authentification réussie.")
                break  # Sortie de la boucle après l'authentification réussie
            else:
                print("Erreur : login ou mot de passe incorrect.")
        else:
            print("Action non reconnue.")


if __name__ == "__main__":
    main()