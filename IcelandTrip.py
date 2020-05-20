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



# Load more results to maximize the scraping

def load_more(driver):
    try:
        more_results = '//a[@class = "moreButton"]'
        driver.find_element_by_xpath(more_results).click()
        print('sleeping.....')
        time.sleep(randint(25,35))
    except:
        pass
# Close Popup #####################################################################################################
def close_popup(driver):
    '''
    Kayak is annoying and will throw popups (mainly to deter from page scraping like this), 
        but we are smarter than that and can just work around these issues.
    '''
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
        exit
    except Exception as e:
        pass
    try:
        print("trying final method")
        xp_popup_close = '//*[contains(@id,"dialog-close") and contains(@aria-label,"Close") and contains(@class,"Button")]'
        driver.find_element_by_xpath(xp_popup_close).submit()
        exit
    except Exception as e:
        pass
    try:
        print("close window")
        browser.close()
    except:
        pass
###################################################################################################################
        

#for flight in flight_containers:
#    print(flight)
def start_kayak_air(driver,username,password,email_to,city_from, city_to, date_start, date_end):
    """City codes - it's the IATA codes!
    Date format -  YYYY-MM-DD"""
    
    kayak_air = ('https://www.kayak.com/flights/' + city_from + '-' + city_to +
             '/' + date_start + '-flexible/' + date_end + '-flexible?sort=bestflight_a')
    driver.get(kayak_air)
    time.sleep(randint(10,20))
    
    # sometimes a popup shows up, so we can use a try statement to check it and close
    close_popup(driver)
    print('loading more.....')
    
#     load_more()
    
    print('starting first scrape.....')
    df_flights_best = page_scrape(driver)
    df_flights_best['sort'] = 'best'
    time.sleep(randint(10,20))
    
    # Let's also get the lowest prices from the matrix on top
#    matrix = driver.find_elements_by_xpath('//*[contains(@id,"FlexMatrixCell")]')
#    matrix_prices = [price.text.replace('$','') for price in matrix]
#    matrix_prices = list(map(int, matrix_prices))
#    matrix_min = min(matrix_prices)
#    matrix_avg = sum(matrix_prices)/len(matrix_prices)
    
    print('switching to cheapest results.....')
    cheap_results = '//a[@data-code = "price"]'
    driver.find_element_by_xpath(cheap_results).click()
    time.sleep(randint(10,20))
    print('loading more.....')
    
#     load_more()
    
    print('starting second scrape.....')
    df_flights_cheap = page_scrape(driver)
    df_flights_cheap['sort'] = 'cheap'
    time.sleep(randint(10,20))
    
    print('switching to quickest results.....')
    quick_results = '//a[@data-code = "duration"]'
    driver.find_element_by_xpath(quick_results).click()  
    time.sleep(randint(10,20))
    print('loading more.....')
    
#     load_more()
    
    print('starting third scrape.....')
    df_flights_fast = page_scrape(driver)
    df_flights_fast['sort'] = 'fast'
    time.sleep(randint(10,20))
    
    # saving a new dataframe as an excel file. the name is custom made to your cities and dates
    final_df = df_flights_cheap.append(df_flights_best).append(df_flights_fast)
    sort_flight = final_df.sort_values(['Out Stops','Price'])
    cheapest = sort_flight['Price'].min()
    average = sort_flight['Price'].mean()    # need to round
    average = round(average,2)
    
    print('saved df.....')
    
    # We can keep track of what they predict and how it actually turns out!
    try:
        xp_loading = '//div[contains(@id,"advice")]'
        loading = driver.find_element_by_xpath(xp_loading).text
    except:
        loading = "no advice"
    try:
        xp_prediction = '//span[@class="info-text"]'
        prediction = driver.find_element_by_xpath(xp_prediction).text
    except:
        prediction = "no prediction"
    print(loading+'\n'+prediction)
    
    # sometimes we get this string in the loading variable, which will conflict with the email we send later
    # just change it to "Not Sure" if it happens
    weird = '¯\\_(ツ)_/¯'
    if loading == weird:
        loading = 'Not sure'

# exporting results to csv and email
    
    to_excel(final_df,city_from,city_to,date_start,date_end)    
#    to_email(city_from,city_to,date_start,date_end,matrix_min,matrix_avg,prediction,loading)
    to_email(username,password,email_to,city_from,city_to,date_start,date_end,cheapest,average,prediction,loading)
    

    
