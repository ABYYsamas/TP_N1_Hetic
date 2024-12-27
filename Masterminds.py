import random
Maximun_Length = 4
Maximun_of_tries = 10
Authorized_color = ["rouge","violet","bleu","jaune"]
def Generator_Secret_Pass():
        colors= random.choices(Authorized_color,k=Maximun_Length)
        return colors
The_conbination= Generator_Secret_Pass()
print(f"la combinaison secréte est {The_conbination}") 

def anwsers_gamers():
    secret_code= input("entrez le code secret").split()
    for color in secret_code:
         if not color.isalpha():
            print("Erreur veuillez entrer uniquement des caractéres.")
            return anwsers_gamers() 
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
         
    print(f"{box_good_place} couleurs bien placée(s), {box_bad_place} couleurs mal placée(s).")
 
anwsers_gamers()

