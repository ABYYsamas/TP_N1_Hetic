import random
Maximun_Length = 4
Maximun_of_tries = 6
Authorized_color = ["rouge","violet","bleu""jaune"]
def Generator_Secret_Pass():
        colors= random.choices(Authorized_color,k=Maximun_Length)
        return colors
The_conbination= Generator_Secret_Pass()
print(f"la combinaison secréte est {The_conbination}") 
