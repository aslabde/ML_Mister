import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor


# Load the CSV file into a DataFrame
df = pd.read_excel('Embarba_J34.xlsx')

df['Lag_1'] = df['POINTS'].shift(1)
df['Lag_2'] = df['POINTS'].shift(2)
df['Lag_3'] = df['POINTS'].shift(3)
df['Lag_4'] = df['POINTS'].shift(4)
df = df.reindex(columns=['GAME','POINTS', 'Lag_1', 'Lag_2', 'Lag_3', 'Lag_4'])

df = df.dropna(axis=0)

y = df.POINTS
X = df.reindex(columns=['GAME', 'Lag_1', 'Lag_2', 'Lag_3', 'Lag_4'])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, shuffle=False)

model = XGBRegressor()
model.fit(X_train, y_train)

y_fit = pd.DataFrame(model.predict(X_train))
y_pred = pd.DataFrame(model.predict(X_test))

print(X_test)
print(y_pred.round())

'''
fig, ax = plt.subplots()
ax = sns.regplot(x='Lag_1', y='POINTS', data=df, ci=None, scatter_kws=dict(color='0.25'))
ax.set_aspect('equal')
ax.set_title('Lag Plot of Points');
plt.show()
'''