import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

EntryLengths = np.array([0.05, 0.5, 1, 2, 2.7, 3])
shearValues = np.array([4.597*10**(-6), 3.784*10**(-6), 3.601 *
                       10**(-6), 3.485*10**(-6), 3.462*10**(-6), 3.456*10**(-6)])

# Tracé
plt.figure(figsize=(9, 6))


plt.plot(EntryLengths, shearValues)


plt.xlabel("Longueur d'entrée (m)")
plt.ylabel("Tension pariétale max, face sup anévrisme (MPa)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("shear_max_entryLength.png", dpi=300)
plt.show()
