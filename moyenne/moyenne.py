# Écrire un programme qui affiche la moyenne 
# pondérée de trois nombres réels saisis au clavier
# traiterez les deux cas suivants :
# (a) les pondérations respectives sont fixées dans le programme ;
# (b) les pondérations respectives sont saisies dans le programme.

a = 5
b = 15
c = 12

print("la moyenne est de " + str('%.1f' % ((a+b+c)/3) ) )

a = input("Entrer le nombre numero 1 : ")
b = input("Entrer le nombre numero 2 : ")
c = input("Entrer le nombre numero 3 : ")

moyenne = ( int(a) + int(b) + int(c) ) /3

print("la moyenne est de " + str('%.1f' % moyenne ) )