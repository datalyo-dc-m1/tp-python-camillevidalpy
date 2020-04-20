t = [1, 2, 3, 4, 5]
a = t[0] + t[3]
b = t[-1]
c = t[3:]
a = a + t[-2]

print(type(t))
print(a)
print(type(b))
print(type(c))

#Exercice 2

liste = [1, 4, 1, 2, 1, 5, 3, 1, 12]
a = len(liste)
b = liste[0]
liste.append(0)
c = len(liste)
d = liste[-1]
print(liste)

liste.append(2)
liste.append(9)
liste.append(1)
print(liste)

print(a)
print(b)
print(c)
print(d)
# len(l) = longeur de la liste
#liste.append(i) = ajout de i à la liste

#liste.sort = trier une liste



liste = [1, 4, 1, 2, 1, 5, 3, 1, 12]

while liste.count(1) > 0:
  liste.remove(1)

print(liste)

liste.sort()

print(liste)


print("Maximum ", liste[0], "Minimum ", liste[len(liste)-1])
print("Minimum ", min(liste), "Maximum ", max(liste))
print("Somme", sum(liste))

#sum(liste) = sommes de la liste
#13. On ne peut pas faire la sommes avec une liste de caractères et un entier (str+ int)

# MOYENNES DE CLASSE

grades = [8, 12, 15, 6, 10, 19, 18, 7, 13, 15, 8, 15, 17, 13, 12, 15, 16, 9, 10, 3, 19, 20, 15]

# Ecart dans une liste entre max et min
print("Minimum", min(grades), "Maximum", max(grades))
ecart = max(grades)- min(grades)
print(ecart)

# Nombre de personnes
print("Il y a ",len(grades), "élèves")

# Inserer une note
grades.append(14)
print(grades)

# Modifier une note
grades[4]=13 #la 5eme note vaut 13 car on commence à 0.
print(grades)

# Calcul de la moyenne
moyenne = sum(grades) / len(grades)
print(moyenne)

# Calcul de la médiane
sorted_grades = sorted(grades)
nb_eleves = len(grades)
moitie = int(nb_eleves /2)
print(sorted_grades[moitie])

# Nombre de personne ayant validé et rattrapages

nb_personnes_passables = 0
nb_personnes_rattrapages = 0

for note in grades :
    if note >= 10:
        nb_personnes_passables = nb_personnes_passables + 1
    elif note>=8 :
        nb_personnes_rattrapages += 1
print (sorted_grades)
print (nb_personnes_passables)
print (nb_personnes_rattrapages)

# Exercice

awesome_couples = {
    'Batman': 'Robin',
    'Harley Quinn': 'Poison Ivy',
    'Iron man': 'War machine',
    'Phenix' : 'Cyclope',
    'Bob sponge square': 'Patrick'
    }

a = awesome_couples['Phenix']
bob = 'Bob sponge square'
b = (bob, 'Patrick starfish') in awesome_couples
awesome_couples['Ant man'] = 'the Wasp'
del awesome_couples['Bob sponge square']
c = bob in awesome_couples
d = awesome_couples.get(bob, 'unknown')
e = awesome_couples.get('Ant man', 'toto')

#questions
print(a)
print(b)
print(c)
print(d)
print(e)
