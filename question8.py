def distance_hamming(bulletin1, bulletin2):
    if len(bulletin1) != len(bulletin2):
        raise ValueError("Les bulletins doivent avoir la meme taille")
    m=len(bulletin1)
    return sum(1 for i in range(m) if bulletin1[i]!=bulletin2[i])

def construire_rangs(ordre):
    rangs = {}
    for i in range(len(ordre)):
        rangs[ordre[i]] = i + 1
    return rangs

def distance_spearman(ordre1, ordre2):
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
