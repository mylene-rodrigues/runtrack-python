#Jules César, général et stratège romain, a été le premier militaire officiel à chiffrer ses
#messages. Sa méthode était assez simple : il décalait les lettres de 3 rangs dans
#l'alphabet.
#Créer une fonction à laquelle on DONNE un message et un décalage,
#  et la fonction renvoie alors le message décalé dans l'alphabet. Il 
# faudra gérer le dépassement ('z'
#décalé vers la droite revient sur 'a', et 'a' décalé vers la gauche revient sur 'z').

#creer une liste: 
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

for i in range(len(alphabet)):
    alphabet.append(alphabet[i])

message = input("Entrez votre message:")
clef = int(input("Entrez votre clef:"))

def chiffrage_lettres(lettre, alphabet, clef):
    for i in range(len(alphabet)):
        if lettre == ' ':
            return ' '
        elif alphabet[i] == lettre:
            return str(alphabet[i+clef])
    return '?'

message_chiffré = str()

for lettre in message:
    message_chiffré += chiffrage_lettres(lettre, alphabet, clef)

print(message_chiffré)



    