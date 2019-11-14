###############################################################################
# Project #06
#
# This program prompts for a file C.elegans.gff or C.elegans_small.gff
# Prompts for a single chromosome or all of the chromosomes in CHROMOSOMES string
# loops while the input is not equal to 'quit', if input is 'quit' program ends
# takes input chromosome and calcuates the mean and standard deviation of all\
#    input chromosomes in file. 
# keeps prompting for chromosome until 'quit' is input
###############################################################################

import math                  #imports math for square root function
CHROMOSOMES = ['chri','chrii','chriii','chriv','chrv','chrx']

def open_file():
    """
    Open file function looks for an input file.
    prompt: input file name
    fp: the file being read in
    """
    while True:
        prompt=input("Input a file name: ")
        try:
            fp= open(prompt,"r")                    # testing to see if correct input is found
            return fp
        except FileNotFoundError:                   # error if incorrect input is entered
            print("Unable to open file.")

def read_file(fp):
    """
    looks in fp read file, removes header,takes out wanted information, then sorts list
    genes_list: list being made and returned here

    """
    genes_list=[]                             #making genes_list
    for line in fp:
        print(line)
        if '#' not in line[0]:
            line=line.split('\t')
            genes_list.append((line[0],int(line[3]),int(line[4])))  #making a list out of file and appending to genes_list
    genes_list.sort()
    return genes_list                       #returns genes_list

def extract_chromosome(genes_list, chromosome):
    """
    Makes a list of only the chromosome that was input
    chrom_gene_list: the list being made
    looks in genes_list for the input chromosome
    returns chrom_gene_list
    """
    chrom_gene_list=[]                         #making chrom_genes_list
    for g in genes_list:
        if g[0]== chromosome:                  #checking if input chromosome is in file
            chrom_gene_list.append(g[0:3])
    chrom_gene_list.sort()
    return chrom_gene_list                     #returns chrom_gene_list

def extract_genome(genes_list):
    """
    making a list, calling extract_chromosome to make a new list of genomes
    genome_list: list being made and returned here
    return genome_list
    """
    genome_list=[]                            # making genome_list
    for j in CHROMOSOMES:                     # loops for all instances of input chromosome
        chromosome=j                         
        genome_list.append(extract_chromosome(genes_list,chromosome))
    return genome_list                        # returns a list of genomes
    
def compute_gene_length(chrom_gene_list):
    """
    gene_len: list of length of gene_list
    gene_mean: calculated mean from gene_len list
    gene_number: calculated length of gene_len
    summation: takes length of gene minus gene mean squared
    gene_stddev: square root of summation of all genes and devides by gene_number
    returns: mean and standard deviation
    """
    gene_len=[]                              #making a gene_len list
    stddev_list=[]                           #making a list to do standard deviation calculation
    for k in chrom_gene_list:
        gene_len.append(k[2]-k[1]+1)         # gene_len= gene_end minus gene_start plus one 
    gene_mean=((sum(gene_len)/len(gene_len))) #mean calculated from sum of gene_len divided by the length of gene_len
    gene_number=len(gene_len)
    for l in gene_len:
        summation=(l-gene_mean)**2            # length minus mean squared
        stddev_list.append(summation)         # appends to a list
        gene_stddev=math.sqrt(sum(stddev_list)/gene_number) #takes the sum of standard deviation list and divides that by gene_number
    return (gene_mean,gene_stddev)
    
 
def display_data(chrom_gene_list, chrom):
    """
    Displays the data being calculated
    x:makes the first 3 letters lowercase
    y:makes the rest of the letters uppercase
    mean and standard_deviation are called in from compute_gene_length
    prints chromosome, mean, and standard deviation
    """
    x=chrom[:3].lower()                    #first 3 letters lowercase
    y=chrom[3:].upper()                    #last letters uppercase
    chrom=(x+y)
    gene_mean=float(compute_gene_length(chrom_gene_list)[0])
    gene_stddev=float(compute_gene_length(chrom_gene_list)[1])

    print("{:<11s}{:9.2f}{:9.2f}".format(chrom,gene_mean,gene_stddev)) #print formatting
    
def main():
    print("Gene length computation for C. elegans.\n")
    fp=open_file()               #prompts open file fuction
    genes_list=read_file(fp)     #defining genes_list as read_file(fp) function
    
    chromosome=input("\nEnter chromosome or 'all' or 'quit': ")
    chromosome=chromosome.lower()             #makes input lowercase
    while chromosome.lower() != 'quit':       #loops until 'quit is input'
        chromosome=chromosome.lower()         #resets input to lowercase
        if chromosome in CHROMOSOMES:
            extract_chromosome(genes_list, chromosome)  #extract_chromosome function called 
            extract_genome(genes_list)                  # extract_genome function called
   
            chrom_gene_list=extract_chromosome(genes_list,chromosome)
            compute_gene_length(chrom_gene_list)       #compute gene length fucnction being called
   
            chrom=chromosome
            print("\nChromosome Length")
            print("{:<11s}{:>9s}{:>9s}".format('chromosome','mean','std-dev'))
            display_data(chrom_gene_list,chrom)
            chromosome=input("\nEnter chromosome or 'all' or 'quit': ")
        
        elif chromosome == 'all':
            print("\nChromosome Length")
            print("{:<11s}{:>9s}{:>9s}".format('chromosome','mean','std-dev'))
            for chromosome in CHROMOSOMES:          #loops through all of the chromosomes
                extract_chromosome(genes_list, chromosome)  #extract_chromosome function called 
                extract_genome(genes_list)                  # extract_genome function called
       
                chrom_gene_list=extract_chromosome(genes_list,chromosome)
                compute_gene_length(chrom_gene_list)        #compute gene length fucnction being called
       
                chrom=chromosome
                display_data(chrom_gene_list,chrom)
            chromosome=input("\nEnter chromosome or 'all' or 'quit': ")
        elif chromosome != 'all' or chromosome not in CHROMOSOMES: #if something else is input, error message displayed
            print("Error in chromosome.  Please try again.")
            chromosome=input("\nEnter chromosome or 'all' or 'quit': ")

if __name__ == "__main__":
    main()
