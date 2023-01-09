# Author: Darrien J-G Varrette (TerrienDJV5)
# Date: Dec 27th, 2022
# matrix_image_prcessing_functions.py


import time


def timed_function(f, *args, **kwargs):
    myname = str(f).split(' ')[1]
    def new_func(*args, **kwargs):
        t = time.ticks_us()
        result = f(*args, **kwargs)
        delta = time.ticks_diff(time.ticks_us(), t)
        print('Function {} Time = {:6.3f}ms'.format(myname, delta/1000))
        return result
    return new_func



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
    return 1*(imageList[yPos]&(0b10000000>>xPos) == (0b10000000>>xPos))

@timed_function
def convertImageFormat2PixelList(imageRbRList):
    print(imageRbRList)
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



