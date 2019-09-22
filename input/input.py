#Exercice avec les "inputs"

#Déterminer le poids d'un utilisateur en pounds que l'on convertit ensuite en kg
weigh_lbs = input("Quel est votre poids en lbs ? ")
weigh_kg = float(weigh_lbs) * 0.45
print("votre poids en kg est " + str('%.1f' % weigh_kg))
#(%.Nf' % variable) permet d'afficher un nombre N de nombre après la virgule