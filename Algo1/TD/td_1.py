#####################################################################
# EXERCICE 1
#####################################################################
def produit_element(liste):
    produit = 1

    for elem in liste:
        produit = produit * elem
    return produit

#   cas       | parametre       | return
#   1         |    []           |   1
# singleton   |    [50]         |   50
#  nb positif |   [1,2,3]       |  6
# nb negatif  |   [-1,-1,-2,-3] |  6
#  melange    |  [-1,1,-2,-3,2] |  -12
# zéro        |  [1,50,10,0]    |  0


def test_produit_element():
    print("Début tests unitaire")
    assert produit_element([]) == 1, "assert 1"
    assert produit_element([50]) == 50, "assert 2"
    assert produit_element([1,2,3]) == 6, "assert 3" 
    assert produit_element([-1,-1,-2,-3]) == 6, "assert 4" 
    assert produit_element([-1,1,-2,-3,2]) == -12, "assert 5"
    assert produit_element([10,50, 1, 0]) == 0, "assert 6"
    print("ok")
###################################################################
###################################################################


#####################################################################
# EXERCICE 2
#####################################################################

# condition   |   cas       | parametre       | return
#             |   zero      |    0            |   1
#    false    | 0 iteration |    9            |   1
#    false    | 1 iteration |    19           |   2
#    false    | 4 iteration |   12345         |   5
#    false    | >10 iterati | 12345678910     |  11
#    true     | 0 iteration |   -9            |   1
#    true     | 1 iteration |    -19          |   2
#    true     | 4 iteration |    -12345       |   5
#    true     | >10 iterati | -12345678910    |

#####################################################################
# EXERCICE 3
#####################################################################

#    cas      |  liste      |   valeur        | return
#  liste vide |   []        |    40           |   [40]
#   en debut  | [-4,-2,3,7] |    -5           | [-5,-4,-2,3,7]
#  vers debut | [-4,-2,3,7] |    -3           | [-5,-4,-2,3,7]
#  vers fin   | [-4,-2,3,7] |     6           | [-4,2,3,6,7]
#   en fin    | [-4,-2,3,7] |     9           | [-4,-2,3,6,7]

liste = [-4,-2,3,7]
assert insertion_ordonnee(liste, 9) == [-4,2,3,7,9]
assert liste == [-4,2,3,7]
# 2)
liste = [-4,-2,3,7]
assert insertion_ordonnee(liste, 9) == None
assert liste == [-4,-2,3,7,9]
###################################################################
###################################################################

#####################################################################
# EXERCICE 4
#####################################################################
def test_valeurs_inferieure():
    print("Test unittaire")
    assert nb_valeurs_inferieures([], 100) == 0
    assert nb_valeurs_inferieures([-3,2,8,1,7,11,3,4], -4) == 0 
    assert nb_valeurs_inferieures([-3,2,8,1,7,11,3,4], 0) == 1 
    assert nb_valeurs_inferieures([-3,2,8,1,7,11,3,4], 3) == 4 
    assert nb_valeurs_inferieures([-3,2,8,1,7,11,3,4], 11) == 8 
    assert nb_valeurs_inferieures([-3,2,8,1,7,11,3,4], 8) == 7 
    print("ok")

#####################################################################
# EXERCICE 5
#####################################################################
def test_indices_valeurs():
    print("Test unnittaire")
    assert indices_valeurs([], 3) == []
    assert indices_valeurs([11,23,67,23,23,83,23,10], 23) == [1,3,4,6]
    assert indices_valeurs([11,23,67,23,23,83,23,10], 11) == [0]
    assert indices_valeurs([11,23,67,23,23,83,23,10], 12) == []
    assert indices_valeurs([11,23,67,23,23,83,23,10], 10) == [7]
    assert indices_valeurs([11,23,67,23,23,83,23,10], 83) == [5]

#####################################################################
# EXERCICE 6
#####################################################################
def puissance(a, b):
    #Type des params: a et b sont des entiers(int)
    #Type de retour: p est un entier(int)
    #Pré condition: a >= 0 et b >=0
    #Post condition: p == a**b 
    assert, "Pré condition"
    assert, "Post condition"

def log2_entier(n):
    #Type des params: n est un enier(int)
    #Type de retour: k est un entier(int)
    #Pré condition: n > 0
    #Post condition: k >= 0 et 2**k <=n < 2**(k+1)
    assert, "Pré condition"
    assert, "Post condition"

#####################################################################
# EXERCICE 7
#####################################################################
def est_croissante(liste):
    for i in range(1, len(liste)):
        if liste[i - 1] > liste[i]:
            return False
    return True

def insertion_ordonnee(liste, n):
    assert est_croissante(liste), 'Pré condition'

#####################################################################
# EXERCICE 8
#####################################################################
def fnct(n):
    assert n>=0, "Pré condition"
    assert a >=0 and a**2<=n<(a+1)**22, "Post condition"