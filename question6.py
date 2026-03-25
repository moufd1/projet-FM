import matplotlib.pyplot as plt
from question1 import generer_profil_approbation
from question5 import phi_carre_approbations
def tracer_evolution_phi_carre(n, m):
    """
    Trace l'évolution de phi^2 en fonction du paramètre de polarisation p.
    """
    # on prépare nos listes pour les axes X (le paramètre p) et Y (le score phi^2)
    valeurs_p = []
    scores_phi_carre = []
    
    # on fait varier p de 0.0 à 1.0 (avec un pas de 0.05 par exemple pour avoir une belle courbe
    # la une petite astuce pour générer ces nombres car range() ne prend que des entierss
    pas = 20
    for i in range(pas + 1):
        p_actuel = i / pas
        
        # Pour lisser la courbe (car la génération a une part d'aléatoire), 
        # on peut calculer la moyenne sur quelques essais pour un même 'p'
        somme_scores = 0
        nb_essais = 10
        
        for _ in range(nb_essais):
            # On génère le profil (Méthode Q1)
            profil = generer_profil_approbation(n, m, p_actuel)
            # On calcule le score (Méthode Q5)
            score = phi_carre_approbations(profil)
            somme_scores += score
            
        moyenne_score = somme_scores / nb_essais
        
        # On ajoute les résultats aux listes pour le graphique
        valeurs_p.append(p_actuel)
        scores_phi_carre.append(moyenne_score)
        
    #on trace le graphique
    plt.figure(figsize=(8, 5))
    plt.plot(valeurs_p, scores_phi_carre, marker='o', linestyle='-', color='b')
    
    # on ajoute des titres et des légendes pour faire un beau rendu
    plt.title(f"Évolution de la polarisation $\\varphi^2$ (Approbations, n={n}, m={m})")
    plt.xlabel("Paramètre de polarisation p (Génération)")
    plt.ylabel("Score $\\varphi^2(p)$ calculé")
    plt.grid(True)
    
    # On force l'axe Y à aller de 0 à 1 pour bien voir le respect de l'Axiome 1
    plt.ylim(-0.05, 1.05) 
    plt.savefig('visualisation/evolution_phi2.png', dpi=300, bbox_inches='tight')
    plt.show()
    


#[-------Fin du graphe-----]


# --- POUR TESTER ---
tracer_evolution_phi_carre(50, 6) # Test avec 50 votantes et 6 candidates