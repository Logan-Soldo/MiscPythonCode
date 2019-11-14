
import csv
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
            
def read_file(fp):
    data={}
    data_list=[]        
    reader=csv.reader(fp)
    header= next(reader,None)
    previous_city,previous_date = "",""
    for line_list in reader:
        if line_list[13] == '':
            continue
        if line_list[18] == '':
            continue
        if line_list[23] == '':
            continue
        if line_list[28] == '':
            continue
        if 'million' in line_list[9]:
            line_list[10]=float(line_list[10])*1000
        if 'million' in line_list[14]:
            line_list[15]=float(line_list[15])*1000
        if 'million' in line_list[19]:
            line_list[20]=float(line_list[20])*1000
        if 'million' in line_list[24]:
            line_list[25]=float(line_list[25])*1000
                     
        data_list.append((line_list[5],line_list[7],line_list[8],line_list[10],line_list[15],line_list[20],line_list[25]))
        for l in data_list:
            state=l[0]
            city=l[1]
            date=l[2]
            data[l[0]]=city,date
                
    print (data)                   

def total_years(D, state):
    pass

def cities(D, state, year):
    pass

def months(D,state,year):
    pass

def display(totals_list,maxval,minval,D_cities,top_months):
#    "\nMax and Min pollution"
#    "\n{:>10s}{:>10s}"
#    "\nPollution totals by year"
#    "\n{:<6s}{:>8s} {:>8s} {:>8s} {:>8s}"
#    "\nPollution by city")
#    "\n{:<16s}{:>8s} {:>8s} {:>8s} {:>8s}"
#    "\nTop Months")
#    "\n{:>8s} {:>8s} {:>8s} {:>8s}"
    pass
  
def plot_years(totals_list,maxval,minval):
    no2 = []
    so2 = []
    o3 = []
    co = []
    years = []

    for i in range(2000,2017):
        years.append(i)

    for i in totals_list:
        no2.append(i[0])
        o3.append(i[1])
        so2.append(i[2])
        co.append(i[3])

    fig, ax = pylab.subplots()
    pylab.ylabel('Average Concentration')
    pylab.xlabel('Year')
    pylab.title('Total Average Pollution Per Year')
    ax.plot(years,no2, 'ro')
    ax.plot(years,o3, 'bo')
    ax.plot(years,so2, 'go')
    ax.plot(years,co, 'yo')
    ax.plot(years,no2, 'ro', label='NO2')
    ax.plot(years,o3, 'bo', label='O3')
    ax.plot(years,so2, 'go', label='SO2')
    ax.plot(years,co, 'yo', label='CO')


    ax.legend(loc='upper right', shadow=True, fontsize='small')

    pylab.show()

def main():
    fp=open_file()
    data=read_file(fp)
#    "Enter a state ('quit' to quit): "
#    "Invalid state."
#    "Enter a year ('quit' to quit): "
#    "Do you want to plot (yes/no)? " 
  
if __name__ == "__main__":
    main()          
