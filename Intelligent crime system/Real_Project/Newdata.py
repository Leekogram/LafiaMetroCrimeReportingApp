import numpy as np
import pandas as pd

try:
    # module exists
    import seaborn as sns
    seaborn_exists = True
except ImportError:
    # module doesn't exist
    seaborn_exists = True

import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

# custom features of plots
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.serif'] = 'Helvetica Neue'
plt.rcParams['font.monospace'] = 'Helvetica Neue'
plt.rcParams['font.size'] = 5
plt.rcParams['axes.labelsize'] = 5
plt.rcParams['axes.labelweight'] = 'bold'
plt.rcParams['axes.titlesize'] = 8
plt.rcParams['xtick.labelsize'] = 5
plt.rcParams['ytick.labelsize'] = 8
plt.rcParams['legend.fontsize'] = 8
plt.rcParams['figure.titlesize'] = 8

#df = pd.read_csv('./data/cleaneddataset.csv')
df = pd.read_csv('C:\\Users\\KAYBEST\\Desktop\\Project\\main_dataset.csv')
print (df['CRIME'].unique())
print (df['LOCATION'].unique())
df.head(5)
for col in df:
    print (type(df[col][1]))


#Location with more than 20 crimes

cutoff = 20
plt.figure(figsize=(10,6))
sd = df['LOCATION'].value_counts(sort=True,ascending=True)
sd.index = sd.index.astype(object)
sd = sd[~(sd<cutoff)]
ax = sd.plot.bar()
ax.set_ylabel('Number of Incidents', fontsize=15)
ax.set_xlabel('LOCATION with more than '+str(cutoff)+' crimes', fontsize=15)
plt.savefig('C:\\Users\\KAYBEST\\Desktop\\Project\\ProjectGraph\\CrimeLocation.png')




# SPlit The DateTime

df['DATE  OF OCCURRENCE'] = pd.to_datetime(df['DATE  OF OCCURRENCE'].astype(str), errors='coerce')
        
df['DATE  OF OCCURRENCE'] = pd.to_datetime(df['DATE  OF OCCURRENCE'], format = '%d/%m/%Y %H:%M:%S')
print(df['DATE  OF OCCURRENCE'])

column_1 = df.ix[:,1]

db=pd.DataFrame({"YEAR": column_1.dt.year,
              "MONTH": column_1.dt.month,
              "DAY": column_1.dt.day,
              "HOUR": column_1.dt.hour,
              "DAYOFYEAR": column_1.dt.dayofyear,
              "WEEK": column_1.dt.week,
              "WEEKOFYEAR": column_1.dt.weekofyear,
              "DAYOFWEEK": column_1.dt.dayofweek,
              "WEEKDAY": column_1.dt.weekday,
              "QUARTER": column_1.dt.quarter,
             })

dataset1=df.drop('DATE  OF OCCURRENCE',axis=1)
data1=pd.concat([db,dataset1],axis=1)
print(data1)
data1.to_csv('C:\\Users\\KAYBEST\\Desktop\\Project\\cleaneddata.csv', encoding='utf-8',index=False)

#MONTHLY CRIME
crime_year = pd.crosstab([data1['YEAR'],data1['MONTH']],data1['CRIME'])

"""fig, ax = plt.subplots(nrows=1, ncols=1,figsize=(12,6))
crime_year.plot(kind='bar', stacked=False, grid=False,ax=ax)
ax.set_ylabel("number of incidents")
ax.set_xlabel("year")
ax.legend(loc = (1,0.1))
ax.set_ylim(0,3000)
plt.tight_layout()
plt.show()"""

"""ax = crime_year.plot()
ax.set_ylabel("number of incidents")
ax.set_xlabel("year")
ax.legend(loc = (1,0.1))
ax.set_ylim(0,3000)
ax.set_xticklabels(ax.get_xticklabels(),rotation=90)
plt.tight_layout()
plt.show()"""

#sns.heatmap(crime_year.T)
#plt.show()

# a set of colors to plot the bars
color_sequence = ['#1f77b4', '#ff7f0e', '#2ca02c','#d62728','#8c564b',
                  '#377eb8','#4daf4a','#984ea3','#f781bf']

# Monthly Crime
fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(12,12), sharex=True)
k=0
for i in range(0,3):
    for j in range(0,3):
        ax = axes[i,j]
        # selec kth columns
        crime_year_col = crime_year.ix[:,k]
        #plot the data with a selected color
        crime_year_col.plot(kind='bar', ax=ax, color=color_sequence[k])
        ax.legend(loc = (0,1))
        # rotate the x-axis ticks
        ax.set_xticklabels(ax.get_xticklabels(),rotation=90)
        ax.set_xlabel('')
        k+=1
