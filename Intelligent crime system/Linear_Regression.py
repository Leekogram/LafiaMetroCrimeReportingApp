import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from pandas import DataFrame
import math


from sklearn import metrics
import statsmodels.formula.api as smf

# visualization
import seaborn as sns
import matplotlib.pyplot as plt


data = pd.read_csv('C:\\Users\\KAYBEST\\Desktop\\Project\\Linear.csv')
print(data)

feature= data.iloc[:, 0].values
target = data.iloc[:, 1].values

print(feature)
print(target)

from sklearn.model_selection import train_test_split
Xtrain, Xtest, Ytrain, Ytest = train_test_split(feature, target, test_size=0.25, random_state=25)

print(Xtrain)
print(Ytrain)

learningRate = 0
numEpochs =1000


def hypothesis(t0,t1,x):
    return (t0 + t1*x)

#Our loss function is the classic mean squared error form
def costFunction(t0, t1):
    loss = 0
    for i, j in zip(Xtrain,Ytrain):
        temp = math.pow((hypothesis(t0,t1,i) - j),2)
        loss += temp
    return loss

#Weight updates are done by taking the derivative of the loss function 
#with respect to each of the theta values. 
def weightUpdate(withRespectTo, t0, t1):
    if (withRespectTo == "theta0"):
        t0 = t0 - learningRate*(derivative(withRespectTo, t0, t1))
        return t0
    else: #has to be wrt to theta1
        t1 = t1 - learningRate*(derivative(withRespectTo, t0, t1))
        return t1
    
#Evaluating a numerical deerivative
def derivative(withRespectTo, t0, t1):
    h = 1./1000.
    if (withRespectTo == "theta0"):
        rise = costFunction(t0 + h, t1) - costFunction(t0,t1)
    else: #has to be wrt to theta1
        rise = costFunction(t0 , t1 + h) - costFunction(t0,t1)
    run = h
    slope = rise/run
    return slope

#Random initialization of the theta values
theta0 = np.random.uniform(0,1)
theta1 = np.random.uniform(0,1)
#Test value
Xtest = 2000
for i in range(0,numEpochs):
    theta0 = weightUpdate("theta0", theta0, theta1)
    theta1 = weightUpdate("theta1", theta0, theta1)
print (hypothesis(theta0,theta1,Xtest))


#lm = smf.ols(formula='Year ~ Homicide', data=data).fit()
