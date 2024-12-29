import random

Maximun_Length = 4
Authorized_color = ["rouge", "violet", "bleu", "jaune"]

def Generator_Secret_Pass():
    colors = random.choices(Authorized_color, k=Maximun_Length)
    return colors


def instruction ():
   print("\033[1mBienvenue dans le jeu Mastermind.\033[0m")
   print("Votre mission si vous l'acceptez est de trouver \033[1mla combinaison secréte qui contient 4 couleurs\033[0m: 🔴 🟡 🟣 🔵. ")
   print("Mais attention pour relever cet objectif \033[1mtu as  droit à seulement 10 essais \033")
   print("Bonne chance nous comptons sur toi !")
    
def anwsers_gamers(The_conbination):
    secret_code= input("entrez le code secret:").split()
    for color in secret_code:
         if not color.isalpha():
            print("Erreur veuillez entrer uniquement des caractéres.")
    if len(secret_code) != Maximun_Length:
       print("erreur le code fait plus de 4 couleurs")
    elif secret_code== The_conbination:
         print ("bravo tu a trouvé le code secret")
    else:
        print ("ce n'est pas le bon code")
        solution_verif (secret_code, The_conbination)


def solution_verif (secret_code, The_conbination):
    box_good_place=0
    box_bad_place=0
    already_check=[]
    for i in range (len(The_conbination)):
        if secret_code [i]== The_conbination[i]:
         box_good_place += 1
         already_check.append(i)
    for i in range (len(The_conbination)):
        if i not in already_check and The_conbination[i] in secret_code:
         if secret_code.count(The_conbination[i]) > already_check.count(i):
            box_bad_place += 1
        already_check.append(i)
         
    print(f"{box_good_place} couleurs bien placée(s)✅, {box_bad_place} couleurs mal placée(s)❌.")
 

def Main_game():
    instruction()
    The_conbination = Generator_Secret_Pass()
    number_of_tries = 0
    Maximun_of_tries = 10
    game_won = False
    while number_of_tries < Maximun_of_tries:
        if anwsers_gamers(The_conbination):
            game_won = True
            break
        number_of_tries += 1
    if not game_won:
        print(f"\033[1méchec de la mission, retente ta chance ! le code était {The_conbination} \033")

Main_game()