#Écrire un programme qui affiche dans le terminal un rectangle avec des ‘-’ et des ‘|’ en

#fonction des paramètres d’entrées, (width, height), par exemple :
def draw_rectangle(width,height):
    tiret= "-"
    pipe= "|"
    vide=" "
    Nt = 1*width-2
    i = 2
    print(pipe + Nt*tiret +pipe)
    while i <height:
        print(pipe+vide*Nt+pipe)
        i+=1
    print(pipe + Nt*tiret+pipe)

draw_rectangle(10,3)