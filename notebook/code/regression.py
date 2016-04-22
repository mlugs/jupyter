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

# Training- und Testset erstellen
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X[:,None], y, test_size=0.3, random_state=1)

# Estimatorklasse importieren, in diesem Fall SGDRegressor
from sklearn.linear_model import LinearRegression

# SGDRegressor erstellen
model = LinearRegression()

# Model an die Trainingsdaten trainieren
model.fit(X_train, y_train)

X_new = X_test
# Predictions berechnen
y_new = model.predict(X_new)

plt.scatter(X_train, y_train,  color='#fc4e2a', s=30)
plt.scatter(X_test, y_test,  color='#0c2c84', s=30)
plt.plot(X_new, y_new)
plt.legend(['Trainingsdaten', 'Testdaten'], fontsize=14, loc='lower right')
plt.title("Training- & Testdaten", fontsize=12)
plt.show()