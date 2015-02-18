__author__ = 'RahulKapur'
import game
import random
def main():
    toPlay = input("Enter 1 to play or 2 for a computer simulation \n")
    answer = "yes"
    userPoints = 0
    computerPoints = 0
    if toPlay == 1:
        print("You are Player one") #assign user to P1
        while answer == "yes":
            choice = input("Enter 1 or 2 \n")
            threshold = random.random() #create random threshold
            computerNumber = game.generateComputerRandom(threshold) #generates number
            total = computerNumber + choice #total sum of choices
            user = game.checkWinner(total) #function to return winner
            if (user == 1 ):
                print("The user wins") #user wins
                userPoints = userPoints + total
                computerPoints = computerPoints - total
            else:
                print("The computer wins")#computer wins
                userPoints = userPoints - total
                computerPoints = computerPoints + total

            print("Computer Points : %d " %(computerPoints)) #print points
            print("User Points : %d " %(userPoints))
            answer = raw_input("Would you like to play again (yes or no) \n")
        print ("Game over! ")
    elif toPlay == 2:
        game.t_comparison() #simulate P1 strategy
        game.t_comparison2() #simulate P2 strategy






main()


