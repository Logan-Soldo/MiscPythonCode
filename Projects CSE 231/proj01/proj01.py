############################################################################################ 
#   Project 1
#   Converts Rods to meter,feet,miles,furlong,and time it takes to walk any number of rods
#       Input number of rods
#       Output conversion rounded to 3rd digit
#
###########################################################################################

Rod= 5.0292     # 1 rod for every 5.0292 meters
Furlong= 40     # 1 furlong for every 40 rods
Mile= 1609.34   # 1 mile for every 1609.34 meters
Foot= 0.3048    # 1 foot for every 0.3048 meters
Speed= 3.1      # average walking speed of 3.1 mi/hr
Minutes=60      # 60 minutes every 1 hour

#Input number of rods to convert
num_str1 = input('Input rods: ')


float1 = float(num_str1)


print('You input',float1,'rods.')

#Conversions

print('Conversions')

Meter_1= float1*Rod
Feet_1= Meter_1/Foot
Miles_1= Meter_1/Mile
Furlong_1= float1/Furlong
Walk_1= ((Speed*Mile/Rod)/float1)
Time_1= Minutes/Walk_1

print('Meters:', round(Meter_1,3))
print('Feet:', round(Feet_1,3))
print('Miles:', round(Miles_1,3))
print('Furlongs:', round(Furlong_1,3))  
print('Minutes to walk', float1, 'rods:', round(Time_1,3))

#End Program