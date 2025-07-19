import pandas as pd
import matplotlib.pyplot as plt
fileName='Parabolic.csv'
dataframe = pd.read_csv(fileName)
dataframe = dataframe.iloc[1:].reset_index(drop=True)


print(dataframe.head())

#print(dataframe)


plt.figure (figsize=(8,6))
plt.scatter(dataframe['X'],dataframe['Y'],color='blue',alpha=0.5)
plt.title('Parabolic chart')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(False)
plt.tight_layout()
plt.show()

