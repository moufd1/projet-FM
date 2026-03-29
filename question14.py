from question13 import *
from question12 import *

def phi_dh(profil,nbr_relances):
    """
    Computes phi_dH(p) for approval votes.
    Measures polarization as the normalized difference between u1* and u2*_tilde.

    profil: list of n approval ballots
    nbr_relances: number of restarts for the k-means algorithm

    Returns: phi_dH(p) in [0, 1]
    """
    
    # vérifier que le profil est valide
    if len(profil)==0:
        raise ValueError("erreur aucune votante trouvée")
    if len(profil[0])==0:
        raise ValueError("erreur aucune candidate trouvée")
    
    # on récupère via les questions precédentes les valeurs de u1 étoile et u2 étoile (approbations)
    u1_étoile=u1_étoile_approbations(profil)
    u2_étoile=u2_tilde_approbation(profil,nbr_relances)
    
    # nbr de votantes et de candidates
    n=len(profil)
    m=len(profil[0])
     # calcule avec la formule de l'énoncé
    return 2*(u1_étoile-u2_étoile)/(n*m)


def phi_ds(profil,nbr_relances):
    """
    Computes phi_dS(p) for total order votes.
    Measures polarization as the normalized difference between u1* and u2*_tilde.

    profil: list of n total orders
    nbr_relances: number of restarts for the k-means algorithm

    Returns: phi_dS(p) in [0, 1]
    """
    
    # vérifier que le profil est valide
    if len(profil)==0:
        raise ValueError("erreur aucune votante trouvée")
    if len(profil[0])==0:
        raise ValueError("erreur aucune candidate trouvée")
    # on récupère via les questions precédentes les valeurs  de u1 étoile et u2 étoile (ordre_totaux)
    u1_étoile=u1_étoile_ordres_totaux(profil)
    u2_étoile=u2_tilde_ordres_totaux(profil,nbr_relances)
        # nbr de votantes et de candidates
    n=len(profil)
    m=len(profil[0])
    
    
    valeur = 4 * (u1_étoile - u2_étoile) / (n * m * m)
    
    
    return valeur

      