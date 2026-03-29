# Projet FM Clone

Projet Python de generation de profils de vote et de mesure de polarisation,
avec deux modeles de preferences :

- votes par approbation (0/1)
- ordres totaux (classements complets)

Le depot suit une logique par questions (Q1, Q2, ..., Q15).

## Prerequis

- Python 3.10+
- Environnement virtuel recommande

Dependances externes utilisees par le projet :

- matplotlib
- scipy

Installation :

```bash
pip install matplotlib scipy
```

## Organisation des fichiers

- question1.py : generation de profils d'approbation polarises.
- question2.py : generation de profils d'ordres totaux polarises.
- question3.py : calcul des distances pairwise entre candidates pour un profil.
- question5.py : calcul de phi^2 pour approbations et ordres totaux.
- question6.py : trace l'evolution moyenne de phi^2 (approbations) selon p.
- question8.py : distances de Hamming et de Spearman.
- question12.py : calcul de u1* (approbations et ordres totaux), avec algorithme hongrois.
- question13.py : approximation de u2*_tilde avec clustering k=2 et relances.
- question14.py : calcul de phi_dH et phi_dS.
- question15.py : comparaison de l'evolution de phi_dH et phi_dS.
- visualisation/ : dossier des figures generees.
- question9.pdf, question10.pdf, question11.pdf : enonces/supports PDF.

## Lancer les scripts principaux

Depuis la racine du projet :

```bash
python question6.py
```

Ce script :

- genere des profils d'approbation pour plusieurs valeurs de p,
- calcule une moyenne de phi^2,
- enregistre la figure dans visualisation/evolution_phi2.png,
- affiche la figure.

```bash
python question15.py
```

Ce script :

- genere des profils (approbation et ordre total) pour plusieurs valeurs de p,
- calcule les moyennes de phi_dH et phi_dS,
- affiche la courbe comparee.

## Remarques

- Les resultats changent d'une execution a l'autre (tirages aleatoires).
- Les modules sont relies entre eux (imports questionX vers questions precedentes), ce qui est normal dans cette structure par etapes.
- question15.py affiche le graphique mais ne l'enregistre pas automatiquement sur disque.
