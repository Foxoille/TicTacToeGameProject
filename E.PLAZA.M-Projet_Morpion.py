############################
# Eduardo Plaza Milhoranza #
# Arthur Rousseau - TG04   #
############################


#Projet Morpion :
#----------------


class Joueur:

    # Un joueur possède 2 attributs : un nom et un symbole ("X" ou "O").
    
    def __init__(self,nom,symbole):

        self.nom = nom
        self.symbole = symbole

       

    def __str__(self):
        
        return self.symbole 





class Case:

    def __init__(self,position):

        self.position = position
        self.valeur = None  #Case vide au début du jeu


    def __str__(self):


        if self.valeur == None : # Si la case est vide on renvoie la position
            return str(self.position)

        else :                   #Sinon on renvoie l'affichage de cette case.
            Affichage = "|"+ self.valeur + "|" 
            return Affichage 
     





class Grille:

    # Une Grille possède 1 attribut : un tableau de 9 Cases.


    def __init__(self,tab):

        self.tab = tab # Tab = liste avec les cases dedans


    def verif_case(self,position):
        # Permet de verifier si une Case a une certaine position est vide ou non. Si la case est vide, la méthode renvoie True et renvoie False sinon.
        # Position viens de la Class Case, et sers à nous repérer dans le tableau tab.
        # .valeur nous permet d'accéder à la valeur de la Case indiquée par position.
        return self.tab[position].valeur == None

    def joue(self,position,joueur):
        # Permet de changer la valeur d'une Case a une certaine position en "X" ou "O".
        # On vérifie si la case est vide, et si elle l'est on remplace le None par "X" ou "O"
        if self.verif_case(position):
            self.tab[position].valeur = joueur.symbole
        else :
            return False


    def verif_victoire(self,joueur):
        
        # Permet de verifier s'il y a un vainqueur horizontalement, verticalement ou diagonalement.

        # Condition de Victoire Verticale :
        # On pose la première condition, puis pour le passage d'un colone à l'autre on ajuste l'indice des cases en faisant +1 à chaque fois.
        for k in range(3):
            if self.tab[0+k].valeur == joueur.symbole and self.tab[3+k].valeur == joueur.symbole and self.tab[6+k].valeur == joueur.symbole :
                return True
    
        # Condition de Victoire Horizontale :
        # De même on pose la première condition, puis pour le passage d'une ligne à l'autre on ajuste l'indice des cases en faisant +3 à chaque fois.
        for k in range(0,9,3):
            if self.tab[0+k].valeur == joueur.symbole and self.tab[1+k].valeur == joueur.symbole and self.tab[2+k].valeur == joueur.symbole :
                return True
        
        # Condition de Victoire Diagonale :
        # On pose directement les deux conditions de victoire.
        if self.tab[0].valeur == joueur.symbole and self.tab[4].valeur == joueur.symbole and self.tab[8].valeur == joueur.symbole :
            return True

        elif self.tab[2].valeur == joueur.symbole and self.tab[4].valeur == joueur.symbole and self.tab[6].valeur == joueur.symbole :
            return True

        else :
            return False
        





    def __str__(self):

        # La méthode __str__ qui permet d'afficher une Grille sous la forme : | | | |
        #                                                                     | | | |
        #                                                                     | | | |
        
            affichage = ""
            for k in range(0,9,3):  # On parcour le tableau, dans la boucle k parcour une ligne et pose les caractères finaux : "|\n" 
                for i in range(3): # Dans la boucle i on vérifie si la case est vide où non et on l'affiche. 
                    if self.verif_case(i+k):
                        affichage += "| "              

                    else :
                        affichage += "|" + self.tab[i+k].valeur

                affichage += "|\n"

            return affichage




""" Jeu """

class Jeu:

    def __init__(self,listeJoueurs,grille):
        
        self.listeJoueurs = listeJoueurs
        self.grille = grille
        self.joueurActuel = 0
        self.cpt = 0

    def joueur_actuel(self):
        # Permet de renvoyer le Joueur correspondant à l'indice du joueur actuel.
        return self.listeJoueurs[self.joueurActuel]

        

    def joueur_suivant(self):
        # Permet de changer l'indice du joueur actuel (Si 0 passe à 1 et inversement).

        if self.joueurActuel == 0 :
            self.joueurActuel += 1

        else :
            self.joueurActuel -= 1

        return self.joueurActuel

    def tour(self):

        print(self.grille)
        demandeCase = input("Choisisez une case (de c1 à c9) : ")
        listeDeCases = ["c1","c2","c3","c4","c5","c6","c7","c8","c9"] # On crée une liste avec les differentes options de saisie
              
        if demandeCase in listeDeCases : # On vérifie si demande se trouve dans les options de saisie, si non on redemande en relançant la fonction.
            case = int(demandeCase[1]) - 1 # Si elle y est, met l'indice de la case choisie dans "case", pour avoir l'indice on converti le chiffre de la case
                                           # qui était en str en int et on soustrait 1. 
            if self.grille.joue(case,self.joueur_actuel()) is False: 
                print("Case déjà prise.")                            # On vérifie si la case est prise ou non, et si oui on refait la methode
                return self.tour()
            else :                                                   # SI tout vas bien on joue
                self.cpt += 1
                self.grille.joue(case,self.joueur_actuel())
    
        else :
            print("Donnez une case comme dans l'exemple ('c1','c2'...,'c9')") # Permet de relancer la fonction en cas de mauvaise saisie. 
            return self.tour()
        

    def jeu_entier(self):

        égalité = False # Variable qui permet de gérer l'égalité, initialisé à False logiquement
        
        while self.grille.verif_victoire(self.joueur_actuel()) is False and égalité is False : # Tant qu'on a ni victoire ni égalité on continue de joeur.
            self.tour() # On fait un tour
            self.grille.verif_victoire(self.joueur_actuel()) # On effectue une vérification
            
            if self.grille.verif_victoire(self.joueur_actuel()) : # Si il y a victoire on affiche la grilleet ainsi que le message
                print(self.grille)
                print("GG à toi", self.joueur_actuel().nom, "t'es trop fort.") 
    
            elif self.cpt == 9 :  #Permet de vérifier l'égalité, si 9 coups ont était joué sans victoire c'est égalité 
                égalité = True 
                print(self.grille)
                print("Domamge, égalité") # On affiche la grille et le message
        
            else:
                self.joueur_suivant() # Si il n'y a ni égalité ni victoire on passe au joueur suivant.
    
        

#------------------------------------
# Programme :
#------------------------------------


def jouer(): # Permet de gérer le lancement du jeu


    # Paramètres de base :
    #---------------------
    c1 = Case(1)
    c2 = Case(2)
    c3 = Case(3)
    c4 = Case(4)
    c5 = Case(5)
    c6 = Case(6)
    c7 = Case(7)
    c8 = Case(8)
    c9 = Case(9)
    grille = Grille([c1,c2,c3,c4,c5,c6,c7,c8,c9])

    # Info Joueurs :
    #---------------
    nom1 = input("Joueur 1, donnez votre pseudo : ")
    nom2 = input("Joueur 2, donnez votre pseudo : ")

    Joueur1 = Joueur(nom1,"X")
    Joueur2 = Joueur(nom2,"O")

    # initialisation du jeu :
    #------------------------
    
    morpion = Jeu([Joueur1,Joueur2],grille)
    morpion.jeu_entier()


    print("Voulez vous rejouer ? Si oui tapez 'oui', sinon tapez 'non'.")
    demande = input(": ")
    if demande == "oui" :
        return jouer()

# Lancement :
#------------

jouer()
