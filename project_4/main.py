# *******************************************************
# hw4A module
# Assignment 4 Part 1
# ENGI E1006
# *******************************************************
#Rahul Kapur
#rk2749

import percolation as perc

def main():
    A=perc.make_sites(0.6,25)
    perc.write_grid('sites.txt',A)
    B=perc.read_grid('sites.txt')
    C=perc.flow(B)
    if perc.percolates(C):
        print('percolates')
    else:
        print('does not percolate')


main()

