def distance_hamming(bulletin1, bulletin2):
    """Calcule la distance de Hamming entre deux bulletins.

    La distance correspond au nombre de positions ou les deux listes
    ont des elements differents.

    Args:
        bulletin1: Premier bulletin (liste de candidates, choix, etc.).
        bulletin2: Deuxieme bulletin, de meme longueur que bulletin1.

    Returns:
        int: Nombre de positions differentes.

    Raises:
        ValueError: Si les deux bulletins n'ont pas la meme taille.
    """
    if len(bulletin1) != len(bulletin2):
        raise ValueError("Les bulletins doivent avoir la meme taille")
    m=len(bulletin1)
    return sum(1 for i in range(m) if bulletin1[i]!=bulletin2[i])

def construire_rangs(ordre):
    """Construit un dictionnaire candidate -> rang a partir d'un ordre total.

    Args:
        ordre: Liste ordonnee des candidates.

    Returns:
        dict: Dictionnaire associant chaque candidate a son rang (a partir de 1).
    """
    rangs = {}
    for i in range(len(ordre)):
        rangs[ordre[i]] = i + 1
    return rangs

def distance_spearman(ordre1, ordre2):
    """Calcule la distance de Spearman entre deux ordres totaux.

    Cette distance est la somme des ecarts absolus entre les rangs
    de chaque candidate dans les deux classements.

    Args:
        ordre1: Premier ordre total (permutation des candidates).
        ordre2: Deuxieme ordre total sur les memes candidates.

    Returns:
        int: Somme des differences absolues de rang.

    Raises:
        ValueError: Si les ordres n'ont pas la meme taille ou ne portent
            pas sur les memes candidates.
    """
    if len(ordre1) != len(ordre2):
        raise ValueError("Les ordres totaux doivent avoir la meme taille")
    if sorted(ordre1) != sorted(ordre2):
        raise ValueError("Les ordres totaux doivent etre des permutations des memes candidates")
    rang1 = construire_rangs(ordre1)
    rang2 = construire_rangs(ordre2)
    somme = 0
    for c in rang1:
        somme += abs(rang1[c] - rang2[c])
    return somme
