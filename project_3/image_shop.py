#RahulKapur
#rk2749


def negate_red(rowArray, maxColorValue): #pass max RGB Value
    i = 0
    newRowArray = []
    for item in rowArray:#loop through the row Array
        if((i)%3 == 0 or (i) == 0):
            item = ((int(item)-int(maxColorValue)) * -1) # change R color value
            newRowArray.append(item) # append to new array
        else:
            newRowArray.append(item)
        i = i +1

    return newRowArray # return array

def negate_green(rowArray, maxColorValue):#loop through the row Array
    i = 0
    newRowArray = []
    for item in rowArray:
        if((i-1)%3 == 0 or (i-1) == 0):
            item = ((int(item)-int(maxColorValue)) * -1) # change G color value
            newRowArray.append(item)
        else:
            newRowArray.append(item)  # append to new array
        i = i +1

    return newRowArray #return array

def negate_blue(rowArray, maxColorValue): #loop through the row Array
    i = 0
    newRowArray = []
    for item in rowArray:
        if((i-2)%3 == 0 or (i-2) == 0):
            item = ((int(item)-int(maxColorValue)) * -1) # change B color value
            newRowArray.append(item)
        else:
            newRowArray.append(item)
        i = i +1

    return newRowArray


def flip_horizontal(rowArray):
    listPixels = []
    singlePixel = []
    newRowArray = []
    i = 0
    for item in rowArray: #loop through row Array
        i = i + 1
        singlePixel.append(item) #append three integers to make a pixel
        if (i%3==0):
            listPixels.append(singlePixel) #append each pixel to list
            singlePixel = []
    listPixels.reverse() #reverse list of pixels
    for item in listPixels:
        for integer in item:
            newRowArray.append(integer)#append each item to new array

    return newRowArray



def grey_scale(rowArray):
    i = 0
    newRowArray = []
    average = 0
    for item in rowArray: #loop through array
        i = i + 1
        average = average + int(item) #add up each pixel
        if (i%3 == 0):
            average = average/3 #find average
            for j in range (0,3):
                newRowArray.append(average) #append average three times to new array
            average = 0 #set verage to 0
    return newRowArray #return new array


def extreme_contrast(rowArray, maxRGBValue): #extra

    newRowArray = []
    for item in rowArray: #loop through array
        if (int(item) > (int(maxRGBValue)/2)):#check if greater than midpoint
            newRowArray.append(int(maxRGBValue)) #append max value
        else:
            number = 0
            newRowArray.append(0) #append 0
    return newRowArray #return new array

def make_mat(rowArray, pixelThickness, pixelArray): #function adds padding each row

    for i in range (0, pixelThickness): #insert pixels at the fron
        rowArray.insert(0,pixelArray[0])
        rowArray.insert(1,pixelArray[1])
        rowArray.insert(2,pixelArray[2])
    for j in range (0, pixelThickness): #insert pixels at the back
        rowArray.append(pixelArray[0])
        rowArray.append(pixelArray[1])
        rowArray.append(pixelArray[2])
    return rowArray

