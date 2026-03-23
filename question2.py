import random

def generer_vote_ordre_total(m):
    vote = [i for i in range(1, m + 1)]
    random.shuffle(vote)
    return vote


def vote_oppose_ordre_total(vote):
    vote_oppose=[]
    for i in range(len(vote)-1,-1,-1):
        vote_oppose.append(vote[i])
    return vote_oppose

def generer_profil_ordre_total(n, m, niveau_polarisation):
    """
    n : nombre de votantes
    m : nombre de candidates
    niveau_polarisation : réel entre 0 et 1

    Retour :
    un profil de n bulletins de taille m
    """

    if (niveau_polarisation < 0) or (niveau_polarisation > 1):
        raise ValueError("Le niveau de polarisation doit etre compris entre 0 et 1")

    vote_a = generer_vote_ordre_total(m)
    vote_a_barre = vote_oppose_ordre_total(vote_a)

    profil = []

    proportion_vote_oppose = niveau_polarisation / 2

    nb_vote_oppose = round(n * proportion_vote_oppose)
    nb_vote_a = n - nb_vote_oppose

    # votes identiques
    for i in range(nb_vote_a):
        copie_vote_a = [x for x in vote_a]
        profil.append(copie_vote_a)

    # votes opposés
    for i in range(nb_vote_oppose):
        copie_vote_a_barre = [x for x in vote_a_barre]
        profil.append(copie_vote_a_barre)

    # mélange
    random.shuffle(profil)
    return profil