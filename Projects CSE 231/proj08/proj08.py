
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
    reader=csv.reader(fp)
    header= next(reader,None)
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
        
        state= line_list[5].strip()
        city= line_list[7].strip()
        date= line_list[8].strip()
        NO2= float(line_list[10])
        O3= float(line_list[15])
        SO2 = float(line_list[20])
        CO = float(line_list[25])             
      
        previous_city,previous_date = "",""
        if previous_city==city and previous_date==date:
            continue
        
        if state in data:
           data[state].append([city,date,NO2,O3,SO2,CO])
        else:
            data[state]=[[city,date,NO2,O3,SO2,CO]]
           
#           previous_city=l[1]
#          previous_date=l[2]       
    return data                  

def total_years(D, state):

    totals_list=[[0,0,0,0]for i in range(17)]
    for item in D[state]:
        year = int(item[1].split('/')[-1])
    
        totals_list[year % 2000][0]+=item[2]
        totals_list[year % 2000][1]+=item[3]
        totals_list[year % 2000][2]+=item[4]
        totals_list[year % 2000][3]+=item[5]
         
    temp = []
    for i in totals_list:
        temp += i
        
    maxval=max(temp)
    minval=min(temp)

    return (totals_list, maxval, minval)

def cities(D, state, year):
    cities={}
    pollution_total=[]
    NO2=0
    O3=0
    SO2=0
    CO=0 
    if state in D.keys():
        pollution_total=D[state]
        for j in pollution_total:
        #    ryear= int(j[1].split('/')[-1])
        #    if ryear == year: 
                city=j[0]
                NO2+=j[2]
                O3+=j[3]
                SO2+=j[4]
                CO+=j[5]
                
        if city not in cities:
            cities[city]= [NO2,O3,SO2,CO]
            NO2=0
            O3=0
            SO2=0
            CO=0 
                
    return cities
        

def months(D,state,year):
    NO2 = []
    O3= []
    SO2= []
    CO= []
    for i in range(12):
        NO2.append(0)
        O3.append(0)
        SO2.append(0)
        CO.append(0)
    if state in D.keys():
        for j in D[state]:
            month= int(j[1].split("/")[0])
            ryear= int(j[1].split("/")[2]) 
            if ryear == year:
                NO2[month - 1] += j[2]
                O3[month - 1] += j[3]
                SO2[month - 1] +=j[4]
                CO[month - 1] += j[5]
                
                
    NO2.sort(reverse=True)
    O3.sort(reverse=True)
    SO2.sort(reverse=True)
    CO.sort(reverse=True)
    
    
#    print(NO2[:5],O3[:5],SO2[:5],CO[:5])
    return (NO2[:5],O3[:5],SO2[:5],CO[:5])

def display(totals_list,maxval,minval,D_cities,top_months):
    print("\nMax and Min pollution")
    print("\n{:>10.2f}{:>10.2f}".format(minval,maxval))
    year=2000
    print("\nPollution totals by year")
    for data in totals_list:
        if data != [0,0,0,0]:
            print("{:<6d}{:>8.2f} {:>8.2f} {:>8.2f} {:>8.2f}".format(year,data[0],data[1],data[2],data[3]))
            year+=1    
    print("\nPollution by city")
    print("\n{:<16s}{:>8s} {:>8s} {:>8s} {:>8s}".format('City','NO2','O3','SO2','CO'))

    for city in D_cities:
        result=D_cities[city]
        if result != [0,0,0,0]:
            print("{:<16s}{:>8.2f} {:>8.2f} {:>8.2f} {:>8.2f}".format(city,result[0],result[1],result[2],result[3]))
 #           
    #    "\nTop Months")
    #    "\n{:>8s} {:>8s} {:>8s} {:>8s}"
    
  
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
    D=read_file(fp)
    state=input("Enter a state('quit' to quit): ")
    while state != "quit":
        if state in D:
            
            totals_list,maxval,minval=total_years(D,state)
            year=int(input("Enter a year ('quit' to quit): "))
            D_cities=cities(D,state,year)
            top_months=months(D,state,year)
            display(totals_list,maxval,minval,D_cities,top_months)
        else:
            print("Invalid state.")
        state=input("Enter a state('quit' to quit): ")


#    "Do you want to plot (yes/no)? " 
  
if __name__ == "__main__":
    main()              