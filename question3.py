def calculDApprobations(p):
    """
    Calcule d_{ck, cl}(p) poour toutes les paires de candidates pour un profil d'approbations
    p : Liste de listes (le résultat de la fonction generer_profil)
 
    RETURN : Un dictionnaire {(k, l): distance_absolue}
    """
    #cas_err 
    if len(p)==0 :
        raise ValueError("pas de votantes")
    
    if len(pp[0])==0 :
        raise ValueError("pas de candidates")

    m = len(p[0]) #nb de candidates
    
    d={}
    # On parcourt toutes les paires possibles de candidates (k, l)
    for k in range(m):
        for l in (k+1,m):
            #compter combien de votantes preferent candidate k a candidate l
            #une votante prefere k a l si elle approuve k par 1 et n'approuve pas l par 0
            nb_kl=0
            nb_lk=0
            
            for vote in p:
                if vote[k]==1 and vote[l]==0:
                    nb_kl+=1
                elif vote[l]==1 and vote[k]==0:
                    nb_lk+=1                 
            d_kl=abs(nb_kl - nb_lk)
            d[(k,l)]=d_kl
    return d

def calculD_ordres_totaux(p):
    """
    Calcule d_{ck, cl}(p) pour un profil d'ordres totaux.
    p : Liste de listes où chaque liste est un classement (ex: [3, 0, 1, 2])
    
    RETURN : Un dictionnaire {(k, l): distance_absolue}
    """
    m = len(p[0]) #nb de candidates
    
    if len(p)==0 :
        raise ValueError("erreur pas de votantes")
    
    if len(p[0])==0 :
        raise ValueError("erreur pas de candidates")
    d={}
    
    for k in range(m):
        for l in range(k+1,m):
            n_kl = 0 
            n_lk = 0 
            
            for vote in p:
                # La candidate avec le plus petit index est la mieux classée
                # la méthode .index() trouve la position de la candidate dans la liste
                position_k = vote.index(k)
                position_l = vote.index(l)
                
                if position_k < position_l:
                    n_kl += 1
                else:
                    n_lk += 1 # Pas d'égalité possible dans un ordre total
                    
            d_kl = abs(n_kl - n_lk)
            d[(k, l)] = d_kl
    return d
    

# --- TEST ---
# m = 5 candidates
# mon_profil = generer_profil(4, 5, 0.5) 
# print("Profil généré :", mon_profil)
# print("Distances :", calculer_d_approbations(mon_profil, 5))

