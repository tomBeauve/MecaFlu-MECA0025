import pandas as pd
import matplotlib.pyplot as plt

# Fichiers et infos associées
files = [
    ("etude1_3014elem.csv", "3014 éléments"),
    ("etude2_7450elem.csv", "7450 éléments"),
    ("etude3_21450elem.csv", "21450 éléments"),
    ("etude4_30318elem.csv", "30318 éléments"),
    ("etude5_41356elem_noConv.csv", "41356 éléments")
]

colors = ["blue", "green", "orange", "red", "black"]

# Tracé
plt.figure(figsize=(10, 6))

for (file, label), color in zip(files, colors):
    df = pd.read_csv(file, skipinitialspace=True)
    df.columns = df.columns.str.strip()
    df = df.sort_values(by="Y Coord")  # Important pour des lignes propres
    plt.plot(df["Magnitude"], df["Y Coord"], label=label, color=color)

plt.ylabel("Y Coord")
plt.xlabel("Magnitude")
plt.title("Comparaison de la magnitude en fonction de Y pour différents maillages")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
