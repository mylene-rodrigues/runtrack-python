def wc(marche, hauteur):

   # marche = 40
  #  hauteur = 5
    nbreFoisJour = 5
    nbreJour = 7
    total = (((marche * hauteur)*nbreFoisJour)*nbreJour)/100
    print(total)
    str1 = "Pour " + str(marche) + " marches de " + str(hauteur) + "cm de hauteur, "
    str2 = "le gardien parcours " + str(total)  + " mètres par semaine."

    print(str1+ str2)
    
wc(40, 5)