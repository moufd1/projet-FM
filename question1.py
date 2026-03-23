import random

def generer_vote_approbation(m, taux_approbation=0.5):
    vote = []
    for i in range(m):
        if random.random() < taux_approbation:
            vote.append(1)
        else:
            vote.append(0)
    return vote


def vote_oppose(vote):
    return [1 - x for x in vote]


def generer_profil_approbation(n, m, niveau_polarisation):
    """
    n : nombre de votantes
    m : nombre de candidates
    niveau_polarisation : réel entre 0 et 1

    Retour :
    un profil de n bulletins de taille m

    """

    if (niveau_polarisation < 0) or (niveau_polarisation > 1):
        raise ValueError("Le niveau de polarisation doit etre compris entre 0 et 1")

    vote_a = generer_vote_approbation(m)
    vote_a_barre = vote_oppose(vote_a)

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
        copie_vote_a_barre= [x for x in vote_a_barre]
        profil.append(copie_vote_a_barre)

    # mélange
    random.shuffle(profil)
    return profil
