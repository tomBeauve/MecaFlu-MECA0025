import csv
import math
# Paramètres
dt = 0.01  # Pas de temps
t_max = 3.0  # Durée totale
V0 = 300
Vf = 200

# Génération des données
times = [round(i * dt, 2) for i in range(int(t_max / dt) + 1)]
vitesse = []
"""
for t in times:
    if (0 <= t < 0.1) or (1.0 <= t < 1.1):
        vitesse.append(500)
    else:
        vitesse.append(0)
"""
for t in times:
    # Initialisation de la vitesse à 0
    vitesse.append(V0 + Vf*math.sin(2*math.pi * t))

# Écriture dans un fichier CSV
with open("temps_vitesse.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["temps", "vitesse"])
    for t, v in zip(times, vitesse):
        writer.writerow([f"{t:.2f}", f"{v:.2f}"])
