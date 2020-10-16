import numpy as np
import pandas as pd
import scipy
import matplotlib.pyplot as plt
import matplotlib.lines as ml
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import pickle
from sklearn import model_selection

from sklearn.metrics import classification_report
data = pd.read_csv('C:\\Users\\KAYBEST\\Desktop\\Project\\ModelData\\RandomForestData.csv')

print(data.shape)
#print(data.describe())
 #cleaning the data by removing nan values
data = data.dropna(axis=0,how='any',inplace=False)

data['LATITUDE'] =data['LATITUDE'].astype(float)
data['LONGITUDE'] =data['LONGITUDE'].astype(float)


target= data.iloc[:,[3,4,]]
predictor=data.iloc[:,[0,1,5,]]

from sklearn.model_selection import train_test_split
Xtrain, Xtest, Ytrain, Ytest = train_test_split(predictor, target, test_size=0.20, random_state=25)



rf = RandomForestRegressor(n_estimators=100,n_jobs=2,oob_score=True)
rf.fit(Xtrain, Ytrain)
predictions_rf = rf.predict(Xtest)
print(predictions_rf)

from sklearn.metrics import accuracy_score

result = model_selection.cross_val_score(rf, Xtest, Ytest)
print(result.mean())

re = rf.score(Xtest,predictions_rf)
print(re)

from sklearn import metrics
print("Mean Squared Error:")
print(metrics.mean_absolute_error(Ytest, predictions_rf))
print("Mean Squared Error:" )
print(metrics.mean_squared_error(Ytest, predictions_rf))
print("Root Mean Squared Error:")
print(np.sqrt(metrics.mean_squared_error(Ytest, predictions_rf)))



result_rf=pd.DataFrame(predictions_rf)
result_rf.columns=['LONGITUDE', 'LATITUDE']
#print(result_rf)
#s=",".join(predictions_rf)

#hot = [predictions_rf.split(",")]
yes = ','.join([repr(i) for i in predictions_rf])
print(yes)

resultrf=result_rf[["LATITUDE","LONGITUDE"]]
resultr=resultrf[:5]
print(resultr)
rlist= resultr.get_values()
#spl_list = [i.split() for i in rlist]
#",".join(rlist).split("")
#for l in rlist:
    #type= l.split(",")


moelSave = open('RandomForest.pkl', 'wb')
pickle.dump(rf, moelSave)







