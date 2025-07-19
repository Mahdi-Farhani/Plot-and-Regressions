import pandas as pd
import matplotlib.pyplot as plt
#fileName='House-01.csv'
fileName='House-02.csv'
dataframe = pd.read_csv(fileName)
dataframe = dataframe.iloc[1:].reset_index(drop=True)


print(dataframe.head())

#print(dataframe)


plt.figure (figsize=(8,6))
plt.scatter(dataframe['M2'],dataframe['Price'],color='blue',alpha=0.5)
plt.title('Entekhab Housing Price')
plt.xlabel('Meter')
plt.ylabel('Price (100 Million Toman)')
plt.grid(True)
plt.tight_layout()
plt.show()

