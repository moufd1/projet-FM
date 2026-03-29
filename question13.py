import random
from question8 import *
from question12 import u1_bulletin_consensus_approbation,matrice_couts
from scipy.optimize import linear_sum_assignment



def u2_tilde_approbation(profil,nbr_relances):
    
    """
    Computes u2*_tilde(p) for approval votes.
    Uses the k-means algorithm with k=2 to find two consensus clusters.
    
    profil: list of n approval ballots, each ballot is a list of 0s and 1s
    nbr_relances: number of times the algorithm is restarted
    
    Returns: estimated optimal value u2*_tilde(p) = minimum sum of Hamming distances with 2 clusters
    """
   # verifier que le prfil est valide
    if len(profil)==0:
        raise ValueError("erreur aucune votante trouvée")
    if len(profil[0])==0:
        raise ValueError("erreur aucune candidate trouvée")
    
    meilleure_sol=float('inf')
     
    for _ in range(nbr_relances):
         # nos deux bulletins de concensus sont deux centroides initialisés aléatoirement
         bull_cons1=[random.randint(0,1) for _ in range(len(profil[0]))]
         bull_cons2=[random.randint(0,1) for _ in range(len(profil[0]))]
         
         
         # on evite de prendre le meme bulletin de concensus deux fois
         while bull_cons1==bull_cons2:
                bull_cons2=[random.randint(0,1) for _ in range(len(profil[0]))]
                
        
         change=True
         
         while change:
             change=False
              
             cluster1=[]
             cluster2=[]
             
          #  affectation de chaque bulletin au cluster dont le bulletin de concensus est le plus proche selon la distance de hamming
             for bulletin in profil :
              if distance_hamming(bulletin,bull_cons1) <= distance_hamming(bulletin,bull_cons2):
                    cluster1.append(bulletin)
              else:
                    cluster2.append(bulletin)
        
           # pour chaque cluster on calcule son bull_cons ? VERIFIER SI y'a un changement ou pas
             if len(cluster1)>0:
               new_bull_cons1=u1_bulletin_consensus_approbation(cluster1)
               if new_bull_cons1 != bull_cons1:
                    bull_cons1=new_bull_cons1
                    change=True
                    
             if len(cluster2)>0:
               new_bull_cons2=u1_bulletin_consensus_approbation(cluster2)
               if new_bull_cons2 != bull_cons2:
                    bull_cons2=new_bull_cons2
                    change=True

        # après la convergence on calcule la somme des distances de hamming entre les bulletins de chaque cluster et leur bulletin de concensus respectif

         Somme_distances=0
         for bulletin in cluster1:
          Somme_distances+=distance_hamming(bulletin,bull_cons1)
        
         for bulletin in cluster2:
          Somme_distances+=distance_hamming(bulletin,bull_cons2)
              
         # on garde la meilleure solution trouvée après nbr_relances
         if Somme_distances < meilleure_sol:
          meilleure_sol=Somme_distances
          
    return meilleure_sol







def u2_tilde_approbation(profil,nbr_relances):
    
    """
    Computes u2*_tilde(p) for approval votes.
    Uses the k-means algorithm with k=2 to find two consensus clusters.
    
    profil: list of n approval ballots, each ballot is a list of 0s and 1s
    nbr_relances: number of times the algorithm is restarted
    
    Returns: estimated optimal value u2*_tilde(p) = minimum sum of Hamming distances with 2 clusters
    """
   # verifier que le prfil est valide
    if len(profil)==0:
        raise ValueError("erreur aucune votante trouvée")
    if len(profil[0])==0:
        raise ValueError("erreur aucune candidate trouvée")
    
    meilleure_sol=float('inf')
     
    for _ in range(nbr_relances):
         # nos deux bulletins de concensus sont deux centroides initialisés aléatoirement
         bull_cons1=[random.randint(0,1) for _ in range(len(profil[0]))]
         bull_cons2=[random.randint(0,1) for _ in range(len(profil[0]))]
         
         
         # on evite de prendre le meme bulletin de concensus deux fois
         while bull_cons1==bull_cons2:
                bull_cons2=[random.randint(0,1) for _ in range(len(profil[0]))]
                
        
         change=True
         
         while change:
             change=False
              
             cluster1=[]
             cluster2=[]
             
          #  affectation de chaque bulletin au cluster dont le bulletin de concensus est le plus proche selon la distance de hamming
             for bulletin in profil :
              if distance_hamming(bulletin,bull_cons1) <= distance_hamming(bulletin,bull_cons2):
                    cluster1.append(bulletin)
              else:
                    cluster2.append(bulletin)
        
           # pour chaque cluster on calcule son bull_cons ? VERIFIER SI y'a un changement ou pas
             if len(cluster1)>0:
               new_bull_cons1=u1_bulletin_consensus_approbation(cluster1)
               if new_bull_cons1 != bull_cons1:
                    bull_cons1=new_bull_cons1
                    change=True
                    
             if len(cluster2)>0:
               new_bull_cons2=u1_bulletin_consensus_approbation(cluster2)
               if new_bull_cons2 != bull_cons2:
                    bull_cons2=new_bull_cons2
                    change=True

        # après la convergence on calcule la somme des distances de hamming entre les bulletins de chaque cluster et leur bulletin de concensus respectif

         Somme_distances=0
         for bulletin in cluster1:
          Somme_distances+=distance_hamming(bulletin,bull_cons1)
        
         for bulletin in cluster2:
          Somme_distances+=distance_hamming(bulletin,bull_cons2)
              
         # on garde la meilleure solution trouvée après nbr_relances
         if Somme_distances < meilleure_sol:
          meilleure_sol=Somme_distances
          
    return meilleure_sol




