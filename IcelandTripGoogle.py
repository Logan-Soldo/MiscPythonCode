# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 18:56:53 2019

@author: Scruffybear
"""

from random import randint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import smtplib
import time
import pandas as pd
from email.mime.multipart import MIMEMultipart

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

def start_google(city_from, city_to, date_start, date_end):
    google = ('https://www.google.com/flights?lite=0#flt={:s}.{:s}.{:s}*{:s}.{:s}.{:s};c:USD;e:1;sd:1;t:f').format(city_from,city_to,date_start,city_to,city_from,date_end)
    driver.get(google)
    time.sleep(randint(8,10))
    
    best,other = page_scrape()
    df_append = append_df(best,other)
#    print(other)
    print(df_append)
    return df_append              
              
def page_scrape():

    xp_best = '//*[@class = "gws-flights-results__result-list"]'
    best_flights = driver.find_elements_by_xpath(xp_best)

    best_res = split_lst(best_flights)   
    best = to_df(best_res)

    xp_other = '//*[@class = "gws-flights-results__has-dominated gws-flights-results__result-list"]'
    other_flights = driver.find_elements_by_xpath(xp_other)
    other_res = split_lst(other_flights) 
#    print(other_res)    
    other = to_df(other_res)

    return best,other

def split_lst(lst):
    '''
    This splits list into multiple lists based on the key "round trip"    
    '''
    for value in lst:
            lst = value.text 
    lst = lst.split('\n')    
    b_size = len(lst)
    idx_list = [idx + 1 for idx,val in enumerate(lst) if val == 'round trip']
    res = [lst[i: j] for i, j in zip([0]+idx_list, idx_list +([b_size] if idx_list[-1] != b_size else []))] 
    for s in res:
#        print(s[3][0],type(s[3][0])) 
        if (s[3][0]).isdigit():
            remove = s[2]
            s[1] = s[1] + ', ' + s[2]
            s.remove(remove)
        else:
 #           print('str')
            pass
    return res

def to_df(lst):
    cols = (['Depart Time','Airline(s)','Trip Time','Airports','Layover','layover time','Price','type'])
    df_flights = pd.DataFrame(columns = cols)
    for flights in lst:
        if len(flights) < 8:
            flights.insert(5,'NA')
#        print([flights[0]])
        df_flights = df_flights.append({'Depart Time': flights[0],
                                   'Airline(s)': flights[1],
                                   'Trip Time': flights[2],
                                   'Airports': flights[3],
                                   'Layover': flights[4],
                                   'layover time': flights[5],
                                   'Price': flights[6],
                                    'type': flights[7]},ignore_index=True)[cols]
   
        df_flights['timestamp'] = time.strftime("%Y%m%d-%H%M") # so we can know when it was scraped
#        df_flights.append(df2)
        
#    print(df_flights)
    return df_flights       

def append_df(df_best,df_other):
    append = df_best.append(df_other,ignore_index=True, sort=True)
    return append


             
driver = webdriver.Chrome()
time.sleep(3)

city_to = 'KEF'
city_from = 'EWR'
date_start = '2020-05-12'
date_end = '2020-05-21'


#for n in range(0,5):
for n in range(1):
    start_google(city_from, city_to, date_start, date_end)
    print()
    print('iteration {} was complete @ {}'.format(n, time.strftime("%Y%m%d-%H%M")))
#    Wait 4 hours
    print("sleeping for 4 hours...")
#    time.sleep(60*60*4)
    print('sleep finished.....')

driver.quit()