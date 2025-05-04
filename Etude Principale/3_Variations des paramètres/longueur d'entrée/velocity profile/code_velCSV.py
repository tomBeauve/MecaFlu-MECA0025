import pandas as pd
import matplotlib.pyplot as plt

# Fichiers et infos associées
files = [
    ("vel_5cm.csv", "5 cm"),
    ("vel_50cm.csv", "50 cm"),
    ("vel_1m.csv", "1 m"),
    ("vel_2m.csv", "2 m"),
    ("vel_2m7.csv", "2.70 m"),
    ("vel_3m.csv", "3 m"),


]

colors = ["blue", "green", "orange", "red",
          "purple", "black", "brown", "pink", "gray"]

# Tracé
plt.figure(figsize=(9, 6))

for (file, label), color in zip(files, colors):
    df = pd.read_csv(file, skipinitialspace=True)
    df.columns = df.columns.str.strip()
    df = df.sort_values(by="Y Coord")  # Important pour des lignes propres
    plt.plot(df["Magnitude"], df["Y Coord"], label=label, color=color)

plt.ylabel("Y Coord")
plt.xlabel("Magnitude de la vitesse (mm/s)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("vel_profiles_entryLength.png", dpi=300)  # Enregistrer la figure
plt.show()
