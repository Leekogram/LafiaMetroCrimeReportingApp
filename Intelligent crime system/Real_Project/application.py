from flask import Flask,render_template,url_for,request
import pandas as pd 
import pickle
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LinearRegression
from sklearn.externals import joblib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.externals import joblib
import calendar
import math



app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html')
@app.route('/index.html')
def home():
    return render_template('index.html')
@app.route('/chart.html')
def charts():
    return render_template('chart.html')

@app.route('/table.html')
def tables():
    return render_template('table.html')

@app.route('/map.html')
def maps():
    return render_template('map.html')

@app.route('/crimerate.html', methods=['GET', 'POST'])
def crimerate():
    if request.method == 'POST':
                        model = joblib.load('Regression.pkl')
                        crimeyear = float(request.form['year'])
                        crimetyp = float(request.form['crimecat'])
                        intcrity = int(crimetyp)
                        intyear = int(crimeyear)
                        
                        if intcrity == 1:
                            intcrity='Burglary'
                        elif intcrity == 2:
                            intcrity='Cultism'
                        elif intcrity == 3:
                            intcrity='Drug Abuse'
                        elif intcrity== 4:
                             intcrity='Homicide'
                        elif intcrity== 5:
                             intcrity='House/Shop Breaking'
                        elif intcrity == 6:
                            intcrity='Kidnapping'
                    
                        elif intcrity== 7:
                            intcrity='Other Offence'
                        elif intcrity== 8:
                            intcrity='Raping'
                        elif intcrity == 9:
                            intcrity='Robbery'
                        elif intcrity== 11:
                            intcrity='Stealing'
                        elif intcrity== 12:
                            intcrity='Assault'
                        elif intcrity == 13:
                            intcrity='Stealing/ Shop Breaking'
                        else:
                            intcrity=''
                        
                        crim = [
                            crimeyear,
                            crimetyp,
                            
                            ]
                        my_pred = [
                            crim
                            ]
                        
                        my_prediction = model.predict(my_pred)[0]
                        my_prediction=np.round(my_prediction, 0)
                        appro=int(my_prediction)
                    
                        return render_template('predictedcrimerate.html',prediction = appro, crimeyear=intyear, crimetyp=intcrity)
    
                    
    return render_template('crimerate.html')
    

        
@app.route('/crimehotspot.html', methods=['GET', 'POST'])
def crimehotspott():
    if request.method == 'POST':
                model = joblib.load('RandomForest.pkl')
        
                day = float(request.form['day'])
        
                month = float(request.form['month'])
                monthString = calendar.month_name[int(month)]
                dayString = calendar.day_name[int(day)]
                crimetypes = float(request.form['crimestypes'])
                
                intcrim = int(crimetypes)
                
                if intcrim == 1:
                            intcrim='Burglary'
                elif intcrim == 2:
                            intcrim='Cultism'
                elif intcrim == 3:
                            intcrim='Drug Abuse'
                elif intcrim== 4:
                             intcrim='Homicide'
                elif intcrim== 5:
                             intcrim='House/Shop Breaking'
                elif intcrim == 6:
                            intcrim='Kidnapping'
                    
                elif intcrim== 7:
                            intcrim='Other Offence'
                elif intcrim== 8:
                            intcrim='Raping'
                elif intcrim == 9:
                            intcrim='Robbery'
                elif intcrim== 11:
                            intcrim='Stealing'
                elif intcrim== 12:
                            intcrim='Assault'
                elif intcrim == 13:
                            intcrim='Stealing/ Shop Breaking'
                else:
                            intcrim=''
                
        
                hotspotfeature = [
                    day,
                    month,
                    crimetypes,
                    ]
        
                hotspot=[
                    hotspotfeature
                    ]        
    

                hotspotprediction = model.predict(hotspot)[0]
                result_rf=pd.DataFrame(hotspotprediction)
               
                yes = ', '.join([repr(i) for i in hotspotprediction])
                return render_template('predictedcrimehotspot.html',prediction = yes, month=monthString, crimet =intcrim, day=dayString)

    return render_template('crimehotspot.html')
    
            

@app.route('/crimetypes.html', methods=['GET', 'POST'])
def crimetypes():
    
    
    
   if request.method == 'POST':
                model = joblib.load('Decisiontree.pkl')
        
                location = float(request.form['location'])
                day = float(request.form['day'])
                time = float(request.form['time'])
                month = float(request.form['month'])
                
                monthStr = calendar.month_name[int(month)]
                dayStr = calendar.day_name[int(day)]
                timeStr = int(time)
        
        
                feature = [
                    location,
                    day,
                    time,
                    month,
                    ]
        
                feat=[
                    feature
                    ]        
                def color_producer(timestr):
                
                    if 0 <= timestr <12 :
                        timestr= timestr,
                        'am'
                    elif 12 <= timestr <23 :
                        timestr= timestr,
                    else:
                        timestr='No Location.'
                
                
                if location == 25:
                    location='Student Village'
                elif location == 21:
                    location='Post Office Area'
                elif location == 13:
                    location='Lavista'
                elif location== 18:
                    location='Nas ST. Poly'
                elif location== 22:
                    location='Project Quarters'
                elif location == 10:
                    location='Lafia East'
                    
                elif location== 17:
                    location='Modern Market'
                elif location== 12:
                    location='Lafia Township Stadium'
                elif location == 31:
                    location='Workers Village'
                elif location== 28:
                    location='Tundun Gwandara'
                elif location== 29:
                    location='U.A.C Road'
                elif location == 6:
                    location='Dunama'
                elif location== 9:
                    location='Inec Office'
                elif location== 26:
                    location='Tahiti Lodge Area'
                elif location == 19:
                    location='Old Tomato Market'
                elif location== 7:
                    location='Government Residential Area'
                elif location== 8:
                    location='Lafia Emirs Palace'
                elif location == 15:
                    location='Millionaire Quarters'
                elif location == 20:
                    location='Open University'
                else:
                    location='No Location.'

                my_prediction = model.predict(feat)[0]
                if my_prediction == 1:
                    my_prediction='Burglary'
                elif my_prediction == 2:
                    my_prediction='Cultism'
                elif my_prediction == 3:
                    my_prediction='Drug Abuse'
                elif my_prediction== 4:
                    my_prediction='Homicide'
                elif my_prediction== 5:
                    my_prediction='House/Shop Breaking'
                elif my_prediction == 6:
                    my_prediction='Kidnapping'
                    
                elif my_prediction== 7:
                    my_prediction='Other Offence'
                elif my_prediction== 8:
                    my_prediction='Raping'
                elif my_prediction == 9:
                    my_prediction='Robbery'
                elif my_prediction== 11:
                    my_prediction='Stealing'
                elif my_prediction== 12:
                    my_prediction='Assault'
                elif my_prediction == 13:
                    my_prediction='Stealing/ Shop Breaking'
                else:
                    my_prediction='Place is safe no crime expected at that timestamp.'
    
                return render_template('predictedcrimetypes.html',prediction = my_prediction, day=dayStr, time=timeStr, month=monthStr, location=location)
 
   return render_template('crimetypes.html')


if __name__ == '__main__':
    app.run(debug=True, port='2000')
    
       