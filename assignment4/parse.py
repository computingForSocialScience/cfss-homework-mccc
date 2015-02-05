import csv
import sys
import matplotlib.pyplot as plt

def readCSV(filename):
    '''Reads the CSV file `filename` and returns a list
    with as many items as the CSV has rows. Each list item 
    is a tuple containing the columns in that row as stings.
    Note that if the CSV has a header, it will be the first
    item in the list.'''
    with open(filename,'r') as f:
        rdr = csv.reader(f)
        lines = list(rdr)
    return(lines)


### enter your code below

def get_avg_latlng(lines):
    print lines[0][128:130]
    return None
    lines= lines[1:]
    for l in lines:
        print l[128]

def zip_code_barchart(lines):
    print zip(range(0,131), lines[0])
    zips = []
    lines = lines[1:]
    for l in lines:
        print l[28]
        zips.append(l[28])

    
    n,bins,patches = plt.hist(zips,50, histtype='bar')
    plt.show()
    



lines = readCSV('permits.csv')
#get_avg_latlng(lines)
zip_code_barchart(lines)
