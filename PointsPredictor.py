import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import time
import json
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt


dataSetFile = "Dataset_v1_20231026-190343"
#file = open(dataSetFile,'r')
initialData=pd.read_json(dataSetFile)
data = initialData.T
#data.info()
#print(data.corr())

#Labelin position as proximity array
data['points'] = data['points'].replace(np.nan, 0) 
#data['position'] = data['position'].replace(1, [1,0,0,0])  #GK
#data['position'] = data['position'].replace(2, [0,1,0,0])  #DF
#data['position'] = data['position'].replace(3, [0,0,1,0])  #MF
#data['position'] = data['position'].replace(4, [0,0,0,1])  #ST
#data = data.dropna()
#data.reset_index()

#This msk var determines the split between train and test size.
msk = np.random.rand(len(data)) < 0.8
train_df = data[msk]
test_df = data[~msk]
X_train = train_df.drop(columns=['player_id','team_id','points'])
y_train = train_df['points']
X_test = test_df.drop(columns=['player_id','team_id','points'])
y_test = test_df['points']

model = LogisticRegression(penalty='l1', dual=False, tol=0.001, C=1.0, fit_intercept=True,
                   intercept_scaling=1, random_state=None,
                   solver='liblinear', max_iter=300, multi_class='ovr', verbose=0)

#model = LogisticRegression()
#model.fit(X_train, np.ravel(y_train.values))
model.fit(X_train, y_train.values)
y_pred = model.predict(X_test)
#y_pred = y_pred[:,1]

testOutputDict= {}
for g in range(len(y_pred)):
        points_prob = round(y_pred[g],1)
        #player = X_test.reset_index().drop(columns = 'index').loc[g,'player_id']
        match = X_test.reset_index().loc[g,'index']
        print(f'The {match} player has a probability of {points_prob} points for the mactch {match}.')
        testOutputDict[match]=points_prob

'''
version = 'v1_'
timestr = time.strftime("%Y%m%d-%H%M%S")
test_Output_file = "ModelTestOutput_"+version+timestr
oFile = open(test_Output_file,'w')
oFile.write(json.dumps(testOutputDict))
oFile.close()
'''
print(accuracy_score(y_test, y_pred))

#plt.figure(figsize=(10,10))
plt.scatter(y_test, y_pred, c='crimson')
p1 = max(max(y_pred), max(y_test))
p2 = min(min(y_pred), min(y_test))
plt.xlabel('True Values ')
plt.ylabel('Predictions ')
plt.axis('equal')
plt.plot([p1, p2], [p1, p2])
plt.show()