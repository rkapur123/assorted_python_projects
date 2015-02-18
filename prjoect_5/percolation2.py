# *******************************************************
# percolation module
# Assignment 4 Part 2
# ENGI E1006
# *******************************************************
#Rahul Kapur
#rk2749
import numpy as np
import matplotlib.pyplot as plt

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


def undirected_flow(sites):
    number = int((sites.size) ** (0.5)) #dimensions
    full = np.zeros((number, number), dtype= int)
    for i in range (0, number): 
        flow_from(sites , full, 0, i) #loop each element of the first row
        
    return full


def flow_from(sites,full,i,j):
    widthAndHeight = int((sites.size) ** (0.5)) #dimensions
    if (sites[i][j] == 0): #if there is a 0
        return 
    if (full[i][j]): # if it equals 1
        return
    full[i][j] = 1 #set it to 1
    if (i + 1 < (widthAndHeight)): #if i + 1is not out of bounds
        flow_from(sites,full,i+1,j) #increment i and recurse

    if (j + 1 < (widthAndHeight)): #if j + 1 is not out of bounds 
        flow_from(sites,full,i,j + 1) #increment j and recurse

    if (j - 1 >= 0): #if j -1 is not out of bounds
        flow_from(sites,full,i, j-1) #recurse








def percolates(flow_matrix):

    number = int((flow_matrix.size) ** (0.5)) #dimensions of array

    for j in range (0, number):
        if flow_matrix[number -1][j] == 1: #check last row for any ones
            return True


    return False #if no 1's then return false

def make_sites(p,n):
    
    sites=np.random.binomial(1,p,(n,n)) #binomial distribution to model data


    return sites




def show_perc(sites):
    full = undirected_flow(sites) #get flow array
    final = sites + full #sum the two
    plt.matshow(final) #graph them
    plt.show() # show




def make_plot(trials,n):
    probCounter = 100 #create a counter
    plt.title("Percolation Probability vs Site Vacancy Probability") #title
    plt.ylabel("Percolation probability") #y
    plt.xlabel("Site Vacancy Probability") #x
    xValues = np.zeros((10)) #10 values
    yValues = np.zeros((10)) #10 values
    for i in range (0 , 100, 10):#run from 0 to 100 with increments of 10
        prob = (float(i) /probCounter)
        checker = 0
        for j in range (0 , trials):
            A = make_sites(prob,n)
            B = undirected_flow(A)
            if percolates(B):
                checker = checker + 1 #increment checker     
        vacancyProbability = (float(checker)/trials)#vacncy prob
        xValues[prob*10] = vacancyProbability #vacancy prob
        yValues[prob*10] = prob #iteration prob
    plt.plot(yValues, xValues) #plot the arrays
    plt.show() #show them
            
        