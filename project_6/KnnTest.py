__author__ = 'RahulKapur'
#Rahul Kapur
#rk2749

import Knn as knn
import scipy as sp

def main():
    kValue = input("Specify a kValue: ")
    data = knn.make_data("/Users/RahulKapur/Desktop/test.txt")
    accuracy = knn.n_validator(data, 10, knn.KNNclassifier, (int(kValue)))
    print"Accuracy of the function is %f" %(accuracy)
    
main()


