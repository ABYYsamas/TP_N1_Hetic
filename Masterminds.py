import random
Maximun_Length = 4
Maximun_of_tries = 6
Authorized_color = ["rouge","violet","bleu","jaune"]
def Generator_Secret_Pass():
        colors= random.choices(Authorized_color,k=Maximun_Length)
        return colors
The_conbination= Generator_Secret_Pass()
print(f"la combinaison secréte est {The_conbination}") 
The_conbination= Generator_Secret_Pass()
print(f"la combinaison secréte est {The_conbination}") 
def anwsers_gamers():
    secret_code= input("entrez le code secret").split()
    if len(secret_code) != Maximun_Length:
       print("erreur le code fait plus de 4 couleurs")
    else:
        return secret_code
anwsers_gamers()
