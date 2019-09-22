#Exercice avec les "inputs"

#Determinez l'age d'un utilisateur en fonction de son année de naissance
birth_year = input('Année de naissance ? ')
#print(type(birth_year))
age = 2019 - int(birth_year) #Utilisation de int() pour convertir mon string(birth_year) en entier pour effectuer mon calcul.
print("Vous avez " + str(age) + " ans.") #Utilisation de str() pour convertir mon entier en string.