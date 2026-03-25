from question3 import calculDApprobations, calculD_ordres_totaux
def phi_carre_approbations(profil):
    """
    Calcule la mesure de polarisation phi^2 pour un profil d'approbations.
    profil : Liste de listes (le résultat de ta fonction generer_profil_approbation)
    
    RETURN : Un float entre 0 et 1 représentant le score de polarisation.
    """
    n = len(profil) 
    m = len(profil[0])
    if n == 0:
        raise ValueError("erreur aucune votantes")
    if m < 2:
        raise ValueError("Il faut au moins 2 candidates")
    combinaisons_m_2 = (m * (m - 1)) / 2
    denominateur = n * combinaisons_m_2
    
    distances = calculDApprobations(profil)
    
    somme_polarisation = 0
    for d_kl in distances.values():
        somme_polarisation += (n - d_kl)
        
    phi_2 = somme_polarisation / denominateur
    
    return float(phi_2)

def phi_carre_ordres_totaux(profil_ordres):
    """
    Calcule la mesure de polarisation phi^2 pour un profil d'ordres totaux.
    profil_ordres : Liste de listes (classements)
    
    RETURN : Un float entre 0 et 1 représentant le score de polarisation.
    """
    n = len(profil_ordres)
    m = len(profil_ordres[0])
    if n == 0:
        raise ValueError("erreur aucune votantes")
    if m < 2:
        raise ValueError("Il faut au moins 2 candidates")
    
    combinaisons_m_2 = (m * (m - 1)) / 2
    denominateur = n * combinaisons_m_2
    
    distances = calculD_ordres_totaux(profil_ordres)
    
    somme_polarisation = 0
    for d_kl in distances.values():
        somme_polarisation += (n - d_kl)
        
    phi_2 = somme_polarisation / denominateur
    
    return float(phi_2)