###############################################################################
# Project #03
# This program is a currency conversion. 
#   Input the starting currency (ex. usd)
#   Input the currency that is being converted to (ex. eur)
#   Input an integer amount to be converted from the starting currency to the new currency
#   The program will output the conversion based on finance.google.com's converter
#   The program asks if you'd like to do another conversion, ending if answer is 'no'
# If a non-integer is input, the program will re-ask for another amount

import urllib.request
Orig_Currency_str = input("What is the original currency? ")        #prompting for inputs
Currency_str= input ("What do you want to convert to? ")            #prompting for inputs
Currency_amt = input("How much do you want to convert (int)? ")     #prompting for inputs

Orig_Currency=Orig_Currency_str.upper()
Currency= Currency_str.upper()
Again= '' 
Again= Again.lower()                            


while Again != 'no':                        # loop will run as long as user keeps prompting to re-run the program
    if Currency_amt.isdigit():              # If an integer is input, the program will continue
        Currency_int=int(Currency_amt)
        URL_str = "https://finance.google.com/finance/converter?a={:d}&from={:s}&to={:s}".format(Currency_int,Orig_Currency,Currency)  # Generating URL from inputs
        
        url= URL_str
        response= urllib.request.urlopen(url)
        result= str(response.read())
        index= result.find("class=bld>")       # finding output to splice
        End_index= result.find("</span>")
        Conversion=result[index:End_index]
        Value= Conversion[10:-4]               # splicing output
        Value_float= float(Value)       
        Currency_find= Conversion[-4:]         # splicing input currency
        print(Currency_int,Orig_Currency,"is",round(Value_float,2),Currency)  #Rounding output value to the 100th decimal place
        
        Again = input("Do you want to convert another currency? ")  #asking if the user would like to convert again
        Again= Again.lower()
        if Again == 'no':                  # if user answers 'no', program will end 
            exit
        elif Again != 'no':                # if user answers anything else, the program will reprompt and loop will restart
            Orig_Currency_str = input("What is the original currency? ")
            Currency_str= input ("What do you want to convert to? ")
            Currency_amt = input("How much do you want to convert (int)? ")
            Orig_Currency=Orig_Currency_str.upper()
            Currency= Currency_str.upper()
            Again= '' 
            Again= Again.lower()            
        
    elif not Currency_amt.isdigit():    # If a non integer is input, an error will be presented and the loop will be re-run
         print("The value you input must be an integer. Please try again")
         Currency_amt = input("How much do you want to convert (int)? ")
         
              

else:
    exit