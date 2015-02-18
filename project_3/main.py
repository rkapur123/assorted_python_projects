#Rahul Kapur
#rk2749
import  image_shop
def main():
    inputName = raw_input("Enter name of image file: ")
    outputName = raw_input("Enter name of output file: ")
    buffer = 3072 #buffer
    bufferArray = [] #array to store a row
    file = open(inputName, 'r')
    PP3 = file.readline()
    columnAndRow = file.readline()
    columnAndRowSplit = columnAndRow.split()
    maxRGBValue = file.readline() #max RGB in ppm
    maxColumn = int(columnAndRowSplit[0]) * 3 #number of integers per row
    if (maxColumn > buffer): #check buffer size
        print("The image cannot fit a row into the buffer")
        file.close() #close file
    else:
        listYes = display_menu() #display menu
        outputFile = open(outputName, 'w') # open output
        outputFile.write(PP3)
        if (listYes[len(listYes) - 1] == 7): # if make_mat is selected
            rValue = input("Enter an R Value ")
            gValue = input("Enter an G Value ")
            bValue = input("Enter an B Value ")
            pixelThickness = input("Enter pixel thickness ")
            pixelArray = []
            pixelArray.append(rValue)
            pixelArray.append(gValue)
            pixelArray.append(bValue)
            x = int(columnAndRowSplit[0]) + (pixelThickness *2)
            y = int(columnAndRowSplit[1]) + (pixelThickness *2)
            outputFile.write(str(x) + " " + str(y) + "\n") #new row/column for output
        else :
            outputFile.write(columnAndRow) #if make_mat is not selected
        outputFile.write(maxRGBValue)
        counter = 0
        for line in file: #read line from input
            for words in line.split():#split it into each element
                bufferArray.append(words) # add to buffer
                if (len(bufferArray) % int(maxColumn) == 0): #check if row is full
                    for function in listYes: #enact the function that was selected in order
                        if function == 1:
                            bufferArray = image_shop.grey_scale(bufferArray)
                        elif function == 2:
                            bufferArray = image_shop.flip_horizontal(bufferArray)
                        elif function == 3:
                            bufferArray = image_shop.negate_red(bufferArray, maxRGBValue)
                        elif function == 4:
                            bufferArray = image_shop.negate_green(bufferArray, maxRGBValue)
                        elif function == 5:
                            bufferArray = image_shop.negate_blue(bufferArray, maxRGBValue)
                        elif function == 6:
                            bufferArray = image_shop.extreme_contrast(bufferArray, maxRGBValue)
                        elif function == 7:
                            if counter == 0:
                                counter = counter + 1
                                for k in range (0, pixelThickness):#add padding to the top  of mat
                                    for l in range (0, int(maxColumn/3) + (pixelThickness*2)):
                                        outputFile.write(str(rValue) + " ")
                                        outputFile.write(str(gValue) + " ")
                                        outputFile.write(str(bValue) + " ")
                                    outputFile.write("\n")
                                bufferArray = image_shop.make_mat(bufferArray, pixelThickness, pixelArray)
                            else:#after top add padding to sides
                                bufferArray = image_shop.make_mat(bufferArray, pixelThickness, pixelArray)
                    for integer in bufferArray:#read each element from the row
                        outputFile.write(str(integer) + " ") #output to file
                    bufferArray = []
                    outputFile.write("\n");
        if (listYes[len(listYes) - 1] == 7): #add bottom padding if mat was selected
            for k in range (0, pixelThickness):
                for l in range (0, int(maxColumn/3) + (pixelThickness*2)):
                    outputFile.write(str(rValue) + " ")
                    outputFile.write(str(gValue) + " ")
                    outputFile.write(str(bValue) + " ")
                outputFile.write("\n")
        outputFile.close() #close both files
        file.close()

        print(outputName + " created")

def display_menu():
        print("Here are your choices: ") #here is the menu
        print("[1]convert to greyscale [2]flip horizontally")
        print("[3]negative of red [4]negative of green [5]negative of blue")
        print("[6] extreme contrast")
        print("[7]  create a mat")
        one = raw_input("Do you want [1]? (y/n) ")
        two = raw_input("Do you want [2]? (y/n) ")
        three = raw_input("Do you want [3]? (y/n) ")
        four = raw_input("Do you want [4]? (y/n) ")
        five = raw_input("Do you want [5]? (y/n) ")
        six = raw_input("Do you want [6]? (y/n) ")
        seven = raw_input("Do you want [7]? (y/n) ")

        listYesNo = [] #append answers to a list
        listYesNo.append(one)
        listYesNo.append(two)
        listYesNo.append(three)
        listYesNo.append(four)
        listYesNo.append(five)
        listYesNo.append(six)
        listYesNo.append(seven)
        listYes = [] #create a new list containing all yes's
        counter = 0
        for item in listYesNo:
            counter = counter + 1
            if (str(item) == "y"):
                listYes.append(counter)
        return listYes #return the list of yes's

main()