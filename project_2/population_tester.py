__author__ = 'RahulKapur'

import pred_prey as pp

def main():
    # set up intitial values
    a = 0.1
    b = 0.01
    c = 0.01
    d = .00002
    pred_init = 25
    prey_init = 2000

    # print a table with populations after each cycle

    print('n \t predator population \t \t \t prey population')
    print('-----------------------------------------------------------------')
    for n in range(0,110,10):
        pred_pop = pp.pred_future(pred_init,prey_init,a,b,c,d,n)
        prey_pop = pp.prey_future(pred_init,prey_init,a,b,c,d,n)
        print( '%d \t %9d \t \t \t \t %8d') %(n,pred_pop, prey_pop)

#now run main()
main()