###############################################################################
# Project #07
# Algorithm
#   prompts for a file
#   prompts for a year for calculations
#       gives all results for that year
#   prompts if user wants top ten for input year
#       displays a graph of the top ten for prescribed medications and Medicaid coverage
#   loops until "q" is input to quit program
###############################################################################
from operator import itemgetter
import pylab

def open_file():
    '''
    Prompts user to enter a filename. Tries to open a comma separated
    value (csv) file. An error message should be shown if the file cannot be opened.
    This function will loop until it receives proper input and successfully opens the file. It
    returns a file pointer.
    '''
    while True:
        prompt=input("Input a file name: ")
        try:
            fp= open(prompt,"r")                    # testing to see if correct input is found
            return fp
        except FileNotFoundError:                   # error if incorrect input is entered
            print("Unable to open the file. Please try again.")
def read_data(fp):
    '''
    receives a file pointer of the data file. Creates a list with year, brand,
    total spending on drug, prescriptions, units, average cost per prescription,
    average cost per unit.
    This function returns a sorted list of tuples
    '''
    data_list=[]     # creating a new list
    Avg_Pre=0
    Avg_Unit=0
    for line in fp:     # reading in file pointer
        try:
            line= line.strip().split(',')               # removing spaces and commas in file
            Avg_Pre= float(line[3])/int(line[4])        # finding average of cost per prescriptions
            Avg_Unit= float(line[3])/int(line[5])       # finding average of cost per unit
            data_list.append((int(line[0]),line[1],float(line[3]),int(line[4]),int(line[5]),Avg_Pre,Avg_Unit))  # appending columns to data_list
            data_list.sort()

        except ValueError:                  # skips values that have "n/a" values
            pass
    return data_list                        # returns a sorted list

def top_ten_list(column, year_list):
    '''
     Receives column index (integer) and a list of tuples
     containing all the medications covered for a specific year, i.e. data returned from the
     get_year_list function. This function returns two lists: (list1) containing the brand names
     of the top 10 and (list2) the values in the specified column for the top 10 tuples reverse
     order. 3 is for Medicaid coverage, 4 is for number of prescriptions.
    '''
    list1=[]            # creating two lists, one for medicaid name, and another for the column being calculated
    list2=[]
    year_list_sorted= sorted(year_list, key=itemgetter(column-1,1), reverse=True)  # sorting year_list that was created earlier for biggest to smallest for the two columns
    for j in year_list_sorted[:10]:     # looking in the sorted list for the top ten values
        medicaid=j[1]                   # looking for medicaid name in the medicaid column
        total=j[column-1]               # looking for medicaid coverage and number of presciption in the index-1 column
        list1.append(medicaid)          # adding values to the new lists
        list2.append(total)  
    return list1,list2
    
def get_year_list(year, data):
    '''
    This function receives the specified year (integer) and the list
    of tuples with the entire dataset, that is, the list returned by read_data. This function
    returns a sorted list of tuples with all the medications covered by Medicaid during the
    specified year
    '''
    year_list = []   # creating a new list called "year_list"
    year= int(year)  # making year into an integer
    for tup in data: # looking in the data file returned by read_data
        if tup[0]== year:  # reading the first column as a year and seeing if it matches input
            year_list.append(tup)
    return year_list        # returns a new list for the year input

def display_table(year, year_list):
    '''
    This function displays the following information for each
    medication in a year (sorted by brand name, A-Z): brand name, number of prescriptions,
    average prescription cost, and the total spending per medication.
    '''
    year=str(year)
    print("{:^80s}".format("Drug spending by Medicaid in "+year))    # printing header and the year input by user
    print("{:<35s}{:>15}{:>20}{:>15}".format("Medication","Prescriptions","Prescription Cost","Total")) # printing column headers
    for k in year_list:
        brand=k[1]   # extracting brand, prescription, and average from year list
        prescription=k[3]
        Avg_prescription=k[5]
        Total=k[2]/1000  # dividing total by 1000 to make the data look cleaner
        print("{:<35s}{:>15,d}{:>20,.2f}{:>15,.2f}".format(brand,prescription,Avg_prescription,Total))

    

def plot_top_ten(x, y, title, xlabel, ylabel):
    '''
        This function plots the top 10 values from a list of medications.
        This function is provided to the students.
        
        Input:
            x (list) -> labels for the x-axis
            y (list) -> values for the y-axis
            title (string) -> Plot title
            xlabel (string) -> Label title for the x-axis
            ylabel (string) -> Label title for the y-axis
    '''
    
    pos = range(10)
    pylab.bar(pos, y)
    pylab.title(title)
    pylab.xlabel(xlabel)
    pylab.ylabel(ylabel)
    pylab.xticks(pos,x, rotation='90')
    pylab.show()
    

def main():
    '''
    Opens the file and passes the file pointer to the read_data function. 
    Then prompts for a year to search in the data list and sends it to the display_table function to output.
    Then prompts whether user wants to plot the top 10 medications in the data list.
    '''
    year = ""      # setting year to be a string
    fp = open_file()   # calls open_file function
    data=read_data(fp) # takes data from read_data function
    print("Medicaid drug spending 2011 - 2015")
    year = input("Enter a year to process ('q' to terminate): ")  # prompting user for a year input
    while year != "q":       # starting loop until "q" input to quit
        while year.isdigit() or year == "q":  # loops while the input is an integer or "q", else displays error message and reprompts for year
            if year == "q":
                break
            while year != "q":   # loops while the year input isn't "q"
                year_list=get_year_list(year,data)   # calls get_year_list function
                display_table(year,year_list)     # calls the display_table function and displays results for input year
                Top_ten=input("Do you want to plot the top 10 values (yes/no)? ")  # prompts if user wants to plot top ten
                if Top_ten == "yes":   # if input for Top_ten is yes, program continues to display
                      
                    (x,y)=top_ten_list(4,year_list)   # uses the 4 index in year_list for first graph.
                    title="Top 10 Medications prescribed in "+year
                    xlabel="Medication Name"
                    ylabel="Prescriptions"
                    plot_top_ten(x,y,title,xlabel,ylabel)   # plots the first graph, continues to the next

                    (x,y)=top_ten_list(3,year_list)    # uses the 3 index in year_list for second graph
                    title="Top 10 Medicaid Covered Medications in "+year
                    xlabel="Medication Name"
                    ylabel="Amount"
                    plot_top_ten(x,y,title,xlabel,ylabel)  # plots the second graph and then reprompts to continue
                    
                    year = input("Enter a year to process ('q' to terminate): ")
                    
                elif Top_ten == "no":   # if the user does not want to print results, just reprompts.
                    year = input("Enter a year to process ('q' to terminate): ")
        else:
            print("Invalid Year. Try Again!")
            year = input("Enter a year to process ('q' to terminate): ")
    
        
if __name__ == "__main__":
    main()