# Author: Darrien J-G Varrette (TerrienDJV5)
# Date: Dec 27th, 2022
# matrix_image_prcessing_functions.py


import time



"""
Private Functions
"""
def timed_function(f, *args, **kwargs):
    myname = str(f).split(' ')[1]
    def new_func(*args, **kwargs):
        t = time.ticks_us()
        result = f(*args, **kwargs)
        delta = time.ticks_diff(time.ticks_us(), t)
        print('Function {} Time = {:6.3f}ms'.format(myname, delta/1000))
        return result
    return new_func







#converts bitString to integer
bitString2int_Cache = {}
def bitString2int(bitString):
    #find a way to make this Much faster
    #try int(bitString, 2)
    integerOut = 0
    if not(bitString in bitString2int_Cache):
        for index in range(len(bitString)):
            integerOut += (2**(len(bitString)-1-index))*(bitString[index]=="1")
        #print(bitString, "==", integerOut, "==", "{:08b}".format(integerOut))
        bitString2int_Cache[ bitString ] = integerOut
    else:
        integerOut = bitString2int_Cache[bitString]
    #print(f"length of bitString2int_Cache:{len(bitString2int_Cache)}")
    return integerOut



#ensure RbR is in intList Format
@timed_function
def bitStringList2intList(bitStringList):
    outputList = []
    for index in bitStringList:
        if type(index)==type("0"):
            outputList.append( bitString2int( index ) )
        elif type(index)==type(0):
            outputList.append( index )
    return outputList





"""
#Convert Calculations
"""

def convertByteStrToValue( byteString ):
    value = 0
    byteLength = len(byteString)
    for indexSub in range( byteLength ):
        index = (byteLength-1-indexSub)
        value += (2** index) * (byteString[indexSub]=="1")
    return value

@timed_function
def convertImageFormat2RbR(imageDict):
    imageRbRList = [0, 0, 0, 0, 0, 0, 0, 0]
    #for yPos in [0,1,2,3,4,5,6,7]:
    #    rowList = imageDict["Pixels"]
    #    rowList = rowList[0+8*yPos:8+8*yPos]
    #    imageRbRList[yPos] = (2**0)*(rowList[ 0 ]) + (2**1)*(rowList[ 1 ]) + (2**2)*(rowList[ 2 ]) + (2**3)*(rowList[ 3 ]) + (2**4)*(rowList[ 4 ]) + (2**5)*(rowList[ 5 ]) + (2**6)*(rowList[ 6 ]) + (2**7)*(rowList[ 7 ])
    pixelsList = imageDict["Pixels"]
    
    rowList = pixelsList[0:8]
    imageRbRList[0] = (2**0)*(rowList[ 0 ]) + (2**1)*(rowList[ 1 ]) + (2**2)*(rowList[ 2 ]) + (2**3)*(rowList[ 3 ]) + (2**4)*(rowList[ 4 ]) + (2**5)*(rowList[ 5 ]) + (2**6)*(rowList[ 6 ]) + (2**7)*(rowList[ 7 ])
    
    rowList = pixelsList[8:16]
    imageRbRList[1] = (2**0)*(rowList[ 0 ]) + (2**1)*(rowList[ 1 ]) + (2**2)*(rowList[ 2 ]) + (2**3)*(rowList[ 3 ]) + (2**4)*(rowList[ 4 ]) + (2**5)*(rowList[ 5 ]) + (2**6)*(rowList[ 6 ]) + (2**7)*(rowList[ 7 ])
    
    rowList = pixelsList[16:24]
    imageRbRList[2] = (2**0)*(rowList[ 0 ]) + (2**1)*(rowList[ 1 ]) + (2**2)*(rowList[ 2 ]) + (2**3)*(rowList[ 3 ]) + (2**4)*(rowList[ 4 ]) + (2**5)*(rowList[ 5 ]) + (2**6)*(rowList[ 6 ]) + (2**7)*(rowList[ 7 ])
    
    rowList = pixelsList[24:32]
    imageRbRList[3] = (2**0)*(rowList[ 0 ]) + (2**1)*(rowList[ 1 ]) + (2**2)*(rowList[ 2 ]) + (2**3)*(rowList[ 3 ]) + (2**4)*(rowList[ 4 ]) + (2**5)*(rowList[ 5 ]) + (2**6)*(rowList[ 6 ]) + (2**7)*(rowList[ 7 ])
    
    rowList = pixelsList[32:40]
    imageRbRList[4] = (2**0)*(rowList[ 0 ]) + (2**1)*(rowList[ 1 ]) + (2**2)*(rowList[ 2 ]) + (2**3)*(rowList[ 3 ]) + (2**4)*(rowList[ 4 ]) + (2**5)*(rowList[ 5 ]) + (2**6)*(rowList[ 6 ]) + (2**7)*(rowList[ 7 ])
    
    rowList = pixelsList[40:48]
    imageRbRList[5] = (2**0)*(rowList[ 0 ]) + (2**1)*(rowList[ 1 ]) + (2**2)*(rowList[ 2 ]) + (2**3)*(rowList[ 3 ]) + (2**4)*(rowList[ 4 ]) + (2**5)*(rowList[ 5 ]) + (2**6)*(rowList[ 6 ]) + (2**7)*(rowList[ 7 ])
    
    rowList = pixelsList[48:56]
    imageRbRList[6] = (2**0)*(rowList[ 0 ]) + (2**1)*(rowList[ 1 ]) + (2**2)*(rowList[ 2 ]) + (2**3)*(rowList[ 3 ]) + (2**4)*(rowList[ 4 ]) + (2**5)*(rowList[ 5 ]) + (2**6)*(rowList[ 6 ]) + (2**7)*(rowList[ 7 ])
    
    rowList = pixelsList[56:64]
    imageRbRList[7] = (2**0)*(rowList[ 0 ]) + (2**1)*(rowList[ 1 ]) + (2**2)*(rowList[ 2 ]) + (2**3)*(rowList[ 3 ]) + (2**4)*(rowList[ 4 ]) + (2**5)*(rowList[ 5 ]) + (2**6)*(rowList[ 6 ]) + (2**7)*(rowList[ 7 ])
    
    return imageRbRList



