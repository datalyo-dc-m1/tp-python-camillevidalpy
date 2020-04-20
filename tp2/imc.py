def calcul_imc(masse,taille):
    return masse/(taille**2)
# 1.Identifier les données d'entrées et initialiser les variables correspondantes
# masse
# Taille
taille_saisie = int(input("Entrez votre taille en cm "))
print(taille_saisie)
masse_saisie = float(input("Entrez votre poids en kg "))
print(masse_saisie)

# 2.Calculer l'IMC
imc = masse_saisie / (taille_saisie / 100)**2
print(imc)

#3 Afficher la catégorie correspondant à l'IMC
if imc < 18.5:
    print("Vous êtes trop maigre.")
elif imc < 24.9 :
    print("Vous êtes normal.")
elif imc < 29.9 :
    print("Vous êtes surpoids")
elif imc < 40.0 :
    print ("Vous êtes en obésité massive")
else :
    print("Vous avez en obéssité morbide")
