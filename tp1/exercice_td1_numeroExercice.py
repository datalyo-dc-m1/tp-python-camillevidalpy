#exercice 0

a = 3
b = 10
c = a + b
b = a * c
a = c + 4

print ("la variable a vaut",a)
print ("la variable b vaut", b)
print ("la variable c vaut", c)



#exercice 1

x= int(input("Renseignez le nombre "))
i=x*x
print("le carré est", i)

#exercice 2
print("for")
i=0
for i in range(21):
    if(i%2==0): #si i est pair
        print(i, "est pair")#afficher i
    else:
        i= i+1
print()
print("while")
i=0
while i <=20:
    if(i%2==0): #si i est pair
        print(i, "est pair")#afficher i
        i=i+1
    else:
        i = i+1

#Exercice 3
n=int(input("Saisissez une valeur positive : "))
s=0
for x in range (n):
     if(x%2 != 0):
         print(x)
         s=s+x
     else:
         print("faux")
print("La somme des impairs est", s)


#Exercice 4

i=1
n=int(input("saisir une valeur de 1 à 100"))
if(n<1 or n>100):
    n = int(input("saisir une valeur de 1 à 100"))

while (i>=1 and i<=n):
    print(i)
    i=i+1

print("fin")

#Exercice 5

x= int(input("Renseignez le nombre: "))
print(x)
i= int(input("Renseignez le nombre:  "))
print(i)
n= input("Renseignez le symbole: ")
print(n)
if(n=='+'):
    n= x + i
    print("Le nombre vaut: ",n)
if(n=='-'):
    n= x - i
    print("Le nombre vaut: ",n)
if(n=='*'):
    n= x * i
    print("Le nombre vaut: ",n)
if(n=='/'):
    if(i==0):
        print("Opération impossible")
    else:
        print('Le résultat est', x / i)
if(n!='+', n!='-', n!='*', n!='/'):
    print("Opération inexistante")

