import netCDF4
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
import xarray as xr

nc = netCDF4.Dataset('air.sig995.2015.nc')

lat = nc.variables['lat'][:]
lon = nc.variables['lon'][:]
time_var = nc.variables['time']
dtime = netCDF4.num2date(time_var[:],time_var.units)
temp = nc.variables['air'][:]

print(temp)

# determine what longitude convention is being used [-180,180], [0,360]
print (lon.min(),lon.max())
print(nc)

# specify some location to extract time series
lati = 66.14; loni = -22.2 + 365  # CHANGE HERE DEPENDING ON LOCATION

# find closest index to specified value
def near(array,value):
    idx=(abs(array-value)).argmin()
    return idx

# Find nearest point to desired location (could also interpolate, but more work)
ix = near(lon, loni)
iy = near(lat, lati)

# Extract desired times.      
# 1. Select -+some days around the current time:
#start = dtime.datetime.utcnow()- dtime.timedelta(days=3)
#stop = dtime.datetime.utcnow()+ dtime.timedelta(days=3)
#       OR
# 2. Specify the exact time period you want:   CHANGE DATE RANGE HERE
start = dt.datetime(2015,1,1,0,0,0)
stop = dt.datetime(2015,12,31,0,0,0)

istart = netCDF4.date2index(start,time_var,select='nearest')
istop = netCDF4.date2index(stop,time_var,select='nearest')
print (istart,istop)

# Get all time records of variable [vname] at indices [iy,ix]
vname = 'Significant_height_of_wind_waves_surface'
#vname = 'surf_el'
var = nc.variables['air']
hs = var[istart:istop,iy,ix]
tim = dtime[istart:istop]

# Create Pandas time series object
ts = pd.Series(hs,index=tim,name=vname)

# Use Pandas time series plot method
ts.plot(figsize=(12,4))
title=plt.title('Location:Lat=%.2f, Lon=%.2f, ' %(lat[iy],lon[ix]))
plt.ylabel(var.units);

#write to a CSV file
ts.to_csv('time_series_from_netcdf.csv')