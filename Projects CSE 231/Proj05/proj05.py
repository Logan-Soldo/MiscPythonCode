###############################################################################
# Project #05
# This program is used to calculate happiness based on a search keyword for Country or region
#   The program first prompts for a file name using a try-except functions
#   if an incorrect file name is input, the file name will be reprompted until found.
#   Once a correct file name is imput, prompts for a "1" for country or "2" for region
#       if something other than "1" or "2" is input, the program will reprompt for a value
#   Once a "1" or "2" is input, a keyword is then prompted for
#       read_data is called and an average is calculated
#       calls display_line within read_data
#   Program ends once a result is shown

##################################################################################
def open_file():
    while True:
        prompt=input("Input a file name: ")
        try:
            fp= open(prompt,"r")                    # testing to see if correct input is found
            return fp
        except FileNotFoundError:                   # error if incorrect input is entered
            print("Unable to open the file. Please try again.")

def read_data(fp, input_str, search_str):
    count=0
    total=0
  
    print("{:24s}{:<32s}{:<17s}".format("Country","Region","Happiness Score"))
    print("-----------------------------------------------------------------------")

    for line in fp:
        line=line.strip().split(",")
        if input_str == "1":                    # searching for country
            if search_str.lower() in line[0].lower():  #looks for lowercase of country and data file
                display_line(line[0],line[1],float(line[2]))               
                count += 1                      # count number of countries found
                total += float(line[2])         # totalling happiness_score values       
                
                
        elif input_str == "2":                  # searcing for a region
            if search_str.lower() in line[1].lower():
                display_line(line[0],line[1],float(line[2]))
                count += 1                      # count number of regions found
                total += float(line[2])         # totalling happiness_score values
                    
    average= total/count                        # taking the average of total happiness_scores and number of results found    
    print("-----------------------------------------------------------------------")    
    print("{:24s}{:>36.2f}".format("Average Happiness Score",average))
def display_line(country_name, region_name, happiness_score):
    
    print("{:24s}{:<32s}{:<17.2f}".format(country_name,region_name,happiness_score))

def main():

    fp=open_file()                          # calling open file until file found
    
    input_str=input("Input 1 to search in country names, 2 to search in regions: ") 
    
    while True:
        if input_str == "1" or input_str == "2":  
            search_str= input("What do you want to search for? ")  
            search_str= search_str.lower()
            read_data(fp,input_str,search_str)
            break
        elif input_str != "1" or input_str != "2":    #if a "1" or "2" not entered, error is prompted
            print("Invalid choice, please try again!")
            input_str=input("Input 1 to search in country names, 2 to search in regions: ")


if __name__ == '__main__':
   main()