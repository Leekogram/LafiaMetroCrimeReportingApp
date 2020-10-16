'''''''''''''''
Health Mapper 
October 2017
'''''''''''''''

import folium
import pandas as pd
import branca
#North and South = latitude, East and West = longitude
categories = ['Crime', 'Date']
#Actual Coordinates of Constanza
#C_COORDINATES = [18.9115, -70.71]

#Average of Coordinates of Constanza Health Data
C_COORDINATES = [8.490988, 8.527665]

#Reading in CSV file into pandas table
crime_map = pd.read_csv('C:\\Users\\KAYBEST\\Desktop\\Project\\Random_forest.csv')
crime_map=crime_map.dropna()

# Number of Data points_for speed purposes
MAX_RECORDS = 51
 
# create empty map zoomed in on Constanza
constanzaMap = folium.Map(location = C_COORDINATES, 
                            tiles = 'OpenStreet Map', 
                            zoom_start = 16,
                            min_lat=17, max_lat=19, 
                            min_lon=-71, max_lon=-69
                            #min_lat=-90, max_lat=90, min_lon=-180, max_lon=180
                            )


#FOR LOOP: add a marker for every record in the CSV file
for each in crime_map[0:MAX_RECORDS].iterrows():
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
    lat = list(crime_map["latitude"])
    lon = list(crime_map["longitude"])
    cri = list(crime_map["Crime"])
    #dat = list(crime_map["DATE  OF OCCURRENCE"])
    fgv = folium.FeatureGroup(name="Volcanoes")
    
    folium.Marker(
        
        #latitude and longitude GPS-Coordinates
            
            location = [each[1]['latitude'],each[1]['longitude']],
            popup = popup
            
        ).add_to(constanzaMap)
   
 
#display(map)
constanzaMap.save('lafianew1.html')

