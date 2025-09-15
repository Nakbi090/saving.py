import random

cartes = {'Deux': 2, 'Trois': 3, 'Quatre': 4, 'Cinq': 5, 'Six': 6, 'Sept': 7, 'Huit': 8, 'Neuf': 9,
          'Dix': 10, 'Valet': 10, 'Dame': 10, 'Roi': 10, 'As': 11}
couleurs = ['Coeur', 'Carreau', 'Trèfle', 'Pique']

MISE_FIXE = 10  

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur
    def __str__(self):
        return f"{self.valeur} de {self.couleur}"

class Blackjack:
    def __init__(self):
        self.solde_joueur = 1000
        self._nouveau_paquet()
        self.main_joueur = []
        self.main_croupier = []

    def _nouveau_paquet(self):
        self.cartes = [Carte(v, c) for v in cartes for c in couleurs]
        random.shuffle(self.cartes)

    def reset_manche(self):
        # reconstituer/reshuffler un paquet complet pour cette version simple
        self._nouveau_paquet()
        self.main_joueur = []
        self.main_croupier = []

    def distribuer_cartes(self):
        for _ in range(2):
            self.main_joueur.append(self.cartes.pop())
            self.main_croupier.append(self.cartes.pop())

    def afficher_main(self, joueur, reveler=False):
        if joueur == 'joueur':
            print("Main du joueur:")
            for carte in self.main_joueur:
                print(carte)
            print(f"Total: {self.valeur_main(self.main_joueur)}")
        elif joueur == 'croupier':
            print("Main du croupier:")
            if reveler:
                for carte in self.main_croupier:
                    print(carte)
                print(f"Total: {self.valeur_main(self.main_croupier)}")
            else:
                print(self.main_croupier[0])
                print("Carte cachée")

    def valeur_main(self, main):
        valeur = sum(cartes[carte.valeur] for carte in main)
        nb_as = sum(1 for carte in main if carte.valeur == 'As')
        while valeur > 21 and nb_as:
            valeur -= 10
            nb_as -= 1
        return valeur

    def tour_joueur(self):
        while True:
            self.afficher_main('joueur')
            choix = input("Voulez-vous prendre une carte (c) ou rester (r) ? ").strip().lower()
            if choix == 'c':
                self.main_joueur.append(self.cartes.pop())
                if self.valeur_main(self.main_joueur) > 21:
                    print("Vous avez dépassé 21. C'est perdu.")
                    return 'perdu'
            elif choix == 'r':
                return 'continuer'
            else:
                print("Choix invalide.")

    def tour_croupier(self):
        while self.valeur_main(self.main_croupier) < 17:
            self.main_croupier.append(self.cartes.pop())

    def resultat(self):
        self.afficher_main('joueur', reveler=True)
        self.afficher_main('croupier', reveler=True)

        valeur_joueur = self.valeur_main(self.main_joueur)
        valeur_croupier = self.valeur_main(self.main_croupier)

        if valeur_joueur > 21:
            return 'perdu'
        if valeur_croupier > 21:
            return 'gagné'
        if valeur_joueur > valeur_croupier:
            return 'gagné'
        if valeur_joueur < valeur_croupier:
            return 'perdu'
        return 'égalité'

    def gestion_argent(self, res):
        if res == 'gagné':
            self.solde_joueur += MISE_FIXE
            print(f"Vous avez gagné ! Solde: {self.solde_joueur} $")
        elif res == 'perdu':
            self.solde_joueur -= MISE_FIXE
            print(f"Vous avez perdu ! Solde: {self.solde_joueur} $")
        else:
            print(f"Égalité. Solde: {self.solde_joueur} $")

def jouer_blackjack():
    jeu = Blackjack()  
    while True:
        jeu.reset_manche()  
        jeu.distribuer_cartes()
        jeu.afficher_main('joueur')
        jeu.afficher_main('croupier')  

        if jeu.tour_joueur() != 'perdu':
            print("C'est au tour du croupier.")
            jeu.tour_croupier()
            resultat = jeu.resultat()
            jeu.gestion_argent(resultat)
            print(f"Résultat: {resultat}")

        rejouer = input("Voulez-vous rejouer ? (o/n) ").strip().lower()
        if rejouer != 'o':
            print("Merci d'avoir joué !")
            break

if __name__ == "__main__":
    jouer_blackjack()