def getPixelValueFromRbR(imageList, xPos, yPos):
    #stringVerInput = "{:08b}".format(imageList[yPos])
    #pixelValue = int(stringVerInput[xPos])
    #return pixelValue
    return 1*(imageList[yPos]&(0b00000001<<xPos) == (0b00000001<<xPos))


@timed_function
def convertImageFormat2PixelList(imageRbRList):
    imageRbRList = bitStringList2intList( imageRbRList )
    imageDict = {
        "SizeX":8,
        "SizeY":8,
        "Palette":[0x00000000,0xffffffff],
        "Pixels":[
            0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0
            ],
        }
    """
    tempString = ""
    tempStrList = []
    tempBigList = []
    for yPos in [0,1,2,3,4,5,6,7]:
        tempString = "{:08b}".format(imageRbRList[yPos])
        tempStrList = list(tempString)
        for xPos in [0,1,2,3,4,5,6,7]:
            tempStrList[xPos] = int( tempStrList[xPos] )
        tempBigList += tempStrList
    imageDict["Pixels"] = tempBigList
    print(len(tempBigList))
    #"""
    #"""
    for yPos in [0,1,2,3,4,5,6,7]:
        for xPos in [0,1,2,3,4,5,6,7]:
            imageDict["Pixels"][xPos + yPos*8] = getPixelValueFromRbR(imageRbRList, xPos, yPos)
    #"""
    return imageDict





"""
other Functions
"""



@timed_function
def subtractBitImagefromBitImage(minuend_BitImage, subtrahend_BitImage):
    #"ms":"d"
    truthTable = {"00":"0",
                  "01":"2", #shoud not Happen
                  "10":"1",
                  "11":"0",
                  }
    difference_BitImage = {
        "SizeX":8,
        "SizeY":8,
        "Palette":[0x00000000,0xffffffff],
        "Pixels":[
            0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0
            ],
        }
    if (minuend_BitImage["SizeX"] == subtrahend_BitImage["SizeX"] and difference_BitImage["SizeX"] == minuend_BitImage["SizeX"]):
        if (minuend_BitImage["SizeY"] == subtrahend_BitImage["SizeY"] and difference_BitImage["SizeY"] == minuend_BitImage["SizeY"]):
            for pixelIndex in range(len(difference_BitImage["Pixels"])):
                difference_BitImage["Pixels"][pixelIndex] = minuend_BitImage["Pixels"][pixelIndex] - subtrahend_BitImage["Pixels"][pixelIndex]
            pass
    
    
    return difference_BitImage