def optimal_centroide(cluster, m):
    """
    Finds the optimal total order for a cluster (same method as u*1).
    Uses the Hungarian algorithm (from question 12) to solve the minimum weight perfect matching.
    
    cluster: list of total orders
    m: number of candidates
    
    Returns: optimal centroid as a list of ranks from 1 to m
    """
    
    couts,ligne_ind,col_ind=matrice_couts(cluster)   
    #centroide[i] = rang de la candidate i
    centroide = [0] * m
    
    for i in range(len(ligne_ind)):
        rang_idx = ligne_ind[i]
        candidate_idx = col_ind[i]
        centroide[candidate_idx] = rang_idx + 1 
    
    return centroide
   

def u2_tilde_ordres_totaux(profil, nbr_relances):
    """
    Computes u2*_tilde(p) for total order votes.
    Uses the k-means algorithm with k=2 to find two consensus clusters.
    
    profil: list of n total orders, each order is a list of m ranks (order[i] = rank of candidate i, from 1 to m)
    nbr_relances: number of times the algorithm is restarted
    
    Returns: estimated optimal value u2*_tilde(p) = minimum sum of Spearman distances with 2 clusters
    """
   
    #verifier que le profl est valide
    if len(profil) == 0:
        raise ValueError("erreur aucune votantes")
    
    if len(profil[0]) == 0:
        raise ValueError("erreur aucune candidates")
    
    # nbr de votantes et candiadtes
    n = len(profil)  
    m = len(profil[0])  
    
    meilleur_res = float('inf')
    
    #on relance l'algo plusierus foir
    for _ in range(nbr_relances):
        
        ordre_base = list(range(1, m + 1))
        random.shuffle(ordre_base) 
        centroide1 = ordre_base.copy()
        
        ordre_base2 = list(range(1, m + 1))
        random.shuffle(ordre_base2)
        centroide2 = ordre_base2.copy()
        
        change = True
        while change:
            
            change = False
            
            
            cluster1 = []
            cluster2 = []
            
            # on assigne chaque ordre du profil à un cluster selon la distance de spearman àchaque cluster
            for ordre in profil:
                
                if distance_spearman(ordre, centroide1) <=distance_spearman(ordre, centroide2) :
                    cluster1.append(ordre)
                else:
                    cluster2.append(ordre)
            
         
            if len(cluster1) > 0:
                
                new_centroide1 = optimal_centroide(cluster1, m)
                if new_centroide1 != centroide1:

                    centroide1 = new_centroide1
                    change = True
            
            if len(cluster2) > 0:
                
                new_centroide2 = optimal_centroide(cluster2, m)
                
                if new_centroide2 != centroide2:
                    centroide2 = new_centroide2
                    change = True
        
        
        somme = 0
        
        for ordre in cluster1:
            somme += distance_spearman(ordre, centroide1)
        
        for ordre in cluster2:
            somme += distance_spearman(ordre, centroide2)
        
        
        if somme < meilleur_res:
            meilleur_res = somme
    
    return meilleur_res