def start_kayak_car(driver,username,password,email_to,city_to, date_start, date_end):
    while True:
        try:
            kayak_car = 'https://www.kayak.com/cars/{:s}-a11024/{:s}/{:s}?sort=rank_a&fs=caroption=Automatic;caragency=-greenmotion'.format(city_to,date_start,date_end)
            driver.get(kayak_car)
            time.sleep(randint(8,10))
            
            # sometimes a popup shows up, so we can use a try statement to check it and close
            close_popup(driver)
            print('loading more.....')
            
        #     load_more()
            
            print('starting small scrape.....')
        #    small_results = '//*[@class="_ioQ _icg _iWa _h-Y _iWb _in7"]'
            small_results = '//*[contains(@id,"SMALL-only")]'
            button = driver.find_element_by_xpath(small_results)
            driver.execute_script("arguments[0].click();",button)
            time.sleep(randint(10,20))
            
            df_car_small = car_scrape()
            df_car_small['sort'] = 'small' 
            time.sleep(randint(10,20))
            
            # Let's also get the lowest prices from the matrix on top
        #    matrix = driver.find_elements_by_xpath('//*[contains(@id,"FlexMatrixCell")]')
        #    matrix_prices = [price.text.replace('$','') for price in matrix]
        #    matrix_prices = list(map(int, matrix_prices))
        #    matrix_min = min(matrix_prices)
        #    matrix_avg = sum(matrix_prices)/len(matrix_prices)
            
            print('switching to suv results.....')
      #      close_popup(driver)
            suv_results = '//*[contains(@id,"SUV-only")]'
            button = driver.find_element_by_xpath(suv_results)
            driver.execute_script("arguments[0].click();",button)
            time.sleep(randint(10,20))
            print('loading more.....')
            
        #     load_more()
            
            print('starting suv scrape.....')
            df_car_suv = car_scrape()
            df_car_suv['sort'] = 'suv'
            time.sleep(randint(10,20))
            
            print('switching to van results.....')
       #     close_popup()
            van_results = '//*[contains(@id,"VAN-only")]'
            button = driver.find_element_by_xpath(van_results)
            driver.execute_script("arguments[0].click();",button)
            time.sleep(randint(10,20))
            print('loading more.....')
            
        #     load_more()
            
            print('starting van scrape.....')
            df_car_van = car_scrape()
            df_car_van['sort'] = 'van'
            time.sleep(randint(10,20))
            
            trend = '//*[@class="_iJx"]'
            deal = '//*[@id="ldmo"]/div/div/div[2]/span'
            trend_report = driver.find_element_by_xpath(trend).text
            deal_report = driver.find_element_by_xpath(deal).text
            return deal_report
        except:
            close_popup(driver)
    
    print(trend_report,deal_report)
    
    return
def page_scrape(driver):
    """This function takes care of the scraping part"""
    
    xp_sections = '//*[@class="section duration allow-multi-modal-icons"]'
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
        print("issues")
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
                               'Price': prices_list})[cols].fillna('nan')
    
    flights_df['timestamp'] = time.strftime("%Y%m%d-%H%M") # so we can know when it was scraped
    print(flights_df)
    return flights_df

def car_scrape(driver):

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
  
    
def email_details():
    '''
    Logging into email account, this allows the user to send results to their 
        email.
    This function will return an error if the password is wrong.
    '''
    try:
        print("input email and password of email you would like to send from...")
        username = 'scruffypi55@gmail.com'
        password = input('input password: ')
        print("Where would you like to send results?")
        email_to = input("send email to: ")
        return username,password,email_to
    except:
        print("Something went wrong when logging in...")
    
def to_email(username,password,email_to,city_from,city_to,date_start,date_end,cheapest,average,prediction,loading):
    '''
    sending email to the user as requested. Takes in the login information as
        well as the results from the scraping.
    This function will have to be called in a different place with combined car 
        rental and airfare.
    '''
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(username, password)
    msg = ('Subject: Flight Scraper\n\n\
    For {:s}-{:s}\nFrom {:s} to {:s}\n Cheapest Flight: {}$\nAverage Price: {}$\n\nRecommendation: {}\n\nEnd of message'.format(city_from,city_to,date_start,date_end,cheapest,average, (loading+'\n'+prediction)))
    message = MIMEMultipart()
    message['From'] = username
    message['to'] = email_to
    server.sendmail(username, email_to, msg)
    print('sent email.....')


def main():
    time.sleep(3)    
    
    
    city_to = 'KEF'
    city_from = 'EWR'
    date_start = '2020-08-12'
    date_end = '2020-08-21'

    
    for n in range(0,5):
        print(('Starting Airfare: Run #{}').format(n+1))
        driver = webdriver.Firefox()
        start_kayak_air(driver,username,password,email_to,city_from, city_to, date_start, date_end)
        driver.close()

        driver = webdriver.Firefox()        
        print(('Starting Car Rental: Run #{}').format(n+1))
        deal_report = start_kayak_car(driver,username,password,email_to,city_to,date_start,date_end)
        driver.close()
        print('iteration {} was complete @ {}'.format(n, time.strftime("%Y%m%d-%H%M")))
    #    Wait 4 hours
        print("sleeping for 4 hours...")
  #      time.sleep(60*60*4)
        print('sleep finished.....')

    driver.quit()

if __name__ == "__main__":
        #browser = webdriver.Firefox(executable_path='/chromedriver')
    username,password,email_to = email_details()
    browser= webdriver.Firefox()
#    driver = webdriver.Chrome()
#    driver = webdriver.Firefox()    
    main() 
