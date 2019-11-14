from operator import itemgetter
import pylab

def open_file():
    while True:
        prompt=input("Input a file name: ")
        try:
            fp= open(prompt,"r")                    # testing to see if correct input is found
            return fp
        except FileNotFoundError:                   # error if incorrect input is entered
            print("Unable to open the file. Please try again.")
def read_data(fp):
    data_list=[]
    Avg_Pre=0
    Avg_Unit=0
    for line in fp:
        try:
            line= line.strip().split(',')
            Avg_Pre= float(line[3])/int(line[4])
            Avg_Unit= float(line[3])/int(line[5])
            data_list.append((int(line[0]),line[1],float(line[3]),int(line[4]),int(line[5]),Avg_Pre,Avg_Unit))
            data_list.sort()

        except ValueError:
            pass
    return data_list

def top_ten_list(column, year_list):
    list1=[]
    list2=[]
    year_list_sorted= sorted(year_list, key=itemgetter(column,1), reverse=True)
    for j in year_list_sorted[:10]:
        medicaid=j[1]
        total=j[column]
        list1.append(medicaid)
        list2.append(total)
    return list1,list2
    
def get_year_list(year, data):
    year_list = []
    year= int(year)
    for tup in data:
        if tup[0]== year:
            year_list.append(tup)
    return year_list        

def display_table(year, year_list):
    year=str(year)
    print("{:^80s}".format("Drug spending by Medicaid in "+year))
    print("{:<35s}{:>15}{:>20}{:>15}".format("Medication","Prescriptions","Prescription Cost","Total"))
    for k in year_list:
        brand=k[1]
        prescription=k[3]
        Avg_prescription=k[5]
        Total=k[2]/1000
#       print("{:<32s,:>15,d,:>20,.2f,:>15,.2f}".format(year_list[1],year_list[3],year_list[5],year_list[2]))
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
    year = ""
    fp = open_file()
    data=read_data(fp)
    print("Medicaid drug spending 2011 - 2015")
    year = input("Enter a year to process ('q' to terminate): ")
    while year != "q":
        while year.isdigit() or year == "q":        
            if year == "q":
                break
            while year != "q":
                year_list=get_year_list(year,data)
                display_table(year,year_list)
                Top_ten=input("Do you want to plot the top 10 values (yes/no)? ")
                if Top_ten == "yes":

                    (x,y)=top_ten_list(3,year_list)
                    title="Top 10 Medications prescribed in "+year
                    xlabel="Medication Name"
                    ylabel="Prescriptions"
                    plot_top_ten(x,y,title,xlabel,ylabel)

                    (x,y)=top_ten_list(2,year_list)
                    title="Top 10 Medicaid Covered Medications in "+year
                    xlabel="Medication Name"
                    ylabel="Amount"
                    plot_top_ten(x,y,title,xlabel,ylabel)   
                    year = input("Enter a year to process ('q' to terminate): ")
                    
                elif Top_ten == "no":
                    year = input("Enter a year to process ('q' to terminate): ")
        else:
            print("Invalid Year. Try Again!")
            year = input("Enter a year to process ('q' to terminate): ")
    
 #       top_ten_list(3,year_list)
        
if __name__ == "__main__":
    main()