import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
# import seaborn as sns; sns.set()

a = 3.0
b = 1.0

# 200 zufällige Datenpunkte im Intervall [0, 30]
X = 30 * np.random.random(200)

# Geradenfunktion y = a * x + b mit additives Gaussrauschen hinzufuegen
y = a * X + b + np.random.normal(0, 5, 200) # y = 3x

# Ergebnis plotten
plt.plot(X,y, "o");