# Exercice all2_1 :	écrire une fonction qui retourne **la position** du plus grand élément d'une liste.
# ++ Fonction qui prend en entrée une liste de nombres positifs et qui retourne la deuxième plus grande valeur de la liste.
def second_biggest(l):
    top1 = 0 # La plus grande valeur trouvée jusqu'à présent 
    top2 = 0 # La deuxième plus grande valeur trouvée jusqu'à présent
    for e in l:
        if e>top1:
            top2 = top1
            top1 = e
        elif e>top2:
            top2 = e
    return top2
# Exemple : position_biggest([4,7,5,5,6]) retourne 1 car le plus grand est dans la case numéro 1

# En python, il existe une fonction appelée sum qui permet de calculer la somme d'une liste. Par exemple :
print('Test de la fonction sum...')
somme_test = sum([1,2,3,14,2,3,6,5,1,5])
print(somme_test) # Affiche 42 car 1+2+3+14+2+3+6+5+1+5 vaut 42
# Exercice all2_2 : comment fonctionne-t'elle ? (Écrire une fonction qui a le même comportement - sans utiliser `sum` bien entendu)

# Exercice all2_3 : écrire une fonction qui retourne la somme des valeurs positives d'une liste.

# Exercice all2_4 : En utilisant les deux fonctions précédentes, écrire une fonction qui retourne la somme des valeurs négatives d'une liste.

def f1(l):
    result=0
    for i in range(len(l)):
        if l[i]%2 == 0: # Si le contenu de la case numéro i est pair
            result += l[i] # J'ajoute ce contenu
    return result
    
def f2(l):
    result=0
    for i in range(len(l)):
        if i%2 == 0: # Si le NUMÉRO de la case numéro i est pair (autrement dit, si i est pair)
            result += l[i] # J'ajoute le numéro en question
    return result
    
liste = [0,1,2,3,4,5,6,7,8,9,10]
print('Avec f1 :',f1(liste))
print('Avec f2 :',f2(liste))

print('Avec f1 :',f1([15,16,16,103]))
print('Avec f2 :',f2([15,16,16,103]))

# Écrire une fonction f3 qui prend une liste en entrée
# et qui retourne la somme des numéros de cases des éléments pairs d'une liste
def f3(l):
    result = 0
    for i in range(len(l)):
        if l[i]%2 == 0: # Si le contenu de la case numéro i est pair
            result += i # On ajoute le numéro
    return result
            
liste_exemple = [3,7,2,20,-3,-8]
print('Avec f1 :',f1(liste_exemple))
print('Avec f2 :',f2(liste_exemple))
print('Avec f3 :',f3(liste_exemple))

# Fonction qui prend en entrée une liste et qui retourne le minimum de cette liste.
def return_min(l):
    best = l[0]
    for i in range(1,len(l)): # Le numéro 1, puis le numéro 2, ..., jusqu'au dernier (numéro taille-1)
        print('Je regarde la case numéro',i,"Meilleure valeur trouvée pour l'instant",best)
        if l[i] < best:
            best = l[i]
    return best
    
print(return_min([1,4,5,2,0,3,6]))
print(return_min([1,4,5,2,100,3,6]))
print(return_min([1,4,5,2,0,3,-6]))


# Fonction qui prend en entrée une liste et qui retourne le maximum de cette liste.
def return_max(l):
    best = l[0]
    for i in range(1,len(l)): # Le numéro 1, puis le numéro 2, ..., jusqu'au dernier (numéro taille-1)
        # print('Je regarde la case numéro',i,"Meilleure valeur trouvée pour l'instant",best)
        if l[i] > best:
            best = l[i]
    return best

print(return_max(l_test))


# Fonction qui prend en entrée une liste et un nombre et qui retourne le nombre de fois que ce nombre apparaît dans la liste.
def count(l,n):
    counter = 0
    for i in range(len(l)):
        if l[i] == n:
            counter = counter+1 # counter += 1
    return counter
    
print(        count(  [1,4,5,8,9,5,6,5,5,2]  ,  4  )        )
# print(...) -> Afficher quelque chose
# print(count(...,...)) -> Afficher le résultat de l'appel de count(...,...)
# print(count([1,4,5,8,9,5,6,5,5,2],4)) -> Afficher le résultat de l'appel de count([1,4,5,8,9,5,6,5,5,2],4)
print(count([1,4,5,8,9,5,6,5,5,2],5))


# Fonction qui prend en entrée une liste et un nombre et qui retourne True si le nombre existe dans la liste, False sinon.
def exist(l,n):
    for i in range(len(l)):
        if l[i]==n:
            return True
    # Une fois que la boucle est terminée (on n'est plus à l'intérieur car on n'est plus décalés sur la droite)
    return False

print(exist([1,4,5,8,9,5,6,5,5,2],4))
print(exist([1,4,5,8,9,5,6,5,5,2],8))
print(exist([1,4,5,8,9,5,6,5,5,2],7))

def exist2(l,n):
    # Écriture correcte, mais un peu maladroite
    if count(l,n) >= 1:
        return True
    else:
        return False
        

print(exist2([1,4,5,8,9,5,6,5,5,2],4))
print(exist2([1,4,5,8,9,5,6,5,5,2],8))
print(exist2([1,4,5,8,9,5,6,5,5,2],7))
        
def exist2_bis(l,n):
    return count(l,n) >= 1


print(exist2_bis([1,4,5,8,9,5,6,5,5,2],4))
print(exist2_bis([1,4,5,8,9,5,6,5,5,2],8))
print(exist2_bis([1,4,5,8,9,5,6,5,5,2],7))

def exist3(l,n):
    return n in l
        
print(exist3([1,4,5,8,9,5,6,5,5,2],4))
print(exist3([1,4,5,8,9,5,6,5,5,2],8))
print(exist3([1,4,5,8,9,5,6,5,5,2],7))