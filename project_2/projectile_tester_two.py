__author__ = 'RahulKapur'

# *********************************************
# projectile_tester
# this prgram tests the functions in the
# projectile module
# *********************************************

import projectile

def main():

    # set up intitial values
    v_0 = 300
    s_0 = 0
    t=0
    delta_t = .05
    list = []
    s=s_0 #start s off at s_0

    # print a table with values computed both ways for positive positions

    print('seconds \t distance_sim \t \t distance_formula')
    print('-----------------------------------------------------------')
    list = projectile.s_extra(t, v_0, s_0, delta_t) # populate list
    for i in range (0, len(list) - 1): # created for loop to loop through the list
        s_formula = projectile.s_standard( t,v_0)
        print( '%2d \t \t %.5f \t \t %.5f') %(t,list[t],s_formula) #print each item
        t=t+1




# now run main()
main()