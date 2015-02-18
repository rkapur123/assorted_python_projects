#Rahul Kapur
#rk2749

import numpy as np

def read_grid(filename):

    inputFile = open(filename, 'r') #open file
    dimensions = int(inputFile.readline()) #get array dimensions


    mainArray = np.array([]) #intialize empty array
    for line in inputFile:
        a = np.fromstring(line,dtype=int,sep=' ') #get a line of data
        mainArray = np.append(mainArray, a) #append array of line to main
    mainArray.shape = (dimensions,dimensions)

    inputFile.close() #close file


    return mainArray #return main


def write_grid(filename,sites):


    output = open(filename, 'w') #open output
    output.write(str(int((sites.size) ** (0.5))) + "\n") #write dimensions
    np.savetxt(output, sites.astype(int), fmt='%i') #write 2d array as int
    output.close() #close output





def flow(sites):

    number = int((sites.size) ** (0.5)) #dimesions of array
    mainArray = np.zeros((number, number), dtype = np.int)
    detectZero = False #boolean to check for zero in column
    for i in range (0, number):
        detectZero = False
        for j in range(0, number):
            if detectZero == False: #if not zero detected
                if (sites[j][i] == 0):
                    detectZero = True
                else:
                    mainArray[j][i] = 1 #add 1

            else:
                mainArray[j][i] = 0 #if zero is detected then add 0

    return mainArray







def percolates(flow_matrix):

    number = int((flow_matrix.size) ** (0.5)) #dimensions of array

    for j in range (0, number):
        if flow_matrix[number -1][j] == 1: #check last row for any ones
            return True


    return False #if no 1's then return false


def make_sites(p,n):


    sites=np.random.binomial(1,p,(n,n)) #binomial distribution to model data


    return sites



    