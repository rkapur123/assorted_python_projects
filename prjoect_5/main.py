# *******************************************************
# hw4B module
# Assignment 4 Part 2
# ENGI E1006
# *******************************************************
#Rahul Kapur
#rk2749

import percolation2 as perc

def main():
    A=perc.make_sites(0.6,25)
    perc.write_grid('sites.txt',A)
    B=perc.read_grid('sites.txt')
    C=perc.undirected_flow(B)
    if perc.percolates(C):
        print('percolates')
    else:
        print('does not percolate')

    
    #visualize flow
    perc.show_perc(B)

    #generate percolation probability graph
    perc.make_plot(10000,10)





main()
