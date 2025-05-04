import pandas as pd
import matplotlib.pyplot as plt

# Fichiers et infos associées
files = [
    ("shearStressPrelim.csv", "")

]


colors = ["blue"]

# Tracé
plt.figure(figsize=(11, 6))

for (file, label), color in zip(files, colors):
    df = pd.read_csv(file, skipinitialspace=True)
    df.columns = df.columns.str.strip()
    df = df.sort_values(by="X Coord")  # Important pour des lignes propres
    plt.plot(df["X Coord"], df["Scalar"], label=label, color=color)


plt.xlabel("X Coord")
plt.ylabel("Tension pariétale (MPa)")
plt.grid(True)
plt.tight_layout()
plt.savefig("shearStress.png", dpi=300)
plt.show()
