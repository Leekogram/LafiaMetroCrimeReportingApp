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
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn import model_selection
dat = pd.read_csv('C:\\Users\\KAYBEST\\Desktop\\Project\\ModelData\\Decisiontree.csv')
print(dat.head())

feature= dat.iloc[:, 1:5].values
target = dat.iloc[:, 0].values
print(feature)
print(target)

from sklearn.model_selection import train_test_split
feature_train, feature_test, target_train, target_test = train_test_split(feature, target, test_size=0.20, random_state=25)

    
print(feature_train)
print(target_train)

from sklearn.tree import DecisionTreeClassifier
dtree = DecisionTreeClassifier()

feature_train=feature_train.reshape(-1,1)
target_train=target_train.reshape(-1,1)


dtree.fit(feature, target)

y_pred=dtree.predict(feature_test)
print(y_pred)
print(target_test)

#The model accuracy



treefeatures=dtree.feature_importances_
indices = np.argsort(treefeatures)
treefeatures

feat = dat.iloc[:,[1,2,3,]]
print(feat)

accuracy = accuracy_score(target_test, y_pred)
print(accuracy)

from sklearn.metrics import confusion_matrix
confusion = confusion_matrix(target_test, y_pred)
print(confusion)

report= classification_report(target_test, y_pred)
print(report)

target_test=target_test.reshape(-1,1)



re = model_selection.cross_val_score(dtree, target_test, y_pred)
print(re.mean())


#plt.savefig('C:\\Users\\KAYBEST\\Desktop\\Project\\ProjectGraph\\actual_predicted.png')

#pyplot.plot(y_pred, target_test)
#pyplot.plot(y_pred, color='red')
#pyplot.show()


moelSave = open('Decisiontree.pkl', 'wb')
pickle.dump(dtree, moelSave)




