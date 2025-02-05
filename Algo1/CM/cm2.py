def est_membre(liste, m):
    for elem in liste:
        if m == elem:
            return True
    return False

def est_majorant(liste, m):
    for elem in liste:
        if elem > m:
            return False
    return True


# TYPE PARAMETRE: liste d'entiers
# PRE-CONDITION: len(liste) > 0
# TYPE RETOUR: n est un entier
# POST-CONDITION: est_membre(liste, n) and est_majorant

def maximum(liste):
    assert len(liste) > 0
    m = 0
    for elem in liste:
        if elem > m:
            m = elem
    assert est_membre(liste, m) and est_membre(liste, m)
    return m