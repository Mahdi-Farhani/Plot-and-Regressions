import pandas as pd
import matplotlib.pyplot as plt
fileName='House-02.csv'
dataframe = pd.read_csv(fileName)
dataframe = dataframe.iloc[1:].reset_index(drop=True)


print(dataframe.head())


X = dataframe['M2']
Z= dataframe['Room']
Y = dataframe['Price']


figure= plt.figure (figsize=(8,6))
ax= figure.add_subplot(111, projection='3d')
ax.scatter(X, Z, Y,c=Z,cmap='viridis',s=50, alpha=0.5)
ax.set_title('Entekhab Housing Price')
ax.set_xlabel('Meter')
ax.set_zlabel('Room')
ax.set_ylabel('Price (100 Million Toman)')

plt.tight_layout()
plt.show()