plt.tight_layout()
#plt.show(fig)
plt.figure(0)
data1.groupby(['YEAR','MONTH'])['CRIME'].count().plot(kind='bar')
#plt.show()

print (data1['WEEKDAY'].unique())
print (data1['HOUR'].unique()) 

#Heat Map OF CRIMES TYPES WITH WEEKDAY

dclean = pd.read_csv('C:\\Users\\KAYBEST\\Desktop\\Project\\cleaned.csv')

"""crime_weekday = pd.crosstab(dclean['WEEKDAY'],dclean['CRIME'])
print(crime_weekday)
ax = plt.subplots(nrows=1, ncols=1, figsize=(12,8), sharex=True)
daysOfWeekList = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
crime_weekday=crime_weekday.reindex(daysOfWeekList)

ax=sns.heatmap(crime_weekday.T,annot=True, fmt="d",linewidths=0.5,cmap='RdBu_r', mask=crime_weekday.T.isnull(), yticklabels=dclean.CRIME)
ax.set_xticklabels(ax.get_xticklabels(),rotation=30)

#plt.savefig('heatmap.png')
plt.show(fig)
"""


#HIGHEST AND LOWEST CRIME DAYS
fig, axes = plt.subplots(nrows=3, ncols=3,figsize=(12,12),sharex=True)

print ('| Crime | Highest | Lowest |')
print ('| --- | --- | --- |')
k=0
for i in range(0,3):
    for j in range(0,3):
        ax = axes[i,j]
        # selec kth columns
        crime_weekday = pd.crosstab(dclean['WEEKDAY'],dclean['CRIME'])
    
        crime_weakday_col = crime_weekday.ix[:,k]
        
        crime_name = crime_weakday_col
        crime_max_label,crime_max_val = crime_weakday_col.idxmax(), crime_weakday_col.max()
        crime_min_label,crime_min_val = crime_weakday_col.idxmin(), crime_weakday_col.min()
        print ('| {} | {} ({}) | {} ({}) |'.format(crime_name,crime_max_label,crime_max_val,crime_min_label,crime_min_val))
        
        crime_weakday_col.plot(kind='line',ax=ax,color='r',marker='o')
        #crime_weakday_col.plot(kind='bar',ax=ax,color='r')
        ax.legend(loc = (0,1))
        ax.set_xticklabels(ax.get_xticklabels(),rotation=60)
        ax.set_xlabel('')
        k+=1
plt.tight_layout()
plt.savefig('C:\\Users\\KAYBEST\\Desktop\\Project\\ProjectGraph\\Crimehours.png')
#plt.show(fig)


#MONTH DAY CRIME TREND
crime_monthday = pd.crosstab(dclean['DAY'],dclean['CRIME'])

fig, axes = plt.subplots(nrows=3, ncols=3,figsize=(12,12),sharex=True)

k=0
for i in range(0,3):
    for j in range(0,3):
        ax = axes[i,j]
        crime_monthday_col = crime_monthday.ix[:,k]
        
        crime_monthday_col.plot(kind='line',ax=ax,color='r',marker='o')
        ax.legend(loc = (0,1))
        ax.set_xticklabels(ax.get_xticklabels(),rotation=0)
        ax.set_xlabel('')
        k+=1
plt.tight_layout()
#plt.show(fig)


# MOST PREVALENT CRIMES

top5List = data1["CRIME"].value_counts().head(5).index.tolist()
top5Counts = data1["CRIME"].value_counts().head(5)

print(top5List)
print(top5Counts)


# display most prevalent Crimes
x = np.arange(5)
fig, ax = plt.subplots()
fig.set_size_inches(10,6)
ax.set_title('Top 5 Crimes', fontsize=20, fontweight='bold')
ax.set_xlabel('Crime Category', fontsize=15)
ax.set_ylabel('Number of Crimes (Thousands)', fontsize=15)
# The x axis of the chart is the head of the value count function on the full database. 
# Which will get the occurance of each unique value in the primary type column 
plt.bar(x, top5Counts , color=['red', 'blue'])
# the labels are the list of the top ten crimes from above
plt.xticks(x, top5List)
plt.savefig('C:\\Users\\KAYBEST\\Desktop\\Project\\ProjectGraph\\Top5crimes.png')

#plt.show()


#The number of each types of crimes in a year
MostCrime = pd.crosstab(dclean['YEAR'],dclean['CRIME'])
print(MostCrime)
#MostCrime.to_csv('C:\\Users\\KAYBEST\\Desktop\\Project\\ModelData\\LinearRegData.csv', encoding='utf-8',index=False)





top5Arrests = dclean.loc[(dclean['CRIME'].isin([top5List[0], top5List[1], top5List[2], top5List[3], top5List[4]])) & dclean['ARREST'] == True]
# This lines gets all the rows for the top 5 crimes that have no arrests made
top5fails = dclean.loc[(dclean['ARREST'] == False) & dclean['CRIME'].isin([top5List[0], top5List[1], top5List[2], top5List[3], top5List[4]])]


