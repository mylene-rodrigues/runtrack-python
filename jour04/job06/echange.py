#Écrire un programme qui échange les valeurs de la première 
#et de la dernière case d’une liste quelconque non vide.

L = ["Fleur", "Fruit", "Four",]
a=L[0]
L[0] = L[-1]
print(L[0])
L[-1] = a

print(L)