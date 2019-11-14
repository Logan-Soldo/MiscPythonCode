import urllib.request
import pandas as pd

def airport_data(station_input):
    # Read Airport Data    
 #       airport_txt = open('airports_dat.csv',encoding = 'utf8')
    airport_txt = pd.read_csv('airports_dat.csv',delimiter=',', names = ['ID','Name','City','Country','IATA','ICAO','Lat','Lon','Alt','TZ','DST','TZO','Type','Source'])
    return airport_txt

def airport_alt(data,station_input):
    station_info = data[data['ICAO'].str.match(station_input)]
    if station_info.empty:
        print("No Elevation Data")
    else:
        Alt = station_info['Alt'].values
        print("Elevation: {:d}ft ".format(int(Alt)))  

station_input = input("Input ICAO Code; 'EXIT' to quit: ")
station_input = station_input.upper()
print()
while station_input.upper() != "EXIT":  
    
    station_input = station_input.upper()      
    URL_str= "https://www.aviationweather.gov/metar/data?ids={:s}&format=decoded&date=&hours=0".format(station_input)
#    URL_str= "https://www.aviationweather.gov/metar/data?ids=KBTV&format=decoded&date=&hours=0"    
    url = URL_str
    response = urllib.request.urlopen(url)
    result = str(response.read())
    # print(result)
###############################################################################
      
###############################################################################
    # Date
    date_index = result.find("Data at: ")
    date_end_index = result.find("Data starts here")
    date_data = result[date_index:date_end_index]
    date = date_data[:29]
#    print(date)
    
    # Station
    station_index = result.find('METAR for')
    station_end_index = result.find("Text:")
    station = result[station_index:station_end_index]
    station_predata = station[26:]
    station_end = station_predata.find("</td")
    station_data = station_predata[:station_end]
#    print("Metar for: ",station)
    
    # Index results to just raw data output
    index = result.find("Text:</span>")
    end_index = result.find("Data ends here")
    raw_data = result[index:end_index]
    # print(raw_data)
    
    # Index raw data to correct pieces
###############################################################################
    # Text
    text_index = raw_data.find(" bold")
    text_end_index = raw_data.find("Temperature")
    text = raw_data[text_index:text_end_index]
    Text_predata = text[7:]
    Text_end = Text_predata.find("</td")
    if Text_predata[3:16] != "No data found":
        Text_data = Text_predata[:Text_end]      # print just this in 
###############################################################################
    # Temperature
    temp_index = raw_data.find("Temperature:</span></td><td>")
    temp_end_index = raw_data.find("Dewpoint")
    temp = raw_data[temp_index:temp_end_index]
    
    celsius = temp[28:33]       #print in final
    fahrenheit = temp[41:44]    #print in final
###############################################################################
    # Dewpoint
    dew_index = raw_data.find("Dewpoint")
    dew_end_index = raw_data.find("Pressure")
    dew = raw_data[dew_index:dew_end_index]
    
    dewpoint_C = dew[26:30] #print in final
    dewpoint_F = dew[39:41] #print in final
    RH = dew[56:58]  # percentage
    
    degree_sign= u'\N{DEGREE SIGN}'    
###############################################################################
    # Pressure(altimiter)
    pressure_index = raw_data.find("altimeter")
    pressure_end_index = raw_data.find("Winds")
    pressure = raw_data[pressure_index:pressure_end_index]
    
    Hg = pressure[27:32]  #print in final
    Mb = pressure[44:50]  #print in final
    SLP = pressure[76:82] #print in final
###############################################################################
    # Winds
    wind_index = raw_data.find("Winds")
    wind_end_index = raw_data.find("Visibility")
    wind = raw_data[wind_index:wind_end_index]
    wind_predata = wind[22:]
    wind_end = wind_predata.find("</td>")
    wind_data = wind_predata[:wind_end] # print in final  
###############################################################################
    # Visibility
    vis_index = raw_data.find("Visibility")
    vis_end_index = raw_data.find("Ceiling")
    vis= raw_data[vis_index:vis_end_index]
    vis_predata = vis[27:]
    vis_end = vis_predata.find("</td>")
    vis_data = vis_predata[:vis_end] # print in final  
###############################################################################
    # Ceiling
    ceiling_index = raw_data.find("Ceiling")
    ceiling_end_index = raw_data.find("Clouds")
    ceiling = raw_data[ceiling_index:ceiling_end_index]
    ceiling_predata= ceiling[24:]
    ceiling_end= ceiling_predata.find("</td")
    ceiling_data= ceiling_predata[:ceiling_end] # print in final  
###############################################################################
    # Clouds
    clouds_index = raw_data.find("Clouds")
    clouds_end_index = raw_data.find("Weather")
    clouds = raw_data[clouds_index:clouds_end_index]
    clouds_predata = clouds[23:]
    clouds_end = clouds_predata.find("</td>")
    clouds_data =  clouds_predata[:clouds_end] # print in final  
###############################################################################
    # Weather
    weather_index = raw_data.find("Weather")
    if weather_index != -1:
        weather = raw_data[weather_index:] 
        weather_predata = weather[24:]
        weather_end = weather_predata.find("</td>")
        weather_data = weather_predata[:weather_end] # print in final  

###############################################################################
    # Final output
    data = airport_data(station_input)
    if Text_predata[3:16] != "No data found":
        print(date)
        print("Metar for: ",station_data)
        station_alt = airport_alt(data,station_input)        
        print("Text: ", Text_data)
        print("Temperature: {:s}{:s}C ({:s}{:s}F)".format(celsius,degree_sign,fahrenheit,degree_sign))
        print("Dewpoint: {:s}{:s}C ({:s}{:s}F) RH= {:s}%".format(dewpoint_C,degree_sign,dewpoint_F,degree_sign,RH))
        print("Pressure: {:s} Hg ({:s} mb) SLP= {:s} mb".format(Hg,Mb,SLP))
        print("Winds: ", wind_data)
        print("Visibility: ", vis_data)     
        print("Ceiling: ",ceiling_data)
        print("Clouds: ",clouds_data)
        if weather_index != -1:
            print("Weather: ",weather_data)
            print()
            station_input = input("Input ICAO Code: ")            
        else:
            print("Weather: ", "No Weather Reported")
            print()
            station_input = input("Input ICAO Code: ")
    elif len(station_input) < 4:
        print("Station ID must have 4 characters")
        station_input = input("Input ICAO Code: ")        
    else:
        print("Station does not exist. Try Again")
        print()
        station_input = input("Input ICAO Code: ")
