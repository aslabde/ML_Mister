import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


# Load the CSV file into a DataFrame
df = pd.read_excel('Embarba_J33.xlsx')

df['Lag_1'] = df['POINTS'].shift(1)
df['Lag_2'] = df['POINTS'].shift(2)
df = df.reindex(columns=['GAME','POINTS', 'Lag_1', 'Lag_2'])

# Display the first few rows of the DataFrame
print(df.head())

y = df['POINTS']
X = df.fillna(0)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, shuffle=False)
model = LinearRegression()
model.fit(X_train, y_train)

y_fit = pd.DataFrame(model.predict(X_train), index=X_train.index, columns=y.columns)
y_pred = pd.DataFrame(model.predict(X_test), index=X_test.index, columns=y.columns)

'''
fig, ax = plt.subplots()
ax = sns.regplot(x='Lag_1', y='POINTS', data=df, ci=None, scatter_kws=dict(color='0.25'))
ax.set_aspect('equal')
ax.set_title('Lag Plot of Points');
plt.show()
'''