#These next two lines get the number of arrests and non arrests for the top 5 crimes and orders the counts by the crime name
Arr = top5Arrests["CRIME"].value_counts().sort_index()
noArr = top5fails["CRIME"].value_counts().sort_index()
#This shows the order the crimes and there counts will be in for the visualisation below




print("Arrests: \n", Arr)
print("\n\n")
print("No Arrests: \n", noArr)


#This bar chart takes the top 5 most occuring crimes and compares the numbers of arrests to no arrests when these crimes occur. 
width = 0.25  

# The number of bars 
ind = np.arange(5)
fig, ax = plt.subplots()

# size of the graph
fig.set_size_inches(10,6)
ax.set_title('Arrest/No Arrest numbers (Top 5 Crimes)', fontsize=20, fontweight='bold')
ax.set_xlabel('Different crimes', fontsize=15)
ax.set_ylabel('Number of Arrests/No Arrest (Thousands)', fontsize=15)

# the true and false bars 
true = ax.bar(ind, Arr, width, color='g')
false = ax.bar(ind + 0.25, noArr, width, color='r')

# creating the lengend and titles
ax.legend((true[0], false[0]), ('Arrest', 'No Arrest'), bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., prop={'size': 7})
ax.set_xticks(ind + width/2)
ax.set_xticklabels(top5List)
plt.savefig('C:\\Users\\KAYBEST\\Desktop\\Project\\ProjectGraph\\Arrest_NoArrest.png')


#This is the list of the years for the xtick labels
yearList = dclean["YEAR"].value_counts().sort_index().index.tolist()
cr=dclean["CRIME"].value_counts().sort_index()
print(cr)


# There are 10 years being compared
ind = np.arange(10)
fig, ax = plt.subplots()
fig.set_size_inches(12, 8)
ax.set_title('Numbers of Crime (Over Years)', fontsize=20, fontweight='bold')
ax.set_xlabel('Years', fontsize=15)
ax.set_ylabel('Number of Crimes (Thousands)', fontsize=15)

#Here we are plotting a line graph of the years against the number of crimes for each year from oldest to newest year
ax.plot(ind, dclean["YEAR"].value_counts().sort_index(), color='orange')
ax.set_xticklabels(yearList)
ax.set_xticks(ind)
plt.savefig('C:\\Users\\KAYBEST\\Desktop\\Project\\ProjectGraph\\CrimeYear.png')

Hour = dclean["HOUR"].value_counts()
#print(Hour)


hr = np.arange(24)
fig, ax = plt.subplots()
fig.set_size_inches(10, 6)
ax.set_title('Crimes by time of day', fontsize=20, fontweight='bold')
ax.set_xlabel('Time of day', fontsize=15)
ax.set_ylabel('Number of Crimes (Thousands)', fontsize=15)

#Here we are plotting a line graph of the years against the number of crimes for each year from oldest to newest year
ax.bar(hr, dclean["HOUR"].value_counts().sort_index())
ax.set_xticks(hr)
plt.savefig('C:\\Users\\KAYBEST\\Desktop\\Project\\ProjectGraph\\CrimeHour.png')


day=dclean["DAYOFWEEK"].value_counts().sort_index()
print(day)

d = np.arange(7)
fig, ax = plt.subplots()
fig.set_size_inches(10, 6)
ax.set_title('Crimes by day of week', fontsize=20, fontweight='bold')
ax.set_xlabel('Day of week', fontsize=15)
ax.set_ylabel('Number of Crimes (Thousands)', fontsize=15)
dayNameList = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# The line graph plots the number of crimes over the different days of the week. 
ax.bar(d, dclean["DAYOFWEEK"].value_counts().sort_index(), color='purple')
ax.set_xticklabels(dayNameList)
ax.set_xticks(d)
plt.savefig('C:\\Users\\KAYBEST\\Desktop\\Project\\ProjectGraph\\CrimeDays.png')

mon=dclean["MONTH"].value_counts().sort_index()
print(mon)

