# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 12:20:08 2019

@author: Scruffybear
"""

from random import randint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import smtplib
import time
import pandas as pd
from email.mime.multipart import MIMEMultipart
#
##browser = webdriver.Chrome(executable_path='/chromedriver')


# Load more results to maximize the scraping

def load_more():
    try:
        more_results = '//a[@class = "moreButton"]'
        driver.find_element_by_xpath(more_results).click()
        print('sleeping.....')
        time.sleep(randint(25,35))
    except:
        pass
# Close Popup #####################################################################################################
def close_popup():
    print("closing popup...")
    # sometimes a popup shows up, so we can use a try statement to check it and close
  #  time.sleep(randint(60,95))   
    try:
        xp_popup_close = '//button[contains(@id,"dialog-close") and contains(@class,"Button-No-Standard-Style close ")]'
        driver.find_elements_by_xpath(xp_popup_close)[5].click()
        time.sleep(randint(60,95))        
    except Exception as e:
        pass    
    try:
        print("trying other closing method")
#        xp_popup_close = '//*[contains(@href,"javascript:void(0)") and contains(@aria-label,"Close")]]'
#        driver.find_element_by_xpath(xp_popup_close).submit()
        driver.find_element_by_xpath("//body").click()
    except Exception as e:
        pass
###################################################################################################################
        

#for flight in flight_containers:
#    print(flight)
def start_kayak_air(city_from, city_to, date_start, date_end):
    """City codes - it's the IATA codes!
    Date format -  YYYY-MM-DD"""
    
    kayak_air = ('https://www.kayak.com/flights/' + city_from + '-' + city_to +
             '/' + date_start + '-flexible/' + date_end + '-flexible?sort=bestflight_a')
    driver.get(kayak_air)
    time.sleep(randint(8,10))
    
    # sometimes a popup shows up, so we can use a try statement to check it and close
    close_popup()
    print('loading more.....')
    
#     load_more()
    
    print('starting first scrape.....')
    df_flights_best = page_scrape()
    df_flights_best['sort'] = 'best'
    time.sleep(randint(60,80))
    
    # Let's also get the lowest prices from the matrix on top
#    matrix = driver.find_elements_by_xpath('//*[contains(@id,"FlexMatrixCell")]')
#    matrix_prices = [price.text.replace('$','') for price in matrix]
#    matrix_prices = list(map(int, matrix_prices))
#    matrix_min = min(matrix_prices)
#    matrix_avg = sum(matrix_prices)/len(matrix_prices)
    
    print('switching to cheapest results.....')
    cheap_results = '//a[@data-code = "price"]'
    driver.find_element_by_xpath(cheap_results).click()
    time.sleep(randint(60,90))
    print('loading more.....')
    
#     load_more()
    
    print('starting second scrape.....')
    df_flights_cheap = page_scrape()
    df_flights_cheap['sort'] = 'cheap'
    time.sleep(randint(60,80))
    
    print('switching to quickest results.....')
    quick_results = '//a[@data-code = "duration"]'
    driver.find_element_by_xpath(quick_results).click()  
    time.sleep(randint(60,90))
    print('loading more.....')
    
#     load_more()
    
    print('starting third scrape.....')
    df_flights_fast = page_scrape()
    df_flights_fast['sort'] = 'fast'
    time.sleep(randint(60,80))
    
    # saving a new dataframe as an excel file. the name is custom made to your cities and dates
    final_df = df_flights_cheap.append(df_flights_best).append(df_flights_fast)
    
    
    print('saved df.....')
    
    # We can keep track of what they predict and how it actually turns out!
    xp_loading = '//div[contains(@id,"advice")]'
    loading = driver.find_element_by_xpath(xp_loading).text
    xp_prediction = '//span[@class="info-text"]'
    prediction = driver.find_element_by_xpath(xp_prediction).text
    print(loading+'\n'+prediction)
    
    # sometimes we get this string in the loading variable, which will conflict with the email we send later
    # just change it to "Not Sure" if it happens
    weird = '¯\\_(ツ)_/¯'
    if loading == weird:
        loading = 'Not sure'

# exporting results to csv and email
    
    to_excel(final_df,city_from,city_to,date_start,date_end)    
    to_email(city_from,city_to,date_start,date_end,matrix_min,matrix_avg,prediction,loading)
    

    
def start_kayak_car(city_to, date_start, date_end):
    kayak_car = 'https://www.kayak.com/cars/{:s}-a11024/{:s}/{:s}?sort=rank_a&fs=caroption=Automatic;caragency=-greenmotion'.format(city_to,date_start,date_end)
    driver.get(kayak_car)
    time.sleep(randint(8,10))
    
    # sometimes a popup shows up, so we can use a try statement to check it and close
    close_popup()
    print('loading more.....')
    
#     load_more()
    
    print('starting small scrape.....')
#    small_results = '//*[@class="_ioQ _icg _iWa _h-Y _iWb _in7"]'
    small_results = '//*[contains(@id,"SMALL-only")]'
    button = driver.find_element_by_xpath(small_results)
    driver.execute_script("arguments[0].click();",button)
    time.sleep(randint(20,30))
    
    df_car_small = car_scrape()
    df_car_small['sort'] = 'small' 
    time.sleep(randint(20,30))
    
    # Let's also get the lowest prices from the matrix on top
#    matrix = driver.find_elements_by_xpath('//*[contains(@id,"FlexMatrixCell")]')
#    matrix_prices = [price.text.replace('$','') for price in matrix]
#    matrix_prices = list(map(int, matrix_prices))
#    matrix_min = min(matrix_prices)
#    matrix_avg = sum(matrix_prices)/len(matrix_prices)
    
    print('switching to suv results.....')
    close_popup()
    suv_results = '//*[contains(@id,"SUV-only")]'
    button = driver.find_element_by_xpath(suv_results)
    driver.execute_script("arguments[0].click();",button)
    time.sleep(randint(20,30))
    print('loading more.....')
    
#     load_more()
    
    print('starting suv scrape.....')
    df_car_suv = car_scrape()
    df_car_suv['sort'] = 'suv'
    time.sleep(randint(20,30))
    
    print('switching to van results.....')
    close_popup()
    van_results = '//*[contains(@id,"VAN-only")]'
    button = driver.find_element_by_xpath(van_results)
    driver.execute_script("arguments[0].click();",button)
    time.sleep(randint(20,30))
    print('loading more.....')
    
#     load_more()
    
    print('starting van scrape.....')
    df_car_van = car_scrape()
    df_car_van['sort'] = 'van'
    time.sleep(randint(20,30))
    
    trend = '//*[@class="_iJx"]'
    deal = '//*[@id="ldmo"]/div/div/div[2]/span'
    trend_report = driver.find_element_by_xpath(trend).text
    deal_report = driver.find_element_by_xpath(deal).text
    
    print(trend_report,deal_report)
    
    return
def page_scrape():
    """This function takes care of the scraping part"""
    
    xp_sections = '//*[@class="section duration"]'
    sections = driver.find_elements_by_xpath(xp_sections)
    sections_list = [value.text for value in sections]
    section_a_list = sections_list[::2] # This is to separate the two flights
    section_b_list = sections_list[1::2] # This is to separate the two flights
    
    # if you run into a reCaptcha, you might want to do something about it
    # you will know there's a problem if the lists above are empty
    # this if statement lets you exit the bot or do something else
    # you can add a sleep here, to let you solve the captcha and continue scraping
    # i'm using a SystemExit because i want to test everything from the start
    if section_a_list == []:
        raise SystemExit
        
    
    # I'll use the letter A for the outbound flight and B for the inbound
    a_duration = []
    a_section_names = []
    for n in section_a_list:
        # Separate the time from the cities
        a_section_names.append(''.join(n.split()[2:5]))
        a_duration.append(''.join(n.split()[0:2]))
    b_duration = []
    b_section_names = []
    for n in section_b_list:
        # Separate the time from the cities
        b_section_names.append(''.join(n.split()[2:5]))
        b_duration.append(''.join(n.split()[0:2]))

    xp_dates = '//div[@class="section date"]'
    dates = driver.find_elements_by_xpath(xp_dates)
    dates_list = [value.text for value in dates]
    a_date_list = dates_list[::2]
    b_date_list = dates_list[1::2]

    try:
        xp_popup_close = '//*[@id="bd1Z-close"]'
        driver.find_elements_by_xpath(xp_popup_close)[5].click()
    except Exception as e:
        pass
    time.sleep(randint(60,95))    


    # Separating the weekday from the day
    a_day = [value.split()[0] for value in a_date_list]
    a_weekday = [value.split()[1] for value in a_date_list]
    b_day = [value.split()[0] for value in b_date_list]
    b_weekday = [value.split()[1] for value in b_date_list]
    
    # getting the prices
    xp_prices = '//*[@class="price-text"]'
    prices = driver.find_elements_by_xpath(xp_prices)
    prices_list = [price.text.replace('$','') for price in prices if price.text != '']
    prices_list = list(map(int, prices_list))

    # the stops are a big list with one leg on the even index and second leg on odd index
    xp_stops = '//div[@class="section stops"]/div[1]'
    stops = driver.find_elements_by_xpath(xp_stops)
    stops_list = [stop.text[0].replace('n','0') for stop in stops]
    a_stop_list = stops_list[::2]
    b_stop_list = stops_list[1::2]

    xp_stops_cities = '//div[@class="section stops"]/div[2]'
    stops_cities = driver.find_elements_by_xpath(xp_stops_cities)
    stops_cities_list = [stop.text for stop in stops_cities]
    a_stop_name_list = stops_cities_list[::2]
    b_stop_name_list = stops_cities_list[1::2]
    
    # this part gets me the airline company and the departure and arrival times, for both legs
    xp_schedule = '//div[@class="section times"]'
    schedules = driver.find_elements_by_xpath(xp_schedule)
    hours_list = []
    carrier_list = []
    for schedule in schedules:
        hours_list.append(schedule.text.split('\n')[0])
        carrier_list.append(schedule.text.split('\n')[1])
    # split the hours and carriers, between a and b legs
    a_hours = hours_list[::2]
    a_carrier = carrier_list[::2]
    b_hours = hours_list[1::2]
    b_carrier = carrier_list[1::2]

    
    cols = (['Out Day', 'Out Time', 'Out Weekday', 'Out Airline', 'Out Cities', 'Out Duration', 'Out Stops', 'Out Stop Cities',
            'Return Day', 'Return Time', 'Return Weekday', 'Return Airline', 'Return Cities', 'Return Duration', 'Return Stops', 'Return Stop Cities',
            'Price'])
#    print(len(a_day),len(a_weekday),len(a_duration),len(a_section_names),len(b_day),len(b_weekday),len(b_duration),len(b_section_names),len(a_stop_list),len(a_stop_name_list),len(b_stop_list),len(b_stop_name_list),len(a_carrier),len(b_hours),len(b_carrier),len(prices_list))
 
    flights_df = pd.DataFrame({'Out Day': a_day,
                               'Out Weekday': a_weekday,
                               'Out Duration': a_duration,
                               'Out Cities': a_section_names,
                               'Return Day': b_day,
                               'Return Weekday': b_weekday,
                               'Return Duration': b_duration,
                               'Return Cities': b_section_names,
                               'Out Stops': a_stop_list,
                               'Out Stop Cities': a_stop_name_list,
                               'Return Stops': b_stop_list,
                               'Return Stop Cities': b_stop_name_list,
                               'Out Time': a_hours,
                               'Out Airline': a_carrier,
                               'Return Time': b_hours,
                               'Return Airline': b_carrier,                           
                               'Price': prices_list})[cols]
    
    flights_df['timestamp'] = time.strftime("%Y%m%d-%H%M") # so we can know when it was scraped
#    print(flights_df)
    return flights_df

def car_scrape():

    xp_prices = '//*[@class="_ip2 _mou"]'
    prices = driver.find_elements_by_xpath(xp_prices)
#    print(prices)
    prices_list = [price.text.replace('$','') for price in prices if price.text != '']
    prices_list = list(map(int, prices_list))
 #   print(len(prices_list))
    
    if prices_list == []:
        raise SystemExit

#    xp_agency = '//*[@class="_iaf _ipQ _iaM _iai _isu _iqq _ia- _iKB _igO "]'
#    xp_agency = '//b[contains(@alt,"Car agency: ")]'
    xp_agency = '//*[@class="_iOA _iyS _ifp _iMT"]'
    agencies = driver.find_elements_by_xpath(xp_agency)
 #   print(agencies.text)
    agency_list = [agency.get_attribute("alt")[12:] for agency in agencies]
#    print(agency_list)
#    print(len(agency_list))
    
    xp_rating = '//*[@class="_iaf _ipQ _iaM _iai _isu _iqq _ia- _iKB _igO "]'
    ratings = driver.find_elements_by_xpath(xp_rating)
    rating_list = [rating.text for rating in ratings]
#    rating_list = [float(i) for i in rating_list]
    rating_list2 = []
    for i in rating_list:
        if i != '':
            rating_list2.append(float(i))
        else:
            rating_list2.append('N/A')
 #   print(rating_list2)
 #   rating_list = list(map(float, rating_list))
#    print(len(rating_list))
    
    xp_location = '//*[@class="_id7 _mou _iBi _iir"]'
    locations = driver.find_elements_by_xpath(xp_location)
    location_list = [location.text for location in locations if location.text != '']
#    print(len(location_list))
    
    xp_car = '//*[@class="_iMq _mou _iBk"]'
    cars = driver.find_elements_by_xpath(xp_car)
    car_list = [car.text for car in cars if car.text != '']

#    print(len(car_list))
    
    cols =(['Agency','Rating','Location','Car Type','Price'])
    car_df = pd.DataFrame({'Agency':agency_list,
                           'Rating':rating_list2,
                           'Location':location_list,
                           'Car Type':car_list,
                           'Price':prices_list,})[cols]
    
    car_df['timestamp'] = time.strftime("%Y%m%d-%H%M") # so we can know when it was scraped
    car_df.sort_values(by=['Price','Rating'])
    print(car_df)
    return car_df
    
def to_excel(df,city_from,city_to,date_start,date_end):
    df.to_excel('search_backups//{}_flights_{}-{}_from_{}_to_{}.xlsx'.format(time.strftime("%Y%m%d-%H%M"),
                                                                                   city_from, city_to, 
                                                                                   date_start, date_end), index=False)    
    
def to_email(city_from,city_to,date_start,date_end,matrix_min,matrix_avg,prediction,loading):
    print("input email and password of email you would like to send from...")
    username = input("input email: ")
    password = input('input password: ')
    print("Where would you like to send results?")
    email_to = input("send email to: ")
    server = smtplib.SMTP('smtp.outlook.com', 587)
    server.ehlo()
    server.starttls()
    server.login(username, password)
    msg = ('Subject: Flight Scraper\n\n\
     For {:s}-{:s} from {:s} to {:s}\n\
     Cheapest Flight: {}$\nAverage Price: {}$\n\nRecommendation: {}\n\nEnd of message'.format(city_from,city_to,date_start,date_end,matrix_min, matrix_avg, (loading+'\n'+prediction)))
    message = MIMEMultipart()
    message['From'] = username
    message['to'] = email_to
    server.sendmail(username, email_to, msg)
    print('sent email.....')


def main():
    time.sleep(3)
    
    city_to = 'KEF'
    city_from = 'EWR'
    date_start = '2020-05-12'
    date_end = '2020-05-21'
    
    
    for n in range(0,5):
#        start_kayak_air(city_from, city_to, date_start, date_end)
        start_kayak_car(city_to,date_start,date_end)
        print('iteration {} was complete @ {}'.format(n, time.strftime("%Y%m%d-%H%M")))
    #    Wait 4 hours
        print("sleeping for 4 hours...")
  #      time.sleep(60*60*4)
        print('sleep finished.....')

    driver.quit()

if __name__ == "__main__":
    driver = webdriver.Chrome()    
    main() 






##price = driver.find_element_by_css_selector(flight_find).text
##airline = driver.find_element_by_css_selector(airline_find).text
##print(flights)
#line_list = []
#flight_list = []
##flights = flights.split('\n',',')
##flights = flights.replace('\n',',')
##flights = flights.split(',')
##flight_list.append(flights)
##print(flights)
#
#line_list = flights[6:29]
#print(line_list)
#start = 0
#end = 7
#idex2 = 0
#for l in line_list:
#    idex = line_list.index('round trip')
#    for i in range(idex):
#      #  print(idex2,idex)
#        flight_list += [line_list[idex2:idex]]
##        print(idex2,idex)
#    idex2 = idex
       
#    print(flight_list)    
#print(flight_list)
#print(flights)
#print(result)

#<div class="flt-subhead1 gws-flights-results__price gws-flights-results__cheapest-price">      $371   </div>
#//*[@id="flt-app"]/div[2]/main[4]/div[7]/div[1]/div[5]/div[1]/ol/li[1]/div/div[1]/div[2]/div[1]/div[1]/div[5]/div[1]

#//*[@id="flt-popup"]