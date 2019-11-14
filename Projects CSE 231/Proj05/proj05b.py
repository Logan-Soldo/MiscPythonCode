def open_file():
    fp=open('data.csv')
    return fp
    #"Input a file name: "
    #"Unable to open the file. Please try again."
    
def read_data(fp, input_str, search_str):
    for line in fp:
        if line.(search_str):
            line=line.split(",")
            Country=line[0]
            Region=line[1]
            Happiness=line[2]        
            return Country,Region,Happiness
def display_line(country_name, region_name, happiness_score):
    pass
    #"{:24s}{:<32s}{:<17.2f}"

def main():
    country_list=()
    fp=open_file()
    input_str=input("Input 1 to search in country names, 2 to search in regions: ")
    if input_str == "1":
        search_str=input("What do you want to search for? ")
        search_str=search_str.lower()
        country_list += read_data(fp,input_str,search_str)
        print(country_list)
        
    
    
    #"Invalid choice, please try again!"
    #"{:24s}{:<32s}{:<17s}"

if __name__ == '__main__':
   main()