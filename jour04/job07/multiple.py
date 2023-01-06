#Écrire un programme qui compte le nombre de multiples de 3 présents dans la liste 
L = [8, 24,48,2,15]

multiple = 0

for i in L:
    if i % 3 == 0:
        multiple += 1
print(multiple)
