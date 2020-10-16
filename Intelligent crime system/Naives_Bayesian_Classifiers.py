'''
CLASS: Naive Bayes SMS spam classifier using sklearn
Data source: https://archive.ics.uci.edu/ml/datasets/SMS+Spam+Collection
'''

## READING IN THE DATA

# read tab-separated file using pandas
import numpy as np 
from pandas import DataFrame
from pandas import Series
from matplotlib import pyplot
import matplotlib.pyplot as plt
import pandas as pd
from math import sqrt
from sklearn.metrics import accuracy_score
import pickle


from pandas import DataFrame
import pandas as pd
##'C:\\Users\\KAYBEST\\Downloads\\Download_crime\\SF_DAT_17-master\\data\\sms.tsv')
df = pd.read_csv('C:\\Users\\KAYBEST\\Desktop\\Project\\ModelData\\NaivesBayesianData.csv')
print(df)
df.head()
#print(df)



feature= df.iloc[:, 1:5].values
target = df.iloc[:, 0].values

#target = df.Crime_Types
print(feature)
print(target)

# split into training and testing sets
from sklearn.model_selection import train_test_split
feature_train, feature_test, target_train, target_test = train_test_split(feature, target, test_size=0.25, random_state=25)


from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(feature_train, target_train)

y_pred = classifier.predict(feature_test)
print(y_pred)

#print(classifier.score(feature_test, y_pred))
accuracy = accuracy_score(target_test, y_pred)
print(accuracy)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(target_test,y_pred) 

print(cm)

from matplotlib.colors import ListedColormap
feature_set, target_set = feature_train, target_train
import seaborn as sns



sns.pairplot(df, x_vars=['LOCATION','DAY','HOUR','MONTH'], y_vars='CRIME_TYPES', size=4.5, aspect=0.7)
#plt.show()
sns.pairplot(df, x_vars=['LOCATION','DAY','HOUR','MONTH'], y_vars='CRIME_TYPES', size=4.5, aspect=0.7, kind='reg')

#pyplot.plot(y_pred)
#pyplot.plot(scatter, color='red')
#pyplot.show()

from matplotlib import cm
## bar plot to examine crime categories based on PdDistrict
crime_count=df.groupby(['CRIME_TYPES']).size()
#set the count numbers into DataFrame for Category + PdDistrict
summary=pd.DataFrame({'count':crime_count}).reset_index()
#find total number of crime in each category then plot pie chart
summary2=summary.groupby('CRIME_TYPES').sum().reset_index()


c=[
"#356146",
"#6B2ED8",
    "#4EBC32",
    "#CF35E0",
    "#85B234",
    "#A85DE7",
    "#B4A82E",
    "#5157D0",
    "#51BA67",
    "#6A2DA6",
    "#407B2A",
    "#D463D5",
    "#90A355",
    "#DB3CAA",
    "#5AB086",
    "#E4412A",
    "#6587DF",
    "#DF8A2F",
    "#AC7CDA",
    "#B18C3C",
    "#842F89",
    "#585A1F",
    "#D773B6",
    "#50A6A8",
    "#AE4220",
    "#6CA2CC",
    "#E35F5D",
    "#52498E",
    "#824D21",
    "#AD90C5",
    "#9B2A3B",
    "#445E7A",
    "#DE427A",
    "#D28461",
    "#932E69",
    "#733A34",
    "#D98AA2",
    "#734968",
    "#AD5F6A"
]



plt.pie(summary2['count'], labels=summary2['CRIME_TYPES'], colors=c)
plt.show()
#find the top 15 crime categories
summary3=summary2.sort_values('count', ascending=False)
top15=summary3[0:5]
print(top15['CRIME_TYPES'])

topCrime=summary[summary['CRIME_TYPES'].isin(top15['CRIME_TYPES'])]
## this selects the top 15 crimes using the boolean function .isin
cri=df.iloc[:, 0].value_counts()
print(cri)
print(topCrime.head())
#ax = plt.subplots(figsize=(10, 4))

#sns.countplot(x='Location', data=df, ax=ax)

moelSave = open('NaivesBayesian.pkl', 'wb')
pickle.dump(classifier, moelSave)

