m = np.arange(12)
fig, ax = plt.subplots()
fig.set_size_inches(10, 6)
ax.set_title('Crimes numbers by month', fontsize=20, fontweight='bold')
ax.set_xlabel('Month', fontsize=15)
ax.set_ylabel('Number of Crimes (Thousands)', fontsize=15)
monthNameList = ["Jan", "Feb","Mar", "Apr","May","June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]

# The line graph plots the number of crimes over the different days of the week. 
ax.bar(m, mon, color='blue')
ax.set_xticklabels(monthNameList)
ax.set_xticks(m)
plt.savefig('C:\\Users\\KAYBEST\\Desktop\\Project\\ProjectGraph\\Crimemonth.png')


cr=dclean["CRIME"].value_counts().sort_index()
print(cr)

c = np.arange(13)
fig, ax = plt.subplots()
fig.set_size_inches(10,6)
ax.set_title('Crimes in Lafia(2009-2018)', fontsize=20, fontweight='bold')
ax.set_xlabel('Crime', fontsize=15)
ax.set_ylabel('Number of Crimes(Thousands)', fontsize=15)

crimelist = ["Assault", "Burglary","Cultism", "Drug","Homicide","House/Shop Breaking", "Kidnapping", "Other Offences", "Raping", "Robbery", "Sexual Assault", "Stealing","Stealing/Shop Breaking"]

ax.bar(c, cr, color='blue')
ax.set_xticklabels(crimelist)
ax.set_xticks(c)
plt.savefig('C:\\Users\\KAYBEST\\Desktop\\Project\\ProjectGraph\\Crimetype.png')



LocList = df["LOCATION"].value_counts()
print(LocList)
#c = np.arange(32)
#fig, ax = plt.bar()
#fig.set_size_inches(25, 12)
#ax.set_title('Crime Location', fontsize=20, fontweight='bold')
#ax.set_xlabel('Crime', fontsize=15)
#ax.set_ylabel('Number of Crimes', fontsize=20)
#ax.bar(c, LocList, color='red')
#ax.set_xticks(c)
#plt.savefig('C:\\Users\\KAYBEST\\Desktop\\Project\\ProjectGraph\\Location.png')


yr=dclean["YEAR"].value_counts()
print(yr)

y=pd.crosstab(dclean["YEAR"], dclean['CRIME'])
print(y)




from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()

# Iterating over all the common columns in train and test

       # Encoding only categorical variables
       # Using whole data to form an exhaustive list of levels



"""for col in dclean.columns.values:
    if dclean[col].dtypes=='object':
        data=dclean[col].append(dclean[col])
        le.fit(data.values)
        d=dclean[col]=le.transform(dclean[col])
        print(d)
        df=pd.DataFrame(d)
        print(df)
        
        df.to_csv('C:\\Users\\KAYBEST\\Desktop\\Project\\catdat.csv', encoding='utf-8',index=False)
        
dat=le.fit_transform(dclean['LOCAT'].astype(str))
print(dat)
print(dclean.head())      

datase=dclean.drop('LOCAT',axis=1)
dfa=pd.DataFrame(dat)
dat1=pd.concat([dfa,datase],axis=1)
#dat1=dclean.append(dat)
print(dat1)
dat1.to_csv('C:\\Users\\KAYBEST\\Desktop\\Project\\cleancatdat.csv', encoding='utf-8',index=False)

cricat = pd.read_csv('C:\\Users\\KAYBEST\\Desktop\\Project\\cleancatdat.csv')
dat=le.fit_transform(cricat['CRIM'].astype(str))
print(dat)
print(cricat.head())      

datase=cricat.drop('CRIM',axis=1)
dfa=pd.DataFrame(dat)
dat1=pd.concat([dfa,datase],axis=1)
#dat1=dclean.append(dat)
print(dat1)
dat1.to_csv('C:\\Users\\KAYBEST\\Desktop\\Project\\PreProcessed.csv', encoding='utf-8',index=False)"""





Loc = np.arange(44)
fig, ax = plt.subplots()
fig.set_size_inches(18, 10)
ax.set_title('Location of the Crimes (Crime numbers)', fontsize=20, fontweight='bold')
ax.set_xlabel('Location', fontsize=15)
ax.set_ylabel('Number of Crimes (Thousands)', fontsize=15)
#monthNameList = ["Jan", "Feb","Mar", "Apr","May","June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]

# The line graph plots the number of crimes over the different days of the week. 
ax.bar(Loc, LocList, color='blue')

ax.set_xticks(Loc)

sns.boxplot(x='ARRT' ,y='HOUR' ,data=dclean, palette='winter_r')
dff = pd.DataFrame(data=dclean, columns=['CRIME','ARRT', 'HOUR', 'DAYOFWEEK'])
dff.plot.hexbin(x='ARRT',y='HOUR',gridsize=25)
dff.plot(legend=False)



# extract and summarize data
ddf = dclean[dclean['CRIME']=="STEALING"]
dtop = ddf.groupby(['YEAR', 'LOCATION']).agg({'LOCATION':'count'}).rename(columns={'LOCATION':'STEALING_INCIDENT'}).reset_index()

# sort and extract neighborhood addresses as a new column using 'extract_address' function.
topdf = dtop.sort_values('STEALING_INCIDENT', ascending=False).reset_index(drop=True).iloc[:1]




# Importing LabelEncoder and initializing it


# display result
print(topdf)

plt.show()




