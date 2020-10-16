'''''''''''''''
Health Mapper 
October 2017
'''''''''''''''

import folium
import pandas as pd
import branca
#North and South = latitude, East and West = longitude
categories = ['CRIME', 
            'DATE  OF OCCURRENCE',
            'ARREST'
            ]
#Actual Coordinates of Constanza
#C_COORDINATES = [18.9115, -70.71]

#Average of Coordinates of Constanza Health Data
C_COORDINATES = [8.490988, 8.527665]

#Reading in CSV file into pandas table
crime_data = pd.read_csv('C:\\Users\\KAYBEST\\Desktop\\Project\\main_dataset.csv')
crime_data=crime_data.dropna()

def color_producer(Crim):

        if Crim =="STEALING":
            return 'green'
        elif Crim== "ROBBERY":
            return 'orange'
        else:
            return 'red'

# Number of Data points_for speed purposes
MAX_RECORDS = 10
 
# create empty map zoomed in on Constanza
constanzaMap = folium.Map(location = C_COORDINATES, 
                            tiles = 'OpenStreet Map', 
                            zoom_start = 12,
                            min_lat=17, max_lat=19, 
                            min_lon=-71, max_lon=-69
                            
                            )


#FOR LOOP: add a marker for every record in the CSV file
for each in crime_data[0:MAX_RECORDS].iterrows():
    #FUNCTION: Generates HTML code for Pop-Up
    def simpHTML(x, each):
        html = '<h4>' + str(x) + '</h4>' + '<p>' + str(each[1][x]) + '</p>'
        return html
    html = ''
    i = 0
    #FOR LOOP: Goes Through Health Categories List and appends it to html code
    for item in range(len(categories)):
        x = simpHTML(categories[i], each)
        i += 1
        html += x
    iframe = branca.element.IFrame(html=html, width=150, height=300)
    popup = folium.Popup(iframe, max_width=500)

    #Creates actual marker based on CSV GPS coordinates and Health Categories List Names
    lat = list(crime_data["LATITUDE"])
    lon = list(crime_data["LONGITUDE"])
    cri = list(crime_data["CRIME"])
    dat = list(crime_data["DATE  OF OCCURRENCE"])
    fgv = folium.FeatureGroup(name="Volcanoes")
    
    for c in zip(cri):
    
        folium.Marker(
        
        #latitude and longitude GPS-Coordinates
            
            location = [each[1]['LATITUDE'],each[1]['LONGITUDE']],
            popup = popup,
            color=color_producer(c)
            
        ).add_to(constanzaMap)
 
#display(map)
    print("YES")
constanzaMap.save('lafiaCme.html')

