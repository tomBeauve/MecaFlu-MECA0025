import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

EntryLengths = np.array([0.05, 0.5, 1, 2, 2.7, 3])
shearValues = np.array([1.075*10**(-2), 1.074*10**(-2), 1.073 *
                       10**(-2), 1.073*10**(-2), 1.073*10**(-2), 1.073*10**(-2)])

# Tracé
plt.figure(figsize=(9, 6))


plt.plot(EntryLengths, shearValues)


plt.xlabel("Longueur d'entrée (m)")
plt.ylabel("Pression pariétale max, face sup anévrisme (MPa)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("pressure_max_entryLength.png", dpi=300)
plt.show()
