import pandas as pd
import matplotlib.pyplot as plt

# Fichiers et infos associées
files = [
    ("shearTop_1bis_3014elem.csv", "géométrie initiale"),
    ("shear_fusiforme.csv", "anévrisme fusiforme")
]
"""
    ("shearTop_4_728elem.csv", "728 éléments"),
    # ("shearTop_2_2036elem.csv", "2036 éléments"),
    ("shearTop_1bis_3014elem.csv", "3014 éléments"),
    ("shearTop_5_5110elem.csv", "5110 éléments"),
    # ("shearTop_3_8250elem.csv", "8250 éléments"),
    ("shearTop_6_12132elem.csv", "12132 éléments")
"""

colors = ["blue", "green", "orange", "red",
          "purple", "black", "brown", "pink", "gray"]

# Tracé
plt.figure(figsize=(9, 6))

for (file, label), color in zip(files, colors):
    df = pd.read_csv(file, skipinitialspace=True)
    df.columns = df.columns.str.strip()
    df = df.sort_values(by="X Coord")  # Important pour des lignes propres
    plt.plot(df["X Coord"], df["Scalar"], label=label, color=color)


plt.xlabel("X Coord")
plt.ylabel("Tension pariétale (MPa)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("plot/comp_fusiforme.png", dpi=300)
plt.show()
