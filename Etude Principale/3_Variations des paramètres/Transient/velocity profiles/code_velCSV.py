import pandas as pd
import matplotlib.pyplot as plt

# Fichiers et infos associées
files = [
    ("vel_1_3014elem.csv", "3014 éléments"),
    ("vel_1bis_3014elem.csv", "3014 éléments"),
    ("vel_2_2036elem.csv", "2036 éléments"),
    ("vel_3_8250elem.csv", "8250 éléments"),
    ("vel_4_728elem.csv", "728 éléments"),
    ("vel_5_5110elem.csv", "5110 éléments"),
]

colors = ["blue", "green", "orange", "red", "purple", "black"]

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
