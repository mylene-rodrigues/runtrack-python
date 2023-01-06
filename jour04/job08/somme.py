#Écrire un programme qui calcule la somme 
# de toutes les valeurs paires de la liste 
L = [8, 24, 27, 48, 2,16, 9, 7, 84, 91]
sommePair = 0

for i in L:
    if i%2 ==0:
        sommePair += i

print(sommePair)
