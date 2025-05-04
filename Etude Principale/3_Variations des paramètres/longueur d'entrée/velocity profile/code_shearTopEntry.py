import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

EntryLengths = np.array([0.05, 0.5, 1, 2, 2.7, 3])
shearValues = np.array([2.275*10**(-6), 7.376*10**(-7), 6.261 *
                       10**(-7), 5.612*10**(-7), 5.473*10**(-7), 5.442*10**(-7)])

# Tracé
plt.figure(figsize=(9, 6))


plt.plot(EntryLengths, shearValues)


plt.xlabel("Longueur d'entrée (m)")
plt.ylabel("Tension pariétale, entrée face supérieure (MPa)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("shear_entryTop_entryLength.png", dpi=300)
plt.show()
