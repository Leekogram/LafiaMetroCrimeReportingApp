import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
import statsmodels.formula.api as smf
import seaborn as sns

# visualization
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import pyplot
import pickle
import numpy as n
from sklearn import model_selection
import math
from sklearn.metrics import classification_report
from sklearn import metrics


dat = pd.read_csv('C:\\Users\\KAYBEST\\Desktop\\Project\\ModelData\\LinearRegData.csv')
print(dat.head())


feature= dat.iloc[:, [0,2]].values
target = dat.iloc[:, 1].values
print(feature)
print(target)

from sklearn.model_selection import train_test_split
Xtrain, Xtest, Ytrain, Ytest = train_test_split(feature, target, test_size=0.20, random_state=25)

    
linreg = LinearRegression()
linreg.fit(Xtrain, Ytrain)
pred=n.round(linreg.predict(Xtest))
print(pred)


dfa=n.round(pred)
print(dfa)


result = model_selection.cross_val_score(linreg, feature, target)
print(result.mean())

re = linreg.score(Xtest,pred)
re=re*100
print(re)

print((linreg.coef_))
print(linreg.intercept_)

print("Mean Squared Error:")
print(metrics.mean_absolute_error(Ytest, pred))
print("Mean Squared Error:" )
print(metrics.mean_squared_error(Ytest, pred))
print("Root Mean Squared Error:")
print(np.sqrt(metrics.mean_squared_error(Ytest, pred)))

# instantiate and fit
Xtrain=Xtrain.reshape(-1,1)
Ytrain=Ytrain.reshape(-1,1)




# predict for a new observation
Xtest=Xtest.reshape(-1,1)
series=dat.max(axis=1)
#pred = format(series[0], '.0f')
#print(pred)



#print(int(str(pred)[2]))

pyplot.plot(pred)
pyplot.plot(pred, color='red')
pyplot.show()


moelSave = open('Regression.pkl', 'wb')
pickle.dump(linreg, moelSave)

## Creating & Training KNN Model



