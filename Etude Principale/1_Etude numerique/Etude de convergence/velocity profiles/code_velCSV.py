import pandas as pd
import matplotlib.pyplot as plt

# Fichiers et infos associées
files = [
    ("vel_4_728elem.csv", "728 éléments"),
    # ("vel_2_2036elem.csv", "2036 éléments"),
    ("vel_1bis_3014elem.csv", "3014 éléments"),
    ("vel_5_5110elem.csv", "5110 éléments"),
    # ("vel_3_8250elem.csv", "8250 éléments"),
    ("vel_6_12132elem.csv", "12132 éléments")
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
plt.savefig("plot/mesh_vel_convergence.png", dpi=300)  # Enregistrer la figure
plt.show()
