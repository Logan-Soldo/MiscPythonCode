# Project #02
# This program calculates 2017 tax, 2018 tax, and then calculates the
# difference and percent difference between the two taxes.
# Input a positive income, a negative will end program
#   2017 taxes are calculated
#   2018 taxes are calculated
#   difference is calculated
#   Percent difference is calculated
#   Output will round to 100th decimal place
# This program ignores tax deductions and only considers single individuals

num_str=input("Enter income as an integer with no commas: ")
income=int(num_str)
Original_income=int(num_str)
tax_sum_2017=0
tax_sum_2018=0

#2017 tax

while income >= 0:
    if income < 9326:
        tax_2017 = (income)*(0.10)
        tax_sum_2017 += tax_2017
        income = Original_income-9326
    
    elif 9326<= income <= 37950:
        tax_2017 = 9325*(0.10)
        tax_sum_2017 += tax_2017
        
        tax_2017 = (Original_income-9325)*(0.15)
        tax_sum_2017 += tax_2017
        income = 9325-Original_income
        
    elif 37951 <= income <= 91900:
        tax_2017 = 9325*(0.10) 
        tax_sum_2017 += tax_2017        
        
        tax_2017 = (37950-9325)*(0.15)
        tax_sum_2017 += tax_2017        
        
        tax_2017 = (Original_income-37950)*(0.25)
        tax_sum_2017 += tax_2017
        income = 37950-Original_income
    
    elif 91901 <= income <= 191650:
        tax_2017 = 9325*(0.10)
        tax_sum_2017 += tax_2017
        
        tax_2017 = (37950-9325)*(0.15)
        tax_sum_2017 += tax_2017
        
        tax_2017 = (91900-37950)*(0.25)
        tax_sum_2017 += tax_2017       
        
        tax_2017 = (Original_income-91900)*(0.28)
        tax_sum_2017 += tax_2017
        income = 91900-Original_income

    elif 191651 <= income <= 416700:
        tax_2017 = 9325*(0.10)
        tax_sum_2017 += tax_2017
        
        tax_2017 = (37950-9325)*(0.15)
        tax_sum_2017 += tax_2017
        
        tax_2017 = (91900-37950)*(0.25)
        tax_sum_2017 += tax_2017     
        
        tax_2017 = (191650-91900)*(0.28)
        tax_sum_2017 += tax_2017

        tax_2017 = (Original_income-191650)*(0.33)
        tax_sum_2017 += tax_2017
        income = 191650-Original_income

    elif 416701 <= income <= 418400:
        tax_2017 = 9325*(0.10)
        tax_sum_2017 += tax_2017
        
        tax_2017 = (37950-9325)*(0.15)
        tax_sum_2017 += tax_2017 
        
        tax_2017 = (91900-37950)*(0.25)
        tax_sum_2017 += tax_2017      
        
        tax_2017 = (191650-91900)*(0.28)
        tax_sum_2017 += tax_2017

        tax_2017 = (416700-191650)*(0.33)
        tax_sum_2017 += tax_2017

        tax_2017 = (Original_income-416700)*(0.35)
        tax_sum_2017 += tax_2017
        income = 416700-Original_income

    elif income > 418400:
        tax_2017 = 9325*(0.10)
        tax_sum_2017 += tax_2017
        
        tax_2017 = (37950-9325)*(0.15)
        tax_sum_2017 += tax_2017 
        
        tax_2017 = (91900-37950)*(0.25)
        tax_sum_2017 += tax_2017       
        
        tax_2017 = (191650-91900)*(0.28)
        tax_sum_2017 += tax_2017

        tax_2017 = (416700-191650)*(0.33)
        tax_sum_2017 += tax_2017  

        tax_2017 = (418400-416700)*(0.35)
        tax_sum_2017 += tax_2017

        tax_2017 = (Original_income-418400)*(0.396)
        tax_sum_2017 += tax_2017
        income = 418400-income             
               
    
    #2018 tax
    income=int(num_str)
    Original_income=int(num_str)
    
    while income >= 0:
        if income <= 9525:
            tax_2018 = (income)*(0.10)
            tax_sum_2018 += tax_2018
            income = Original_income-9526
        
        elif 9526<= income <= 38700:
            tax_2018 = 9525*(0.10)
            tax_sum_2018 += tax_2018
            
            tax_2018 = (Original_income-9525)*(0.12)
            tax_sum_2018 += tax_2018
            income = 9525-Original_income
            
        elif 38701 <= income <= 82500:
            tax_2018 = 9525*(0.10) 
            tax_sum_2018 += tax_2018        
            
            tax_2018 = (38700-9525)*(0.12)
            tax_sum_2018 += tax_2018        
            
            tax_2018 = (Original_income-38700)*(0.22)
            tax_sum_2018 += tax_2018
            income = 38700-Original_income
        
        elif 82501 <= income <= 157500:
            tax_2018 = 9525*(0.10)
            tax_sum_2018 += tax_2018
            
            tax_2018 = (38700-9525)*(0.12)
            tax_sum_2018 += tax_2018
            
            tax_2018 = (82500-38700)*(0.22)
            tax_sum_2018 += tax_2018       
            
            tax_2018 = (Original_income-82500)*(0.24)
            tax_sum_2018 += tax_2018
            income = 82500-Original_income
    
        elif 157501 <= income <= 200000:
            tax_2018 = 9525*(0.10)
            tax_sum_2018 += tax_2018
            
            tax_2018 = (38700-9525)*(0.12)
            tax_sum_2018 += tax_2018
            
            tax_2018 = (82500-38700)*(0.22)
            tax_sum_2018 += tax_2018     
            
            tax_2018 = (157500-82500)*(0.24)
            tax_sum_2018 += tax_2018
    
            tax_2018 = (Original_income-157500)*(0.32)
            tax_sum_2018 += tax_2018
            income = 157500-income
    
        elif 200001 <= income <= 500000:
            tax_2018 = 9525*(0.10)
            tax_sum_2018 += tax_2018
            
            tax_2018 = (38700-9525)*(0.12)
            tax_sum_2018 += tax_2018
            
            tax_2018 = (82500-38700)*(0.22)
            tax_sum_2018 += tax_2018     
            
            tax_2018 = (157500-82500)*(0.24)
            tax_sum_2018 += tax_2018
    
            tax_2018 = (200000-157500)*(0.32)
            tax_sum_2018 += tax_2018
    
            tax_2018 = (Original_income-200000)*(0.35)
            tax_sum_2018 += tax_2018
            income = 200000-income
    
        elif income > 500000:
            tax_2018 = 9525*(0.10)
            tax_sum_2018 += tax_2018
            
            tax_2018 = (38700-9525)*(0.12)
            tax_sum_2018 += tax_2018
            
            tax_2018 = (82500-38700)*(0.22)
            tax_sum_2018 += tax_2018     
            
            tax_2018 = (157500-82500)*(0.24)
            tax_sum_2018 += tax_2018
    
            tax_2018 = (200000-157500)*(0.32)
            tax_sum_2018 += tax_2018
    
            tax_2018 = (500000-200000)*(0.35)
            tax_sum_2018 += tax_2018
    
            tax_2018 = (Original_income-500000)*(0.37)
            tax_sum_2018 += tax_2018
            income = 500000-income 
                  
 
# difference



    Difference= tax_sum_2018-tax_sum_2017
    Per_Difference= ((tax_sum_2017-tax_sum_2018)/tax_sum_2017)*100
                    
#Print                    
    print("Income:", num_str)
    print("2017 tax:",round(tax_sum_2017,2))
    print("2018 tax:",round(tax_sum_2018,2))
    print("Difference:",round(Difference,2))
    print("Difference (percent):",round(Per_Difference,2))

    num_str=input("Enter income as an integer with no commas: ")
    income=int(num_str)
    Original_income=int(num_str)
    tax_sum_2017=0
    tax_sum_2018=0

    continue    
           