import numpy as np
import matplotlib.pyplot as plt
import csv

# Paramètres
dt = 0.01
t_max = 7
times = np.arange(4, t_max + dt, dt)

# Paramètres de la fonction gamma
A = 1 * 1200/0.2091042317418268
alpha = 0.7
beta = 0.33  # Durée caractéristique de l'impulsion
pulse_interval = 1.0  # Intervalle entre les impulsions (1 seconde)

vitesse = np.zeros_like(times)

# Ajouter une impulsion gamma à chaque début de seconde
for t0 in np.arange(0, t_max, pulse_interval):
    t_rel = times - t0
    # Appliquer la fonction gamma uniquement pour t_rel > 0
    mask = t_rel > 0
    vitesse[mask] += A * (t_rel[mask] ** alpha) * np.exp(-t_rel[mask] / beta)

print(max(vitesse))
print(min(vitesse))
print(np.mean(vitesse))

# Tracer le signal
plt.figure(figsize=(10, 4))
plt.plot(times, vitesse)
plt.xlabel("Temps (s)")
plt.ylabel("Vitesse du flux sanguin")
plt.grid(True)
plt.savefig("blood_vel_transient.png")
plt.show()

with open("temps_vitesse_impulsion.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["temps", "vitesse"])
    for t, v in zip(times, vitesse):
        writer.writerow([f"{t-4:.2f}", f"{v:.2f}"])
