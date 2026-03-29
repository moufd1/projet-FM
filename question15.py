"""
Question 15 - Evolution of phi_dH and phi_dS as a function of polarization.
Generates approval and total order profiles for increasing polarization levels,
computes the average phi_dH and phi_dS over multiple profiles, and plots the results.
"""

from question1 import generer_profil_approbation
from question2 import generer_profil_ordre_total
import matplotlib.pyplot as plt
from question14 import phi_dh, phi_ds

# Parameters
n = 20           
m = 8             
nbr_relances = 100  
nb_moyennes = 5  

polarisation = [i/20 for i in range(21)]  

phi_dh_values = []
phi_ds_values = []

for p in polarisation:
    dh_moy = 0
    ds_moy = 0
    for _ in range(nb_moyennes):
        prof_appro = generer_profil_approbation(n, m, p)
        prof_ordre = generer_profil_ordre_total(n, m, p)
        dh_moy += phi_dh(prof_appro, nbr_relances)
        ds_moy += phi_ds(prof_ordre, nbr_relances)
    phi_dh_values.append(dh_moy / nb_moyennes)
    phi_ds_values.append(ds_moy / nb_moyennes)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(polarisation, phi_dh_values, label='phi_dH', marker='o', color='blue')
plt.plot(polarisation, phi_ds_values, label='phi_dS', marker='o', color='orange')
plt.title('Evolution of phi_dH and phi_dS as a function of polarization')
plt.xlabel('Polarization (p)')
plt.ylabel('Value of phi_dH and phi_dS')
plt.ylim(0, 1.05)
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()