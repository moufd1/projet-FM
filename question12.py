from question8 import distance_hamming,distance_spearman
from scipy.optimize import linear_sum_assignment



def u1_bulletin_consensus_approbation(profil):
    
    """
    Computes the consensus ballot for approval votes using majority rule.
    For each position, assigns 1 if the majority approves, 0 otherwise.
    In case of a tie, assigns 1.

    profil: list of n approval ballots, each ballot is a list of 0s and 1s

    Returns: consensus ballot as a list of 0s and 1s
    """

    #vérifier que le profil est valide
    if len(profil)==0:
        raise ValueError("erreur aucune votante trouvée")
    if len(profil[0])==0:
        raise ValueError("erreur aucune candidate trouvée")

    
    
    bulletin_cons = []
    for i in range(len(profil[0])):
        nbr_uns = 0
        for bulletin in profil:
            if bulletin[i] == 1:
                nbr_uns += 1
        nbr_zeros = len(profil) - nbr_uns
        if nbr_uns >= nbr_zeros:
            bulletin_cons.append(1)
        else:
            bulletin_cons.append(0)

    return bulletin_cons


def u1_étoile_approbations(profil):
    """
    Computes u1*(p) for approval votes.
    Finds the consensus ballot that minimizes the sum of Hamming distances.

    profil: list of n approval ballots

    Returns: optimal value u1*(p) = minimum sum of Hamming distances to the consensus
    """
    bulletin_cons = u1_bulletin_consensus_approbation(profil)
    some=sum(distance_hamming(bulletin,bulletin_cons) for bulletin in profil)
    
    return some


def matrice_couts(profil):
    
      """
    Builds the cost matrix for the Hungarian algorithm.
    couts[i][j] = cost of assigning rank i+1 to candidate j.

    profil: list of n total orders

    Returns: (couts, ligne_ind, col_ind) — cost matrix and optimal assignment indices
    """

      m = len(profil[0])

    # Construction de la matrice de coût
    # couts[i][j] = coût d'assigner le rang i+1 à la candidate j
      couts = []
      for i in range(1, m + 1):
         ligne_couts = []
         for j in range(m):
            cout = sum(abs(i - bulletin[j]) for bulletin in profil)
            ligne_couts.append(cout)
         couts.append(ligne_couts)

    # Résolution par l'algorithme hongrois
      ligne_ind, col_ind = linear_sum_assignment(couts)
      return couts,ligne_ind,col_ind

def u1_étoile_ordres_totaux(profil):
    """
    Computes u1*(p) for total order votes.
    Uses the Hungarian algorithm to find the optimal consensus permutation.

    profil: list of n total orders, each order is a list of m ranks (from 1 to m)

    Returns: optimal value u1*(p) = minimum sum of Spearman distances to the consensus
    """
    if len(profil) == 0:
        raise ValueError("erreur aucune votante trouvée")
    if len(profil[0]) == 0:
        raise ValueError("erreur aucune candidate trouvée")
    
    couts,ligne_ind,col_ind=matrice_couts(profil)
    
    sol_opt = sum(couts[ligne_ind[i]][col_ind[i]] for i in range(len(ligne_ind)))
    
    return sol_opt

    


