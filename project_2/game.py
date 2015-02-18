__author__ = 'RahulKapur'
import random

def generateComputerRandom(threshold): #passes in threshold value
    number = 0
    computerNumber = random.random()
    if(computerNumber > threshold):
        number = 2 #number declred is two
    else:
        number = 1
    return number
def checkWinner(total):
    winner = 0
    user = 0
    if (total == 2 ):
        user = 2 #player 2
    elif (total == 4):
        user = 2 #player 2
    elif (total == 3):
        user = 1 #player 1
    else:
        user = 3

    return user #return player




def t_comparison(): #simulate p1
    maxAverage = 0 #find the maximum average winnings
    computerOneRandom = 0 #starting t1 value
    for n in range (0, 11):
        print("\n")
        print("Holding t1 at %f" %computerOneRandom)
        print("t1 \t \t \t \t t2 \t \t Player one \t Player Two")
        average = 0
        bestT1 = 0 #store best t1 for optimal strategy
        computerTwoRandom = 0
        for j in range (0, 11):
            computerOnePoints = 0
            computerTwoPoints = 0
            computerOneWins = 0
            computerTwoWins = 0
            for k in range (0, 100000):#100,000 rounds to compute each value
                computerOneNumber = generateComputerRandom(computerOneRandom)
                computerTwoNumber = generateComputerRandom(computerTwoRandom)
                total = computerOneNumber + computerTwoNumber
                winner = checkWinner(total)
                if (winner == 1):
                    computerOnePoints = computerOnePoints + total
                    computerTwoPoints = computerTwoPoints - total
                    computerOneWins = computerOneWins + 1
                elif (winner == 2):
                    computerOnePoints = computerOnePoints - total
                    computerTwoPoints = computerTwoPoints + total
                    computerTwoWins = computerTwoWins + 1

            print ("%f \t  %f \t \t %d\t \t %d " %(computerOneRandom, computerTwoRandom, computerOnePoints, computerTwoPoints))
            average = average + computerOnePoints # sum wininngs of p1
            computerTwoRandom = computerTwoRandom + 0.1
        print("\n")
        print("The average winnings for Player 1 are: %f" %(average/11)) #average for a given t1
        average = average/11
        if (average > maxAverage):
            maxAverage = average
            bestT1 = computerOneRandom
        computerOneRandom = computerOneRandom + 0.1
    print("\n")
    print("Optimal strategy Max Average: %f T1: %f" %(maxAverage, bestT1)) #print optimal strategy

def t_comparison2():
    maxAverage = 0 # store max average for optimal strategy
    computerTwoRandom = 0
    for n in range (0, 11):
        print("\n")
        print("Holding t2 at %f" %computerTwoRandom) #hold t2 constant
        print("t2 \t \t \t \t t1 \t \t Player one \t Player Two")
        average = 0
        bestT2 = 0 #store best t2
        computerOneRandom = 0
        for j in range (0, 11):
            computerOnePoints = 0
            computerTwoPoints = 0
            computerOneWins = 0
            computerTwoWins = 0
            for k in range (0, 100000):
                computerOneNumber = generateComputerRandom(computerTwoRandom)
                computerTwoNumber = generateComputerRandom(computerOneRandom)
                total = computerOneNumber + computerTwoNumber
                winner = checkWinner(total)
                if (winner == 1):
                    computerOnePoints = computerOnePoints + total
                    computerTwoPoints = computerTwoPoints - total
                    computerOneWins = computerOneWins + 1
                elif (winner == 2):
                    computerOnePoints = computerOnePoints - total
                    computerTwoPoints = computerTwoPoints + total
                    computerTwoWins = computerTwoWins + 1

            print ("%f \t  %f \t \t %d\t \t %d " %( computerTwoRandom, computerOneRandom, computerOnePoints, computerTwoPoints))
            average = average + computerTwoPoints
            computerOneRandom = computerOneRandom + 0.1
        print("\n")
        print("The average winnings for Player 2 are: %f" %(average/11)) #average winnings for a given t2
        average = average/11
        if (average > maxAverage):
            maxAverage = average
            bestT2 = computerTwoRandom
        computerTwoRandom = computerTwoRandom + 0.1 #increment t2
    print("\n")
    print("Optimal strategy, Max Average: %f T2: %f" %(maxAverage, bestT2)) #optimal strategy




