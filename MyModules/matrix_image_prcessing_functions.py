# Author: Darrien J-G Varrette (TerrienDJV5)
# Date: Dec 27th, 2022
# matrix_image_prcessing_functions.py


import time
import MyModules.binaryStringBitwiseLogic as bSBitwiseLogic
import gc

#python -m mpy_cross "matrix_image_prcessing_functions.py" Compile Me

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








"""
Image Effects Functions
"""



def offset_Image( imageFormatArray, offsetX = 0, offsetY = 0 ):
    imageFormatArrayOutput = {
        "SizeX":imageFormatArray["SizeX"],
        "SizeY":imageFormatArray["SizeY"],
        "Palette":imageFormatArray["Palette"],
        "Pixels":imageFormatArray["Pixels"],
        }
    imagePixelTemp = imageFormatArrayOutput["Pixels"]
    sizeX = imageFormatArrayOutput["SizeX"]
    sizeY = imageFormatArrayOutput["SizeY"]
    totalPixels = sizeX*sizeY
    if (offsetX >= sizeX)or(offsetX <= -sizeX)or(offsetY >= sizeY)or(offsetY <= -sizeY):
        imageFormatArrayOutput["Pixels"] = [0]*sizeX*sizeY
        return imageFormatArrayOutput
    #apply offsetY
    if (offsetY > 0):
        imagePixelTemp = [0]*offsetY*sizeX + imagePixelTemp[0:(sizeY-offsetY)*sizeX]
    elif (offsetY < 0):
        imagePixelTemp = imagePixelTemp[abs(offsetY)*sizeX:totalPixels] + abs(offsetY)*[0]*sizeX
    else:
        imagePixelTemp = imagePixelTemp
    #apply offsetX
    if (offsetX < 0):
        for y in range(imageFormatArrayOutput["SizeY"]):
            print(imagePixelTemp[y*sizeX+0:y*sizeX+sizeX], [0]*abs(offsetX) + imagePixelTemp[y*sizeX : y*sizeX+sizeX-abs(offsetX)])
            imagePixelTemp[y*sizeX+0:y*sizeX+sizeX] = [0]*abs(offsetX) + imagePixelTemp[y*sizeX : y*sizeX+sizeX-abs(offsetX)]
    elif (offsetX > 0):
        for y in range(imageFormatArrayOutput["SizeY"]):
            print(imagePixelTemp[y*sizeX+0:y*sizeX+sizeX], imagePixelTemp[y*sizeX+abs(offsetX) : y*sizeX+sizeX] + [0]*abs(offsetX))
            imagePixelTemp[y*sizeX+0:y*sizeX+sizeX] = imagePixelTemp[y*sizeX+abs(offsetX) : y*sizeX+sizeX] + [0]*abs(offsetX)
    else:
        imagePixelTemp = imagePixelTemp
    imageFormatArrayOutput["Pixels"] = imagePixelTemp
    del imagePixelTemp
    return imageFormatArrayOutput


def resize_Image( imageFormatArray, reSizedX = -1, reSizedY = -1 ):
    if (reSizedX==-1):
        reSizedX = imageFormatArray["SizeX"]
    if (reSizedY==-1):
        reSizedY = imageFormatArray["SizeY"]
    imageFormatArrayOutput = {
        "SizeX":reSizedX,
        "SizeY":reSizedY,
        "Palette":imageFormatArray["Palette"],
        "Pixels":imageFormatArray["Pixels"],
        }
    sizeX = imageFormatArray["SizeX"]
    sizeY = imageFormatArray["SizeY"]
    imagePixelTemp = imageFormatArrayOutput["Pixels"]
    for y in range(imageFormatArrayOutput["SizeY"]):
        imagePixelTemp[y*sizeX+0:y*sizeX+sizeX] = imagePixelTemp[y*sizeX+0:y*sizeX+sizeX] + [0]*(reSizedX-sizeX)
    imagePixelTemp += [0]*reSizedX*reSizedY
    imageFormatArrayOutput["Pixels"] = imagePixelTemp
    del imagePixelTemp
    return imageFormatArrayOutput

#finish this
def clip_Image( imageFormatArray, reSizedX = 8, reSizedY = 8, offsetX = 0, offsetY = 0):
    imageFormatArrayOutput = {
        "SizeX":imageFormatArray["SizeX"],
        "SizeY":imageFormatArray["SizeY"],
        "Palette":imageFormatArray["Palette"],
        "Pixels":imageFormatArray["Pixels"],
        }
    return imageFormatArrayOutput



#make this function scroll Words
#i was here
def scroll_Images_Right2Left( imageListArray, offset = 0 ):
    input_image_array = {
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
    return calculateEfficientImageRegisterPatterns( input_image_array, fastCalculation = False )





"""
Image Effects Functions End
"""


"""
8x8 Led matrix to Shift registers
"""


#main program, calling shift register function


#convert BitString to HexString
def convert_BitString_to_HexString( bitStringInput ): #ExpectInput: "00101010"
    nibble2hexDict = {"0000":"0","0001":"1",
                      "0010":"2","0011":"3",
                      "0100":"4","0101":"5",
                      "0110":"6","0111":"7",
                      "1000":"8","1001":"9",
                      "1010":"A","1011":"B",
                      "1100":"C","1101":"D",
                      "1110":"E","1111":"F"}
    hexStringOutput = ""
    counterPage = len(bitStringInput)
    bitStringInput = "0"*(counterPage%4) + bitStringInput #add leading Zeros
    nibbleString = "0000"
    counterPage = 0 #reusing This Variable For something different now!
    for index in range(len(bitStringInput)):
        if (counterPage==0):
            nibbleString = bitStringInput[index:index+4]
            hexStringOutput += nibble2hexDict[ nibbleString ]
        counterPage+=1;counterPage%=4 #update counterPage
    return hexStringOutput

#convert HexString to BitString
def convert_HexString_to_BitString( hexStringInput ): #ExpectInput: "A0"
    hex2nibbleDict = {"0":"0000","1":"0001",
                      "2":"0010","3":"0011",
                      "4":"0100","5":"0101",
                      "6":"0110","7":"0111",
                      "8":"1000","9":"1001",
                      "A":"1010","B":"1011",
                      "C":"1100","D":"1101",
                      "E":"1110","F":"1111"}
    bitStringOutput = ""
    for index in hexStringInput:
        bitStringOutput += hex2nibbleDict[ index ]
    return bitStringOutput




#rotateImage 270 degrees 8X8 image (turn 90 degrees Clockwise the flip Left2Right)
"""
-------->
01234567|umeWOG80|08GOWemu
89ABCDEF|vnfXPH91|19HPXfnv
GHIJKLMN|wogYQIA2|2AIQYgow
OPQRSTUV|xphZRJB3|3BJRZhpx
WXYZabcd|yqiaSKC4|4CKSaiqy
efghijkl|zrjbTLD5|5DLTbjrz
mnopqrst|-skcUME6|6EMUcks-
uvwxyz-+|+tldVNF7|7FNVdlt+
"""
#@timed_function
def rotateStrImage270(input_image_array):
    """ Older, Works
    flipped_image_String_array = ["00000000", "00000000", "00000000", "00000000", "00000000", "00000000", "00000000", "00000000"]
    tempList = ["0","0","0","0","0","0","0","0"]
    for i in [0,1,2,3,4,5,6,7]:
        for j in [0,1,2,3,4,5,6,7]:
            tempList[j] = input_image_array[j][i]
        flipped_image_String_array[i] = "".join(tempList)
    del tempList
    #print(flipped_image_String_array)
    #"""
    
    """ Better, Works
    flipped_image_String_array = [list(index) for index in input_image_array]
    tempList = ["0","0","0","0","0","0","0","0"]
    for i in [0,1,2,3,4,5,6,7]:
        for j in [0,1,2,3,4,5,6,7]:
            tempList[j] = input_image_array[j][i]
        flipped_image_String_array[i] = tempList
    flipped_image_String_array = ["".join(index) for index in flipped_image_String_array]
    del tempList
    #"""
    ###i am here
    #"""
    
    
    #inputOrder = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-+"
    #outputOrder = "08GOWemu19HPXfnv2AIQYgow3BJRZhpx4CKSaiqy5DLTbjrz6EMUcks-7FNVdlt+"
    
    inOutListOrder = [0, 8, 16, 24, 32, 40, 48, 56, 1, 9, 17, 25, 33, 41, 49, 57, 2, 10, 18, 26, 34, 42, 50, 58, 3, 11, 19, 27, 35, 43, 51, 59, 4, 12, 20, 28, 36, 44, 52, 60, 5, 13, 21, 29, 37, 45, 53, 61, 6, 14, 22, 30, 38, 46, 54, 62, 7, 15, 23, 31, 39, 47, 55, 63]
    #for index in range(len(inputOrder)):
    #    inOutListOrder.append(outputOrder.index(inputOrder[index]))
    #print(inOutListOrder)
    #time.sleep(100)
    
    #"""
    input_image_array_Line = []
    for index in input_image_array:
        input_image_array_Line += index
    
    flipped_image_String_array = input_image_array_Line[:]
    
    
    for index1 in [0,1,2,3,4,5,6,7]:
        for index2 in [0,1,2,3,4,5,6,7]:
            index = index2 + index1*8
            flipped_image_String_array[index] = input_image_array_Line[inOutListOrder[index]]
    
    
    input_image_array_Line1 = []
    for index1 in [0,1,2,3,4,5,6,7]:
        tempList_1 = b''
        for index2 in [0,1,2,3,4,5,6,7]:
            tempList_1 += flipped_image_String_array[index1*8+index2].encode()
        input_image_array_Line1.append(tempList_1.decode())
    flipped_image_String_array = input_image_array_Line1[:]
    #"""
    
    
    
    """
    input_image_array_Line1 = [b'', b'', b'', b'', b'', b'', b'', b'']
    for index1 in [0,1,2,3,4,5,6,7]:
        for index2 in [0,1,2,3,4,5,6,7]:
            newindex = inOutListOrder[ index2 + index1*8 ]
            input_image_array_Line1[index1] += input_image_array[int((newindex - newindex%8)*0.125)][newindex%8].encode()
        input_image_array_Line1[index1] = input_image_array_Line1[index1].decode()
    flipped_image_String_array = input_image_array_Line1[:]
    #"""
    
    
    
    #del input_image_array_Line1
    #del input_image_array_Line
    
    
    #"""
    
    #print(flipped_image_String_array)
    return flipped_image_String_array






"""
#Sub Calculations
"""
_invert4BitBinaryString = {'0000': '1111', '0001': '1110', '0010': '1101', '0011': '1100', '0100': '1011', '0101': '1010', '0110': '1001', '0111': '1000', '1000': '0111', '1001': '0110', '1010': '0101', '1011': '0100', '1100': '0011', '1101': '0010', '1110': '0001', '1111': '0000'}
_invert8BitBinaryString = {'00000000': '11111111', '00000001': '11111110', '00000010': '11111101', '00000011': '11111100', '00000100': '11111011', '00000101': '11111010', '00000110': '11111001', '00000111': '11111000', '00001000': '11110111', '00001001': '11110110', '00001010': '11110101', '00001011': '11110100', '00001100': '11110011', '00001101': '11110010', '00001110': '11110001', '00001111': '11110000', '00010000': '11101111', '00010001': '11101110', '00010010': '11101101', '00010011': '11101100', '00010100': '11101011', '00010101': '11101010', '00010110': '11101001', '00010111': '11101000', '00011000': '11100111', '00011001': '11100110', '00011010': '11100101', '00011011': '11100100', '00011100': '11100011', '00011101': '11100010', '00011110': '11100001', '00011111': '11100000', '00100000': '11011111', '00100001': '11011110', '00100010': '11011101', '00100011': '11011100', '00100100': '11011011', '00100101': '11011010', '00100110': '11011001', '00100111': '11011000', '00101000': '11010111', '00101001': '11010110', '00101010': '11010101', '00101011': '11010100', '00101100': '11010011', '00101101': '11010010', '00101110': '11010001', '00101111': '11010000', '00110000': '11001111', '00110001': '11001110', '00110010': '11001101', '00110011': '11001100', '00110100': '11001011', '00110101': '11001010', '00110110': '11001001', '00110111': '11001000', '00111000': '11000111', '00111001': '11000110', '00111010': '11000101', '00111011': '11000100', '00111100': '11000011', '00111101': '11000010', '00111110': '11000001', '00111111': '11000000', '01000000': '10111111', '01000001': '10111110', '01000010': '10111101', '01000011': '10111100', '01000100': '10111011', '01000101': '10111010', '01000110': '10111001', '01000111': '10111000', '01001000': '10110111', '01001001': '10110110', '01001010': '10110101', '01001011': '10110100', '01001100': '10110011', '01001101': '10110010', '01001110': '10110001', '01001111': '10110000', '01010000': '10101111', '01010001': '10101110', '01010010': '10101101', '01010011': '10101100', '01010100': '10101011', '01010101': '10101010', '01010110': '10101001', '01010111': '10101000', '01011000': '10100111', '01011001': '10100110', '01011010': '10100101', '01011011': '10100100', '01011100': '10100011', '01011101': '10100010', '01011110': '10100001', '01011111': '10100000', '01100000': '10011111', '01100001': '10011110', '01100010': '10011101', '01100011': '10011100', '01100100': '10011011', '01100101': '10011010', '01100110': '10011001', '01100111': '10011000', '01101000': '10010111', '01101001': '10010110', '01101010': '10010101', '01101011': '10010100', '01101100': '10010011', '01101101': '10010010', '01101110': '10010001', '01101111': '10010000', '01110000': '10001111', '01110001': '10001110', '01110010': '10001101', '01110011': '10001100', '01110100': '10001011', '01110101': '10001010', '01110110': '10001001', '01110111': '10001000', '01111000': '10000111', '01111001': '10000110', '01111010': '10000101', '01111011': '10000100', '01111100': '10000011', '01111101': '10000010', '01111110': '10000001', '01111111': '10000000', '10000000': '01111111', '10000001': '01111110', '10000010': '01111101', '10000011': '01111100', '10000100': '01111011', '10000101': '01111010', '10000110': '01111001', '10000111': '01111000', '10001000': '01110111', '10001001': '01110110', '10001010': '01110101', '10001011': '01110100', '10001100': '01110011', '10001101': '01110010', '10001110': '01110001', '10001111': '01110000', '10010000': '01101111', '10010001': '01101110', '10010010': '01101101', '10010011': '01101100', '10010100': '01101011', '10010101': '01101010', '10010110': '01101001', '10010111': '01101000', '10011000': '01100111', '10011001': '01100110', '10011010': '01100101', '10011011': '01100100', '10011100': '01100011', '10011101': '01100010', '10011110': '01100001', '10011111': '01100000', '10100000': '01011111', '10100001': '01011110', '10100010': '01011101', '10100011': '01011100', '10100100': '01011011', '10100101': '01011010', '10100110': '01011001', '10100111': '01011000', '10101000': '01010111', '10101001': '01010110', '10101010': '01010101', '10101011': '01010100', '10101100': '01010011', '10101101': '01010010', '10101110': '01010001', '10101111': '01010000', '10110000': '01001111', '10110001': '01001110', '10110010': '01001101', '10110011': '01001100', '10110100': '01001011', '10110101': '01001010', '10110110': '01001001', '10110111': '01001000', '10111000': '01000111', '10111001': '01000110', '10111010': '01000101', '10111011': '01000100', '10111100': '01000011', '10111101': '01000010', '10111110': '01000001', '10111111': '01000000', '11000000': '00111111', '11000001': '00111110', '11000010': '00111101', '11000011': '00111100', '11000100': '00111011', '11000101': '00111010', '11000110': '00111001', '11000111': '00111000', '11001000': '00110111', '11001001': '00110110', '11001010': '00110101', '11001011': '00110100', '11001100': '00110011', '11001101': '00110010', '11001110': '00110001', '11001111': '00110000', '11010000': '00101111', '11010001': '00101110', '11010010': '00101101', '11010011': '00101100', '11010100': '00101011', '11010101': '00101010', '11010110': '00101001', '11010111': '00101000', '11011000': '00100111', '11011001': '00100110', '11011010': '00100101', '11011011': '00100100', '11011100': '00100011', '11011101': '00100010', '11011110': '00100001', '11011111': '00100000', '11100000': '00011111', '11100001': '00011110', '11100010': '00011101', '11100011': '00011100', '11100100': '00011011', '11100101': '00011010', '11100110': '00011001', '11100111': '00011000', '11101000': '00010111', '11101001': '00010110', '11101010': '00010101', '11101011': '00010100', '11101100': '00010011', '11101101': '00010010', '11101110': '00010001', '11101111': '00010000', '11110000': '00001111', '11110001': '00001110', '11110010': '00001101', '11110011': '00001100', '11110100': '00001011', '11110101': '00001010', '11110110': '00001001', '11110111': '00001000', '11111000': '00000111', '11111001': '00000110', '11111010': '00000101', '11111011': '00000100', '11111100': '00000011', '11111101': '00000010', '11111110': '00000001', '11111111': '00000000'}

def calculateResultImage(rowBinaryStr, columnBinaryStr):
    #inputs must be a string repesentation of a Binary Value from 0 - 255
    #invert columnBinaryStr
    ###columnInvert = "".join(["0" if columnBinaryStr[i]=="1" else "1" for i in [0,1,2,3,4,5,6,7]])
    columnInvert = _invert8BitBinaryString[ columnBinaryStr ]
    
    #create result Image
    resultImage = [columnInvert if (rowBinaryStr[i] == "1") else "00000000" for i in [0,1,2,3,4,5,6,7]]
    return resultImage



_valuePixelCountDict8Bit = {'00000000': 0, '00000001': 1, '00000010': 1, '00000011': 2, '00000100': 1, '00000101': 2, '00000110': 2, '00000111': 3, '00001000': 1, '00001001': 2, '00001010': 2, '00001011': 3, '00001100': 2, '00001101': 3, '00001110': 3, '00001111': 4, '00010000': 1, '00010001': 2, '00010010': 2, '00010011': 3, '00010100': 2, '00010101': 3, '00010110': 3, '00010111': 4, '00011000': 2, '00011001': 3, '00011010': 3, '00011011': 4, '00011100': 3, '00011101': 4, '00011110': 4, '00011111': 5, '00100000': 1, '00100001': 2, '00100010': 2, '00100011': 3, '00100100': 2, '00100101': 3, '00100110': 3, '00100111': 4, '00101000': 2, '00101001': 3, '00101010': 3, '00101011': 4, '00101100': 3, '00101101': 4, '00101110': 4, '00101111': 5, '00110000': 2, '00110001': 3, '00110010': 3, '00110011': 4, '00110100': 3, '00110101': 4, '00110110': 4, '00110111': 5, '00111000': 3, '00111001': 4, '00111010': 4, '00111011': 5, '00111100': 4, '00111101': 5, '00111110': 5, '00111111': 6, '01000000': 1, '01000001': 2, '01000010': 2, '01000011': 3, '01000100': 2, '01000101': 3, '01000110': 3, '01000111': 4, '01001000': 2, '01001001': 3, '01001010': 3, '01001011': 4, '01001100': 3, '01001101': 4, '01001110': 4, '01001111': 5, '01010000': 2, '01010001': 3, '01010010': 3, '01010011': 4, '01010100': 3, '01010101': 4, '01010110': 4, '01010111': 5, '01011000': 3, '01011001': 4, '01011010': 4, '01011011': 5, '01011100': 4, '01011101': 5, '01011110': 5, '01011111': 6, '01100000': 2, '01100001': 3, '01100010': 3, '01100011': 4, '01100100': 3, '01100101': 4, '01100110': 4, '01100111': 5, '01101000': 3, '01101001': 4, '01101010': 4, '01101011': 5, '01101100': 4, '01101101': 5, '01101110': 5, '01101111': 6, '01110000': 3, '01110001': 4, '01110010': 4, '01110011': 5, '01110100': 4, '01110101': 5, '01110110': 5, '01110111': 6, '01111000': 4, '01111001': 5, '01111010': 5, '01111011': 6, '01111100': 5, '01111101': 6, '01111110': 6, '01111111': 7, '10000000': 1, '10000001': 2, '10000010': 2, '10000011': 3, '10000100': 2, '10000101': 3, '10000110': 3, '10000111': 4, '10001000': 2, '10001001': 3, '10001010': 3, '10001011': 4, '10001100': 3, '10001101': 4, '10001110': 4, '10001111': 5, '10010000': 2, '10010001': 3, '10010010': 3, '10010011': 4, '10010100': 3, '10010101': 4, '10010110': 4, '10010111': 5, '10011000': 3, '10011001': 4, '10011010': 4, '10011011': 5, '10011100': 4, '10011101': 5, '10011110': 5, '10011111': 6, '10100000': 2, '10100001': 3, '10100010': 3, '10100011': 4, '10100100': 3, '10100101': 4, '10100110': 4, '10100111': 5, '10101000': 3, '10101001': 4, '10101010': 4, '10101011': 5, '10101100': 4, '10101101': 5, '10101110': 5, '10101111': 6, '10110000': 3, '10110001': 4, '10110010': 4, '10110011': 5, '10110100': 4, '10110101': 5, '10110110': 5, '10110111': 6, '10111000': 4, '10111001': 5, '10111010': 5, '10111011': 6, '10111100': 5, '10111101': 6, '10111110': 6, '10111111': 7, '11000000': 2, '11000001': 3, '11000010': 3, '11000011': 4, '11000100': 3, '11000101': 4, '11000110': 4, '11000111': 5, '11001000': 3, '11001001': 4, '11001010': 4, '11001011': 5, '11001100': 4, '11001101': 5, '11001110': 5, '11001111': 6, '11010000': 3, '11010001': 4, '11010010': 4, '11010011': 5, '11010100': 4, '11010101': 5, '11010110': 5, '11010111': 6, '11011000': 4, '11011001': 5, '11011010': 5, '11011011': 6, '11011100': 5, '11011101': 6, '11011110': 6, '11011111': 7, '11100000': 3, '11100001': 4, '11100010': 4, '11100011': 5, '11100100': 4, '11100101': 5, '11100110': 5, '11100111': 6, '11101000': 4, '11101001': 5, '11101010': 5, '11101011': 6, '11101100': 5, '11101101': 6, '11101110': 6, '11101111': 7, '11110000': 4, '11110001': 5, '11110010': 5, '11110011': 6, '11110100': 5, '11110101': 6, '11110110': 6, '11110111': 7, '11111000': 5, '11111001': 6, '11111010': 6, '11111011': 7, '11111100': 6, '11111101': 7, '11111110': 7, '11111111': 8}

def calculateResultImagePixelCount(rowBinaryStr, columnBinaryStr):
    """
    rowPixelCount, columnPixelCount = 0, 0
    for i in [0,1,2,3,4,5,6,7]:
        rowPixelCount = (rowPixelCount+1 if (rowBinaryStr[i] == "1") else rowPixelCount ) #High Pins on Rows Activate Leds
        columnPixelCount = (columnPixelCount+1 if (columnBinaryStr[i] == "0") else columnPixelCount ) #Low Pins on columns Activate Leds
        #rowPixelCount += 1*(rowBinaryStr[i] == "1") #High Pins on Rows Activate Leds
        #columnPixelCount += 1*(columnBinaryStr[i] == "0") #Low Pins on columns Activate Leds
    #"""
    #High Pins on Rows Activate Leds
    rowPixelCount = _valuePixelCountDict8Bit[rowBinaryStr]
    #Low Pins on columns Activate Leds
    columnPixelCount = 8-_valuePixelCountDict8Bit[columnBinaryStr]
    pixelCount = rowPixelCount * columnPixelCount #counts all the Active pixels in the Result Image using rowBinaryStr, columnBinaryStr
    return pixelCount




#calculate Image Register Patterns (Row by Row)
#@timed_function
def calculateImageRegisterPatternsRbR(input_image_array):
    import MyModules.binaryStringBitwiseLogic as bSBitwiseLogic
    stringVerInput = ["{:08b}".format(input_image_array[i]) for i in range(len(input_image_array))]
    
    masterCountRange = [0,1,2,3,4,5,6,7]
    binaryImageOutStream = {
        "Data":[],#[Row][Col] == [RRRRRRRR, CCCCCCCC] #R='row', C='Col' flip Col
        "DataFormat":"0b",#format Type ["0b", "0x"]
        "DataImagesPixelCount":[],#List of The Images Pixel Count the Data will generate
        "DataListLength":0, #length of Data List
        }
    dupe_Col_byte_Row = [False,False,False,False,False,False,False,False]
    rowIndexer = [0,1,2,3,4,5,6,7]
    bitwiseMath = bSBitwiseLogic.BinaryStringBitwiseLogic()
    for indexRow in masterCountRange:
        if rowIndexer[indexRow] != indexRow: #skip row because rowIndexer was modifidy with dupe row
            continue
        #calculate Column to Print
        dupe_Col_byte_Row = [False,False,False,False,False,False,False,False]
        dupe_Col_byte_Row[indexRow] = True
        
        #check for Similar Cols and mark the Rows
        tempList = ["0","0","0","0","0","0","0","0"] #create Row Binary
        bit_byte_Col_Str = stringVerInput[indexRow] #create Column Binary
        for j in masterCountRange:
            dupe_Col_byte_Row[j] = (True if (stringVerInput[j] == bit_byte_Col_Str) else False)
            rowIndexer[j] = ( indexRow if (dupe_Col_byte_Row[j]==True) else rowIndexer[j] ) #allows for dupe Row Calculation to be skipped
            tempList[j] = ("1" if (dupe_Col_byte_Row[j]==True) else "0")  #calculate Row
        bit_byte_Row_Str = "".join(tempList)
        del tempList
        del dupe_Col_byte_Row
        
        
        shiftDataLines = [bit_byte_Row_Str, bitwiseMath.bitwiseNOT( bit_byte_Col_Str )]
        del bit_byte_Row_Str, bit_byte_Col_Str
        if (shiftDataLines in binaryImageOutStream["Data"])==False:
            binaryImageOutStream["Data"].append( shiftDataLines )
            binaryImageOutStream["DataImagesPixelCount"].append( calculateResultImagePixelCount( shiftDataLines[0], shiftDataLines[1] ) )
            binaryImageOutStream["DataListLength"] += 1
    binaryImageOutStream["DataListLength"] = len(binaryImageOutStream["Data"])
    del bitwiseMath
    #print(binaryImageOutStream)
    return binaryImageOutStream




#calculate Image Register Patterns (Column by Column)
#@timed_function
def calculateImageRegisterPatternsCbC(input_image_array):
    stringVerInput = ["{:08b}".format(input_image_array[i]) for i in range(len(input_image_array))]
    stringVerInput = rotateStrImage270(stringVerInput)
    
    
    masterCountRange = [0,1,2,3,4,5,6,7]
    binaryImageOutStream = {
        "Data":[],#[Row][Col] == [RRRRRRRR, CCCCCCCC] #R='row', C='Col' flip Col
        "DataFormat":"0b",#format Type ["0b", "0x"]
        "DataImagesPixelCount":[],#List of The Images Pixel Count the Data will generate
        "DataListLength":0,#length of Data List
        }
    dupe_Col_byte_Row = [False,False,False,False,False,False,False,False]
    columnIndexer = [0,1,2,3,4,5,6,7]
    for i in masterCountRange:
        indexColumn = i
        if columnIndexer[indexColumn] != indexColumn: #skip column because rowIndexer was modifidy with dupe column
            continue
        dupe_Col_byte_Row = [False,False,False,False,False,False,False,False]
        dupe_Col_byte_Row[i] = True
        
        #check for Similar Cols and mark the Rows
        #calculate Column
        bit_byte_Col_Str = stringVerInput[i] #create Column Binary
        for j in masterCountRange:
            dupe_Col_byte_Row[j] = (True if (stringVerInput[j] == bit_byte_Col_Str) else False)
            columnIndexer[j] = ( indexColumn if (dupe_Col_byte_Row[j]==True) else columnIndexer[j] ) #allows for dupe Column Calculation to be skipped
        
        #create Row Binary
        #tempList = ["1"if (dupe_Col_byte_Row[j]) else "0" for j in masterCountRange]
        tempList = ["0"if (dupe_Col_byte_Row[j]) else "1" for j in masterCountRange] #inverts Here
        bit_byte_Row_Str = "".join(tempList) #calculate Row
        del tempList
        
        shiftDataLines = [bit_byte_Col_Str, bit_byte_Row_Str]
        del bit_byte_Row_Str, bit_byte_Col_Str
        
        
        if (shiftDataLines in binaryImageOutStream["Data"])==False:
            binaryImageOutStream["Data"].append( shiftDataLines )
            binaryImageOutStream["DataImagesPixelCount"].append( calculateResultImagePixelCount( shiftDataLines[0], shiftDataLines[1] ) )
            binaryImageOutStream["DataListLength"] += 1
    #print(binaryImageOutStream)
    return binaryImageOutStream







#calculate Image Register Patterns (Row by Row) & (Column by Column)
#making this faster
#@timed_function
def calculateImageRegisterPatternsRbRandCbC(input_image_array):
    stringVerInput_RbR = ["{:08b}".format(input_image_array[i]) for i in range(len(input_image_array))]
    stringVerInput_CbC = ["{:08b}".format(input_image_array[i]) for i in range(len(input_image_array))]
    
    stringVerInput_CbC = rotateStrImage270(stringVerInput_CbC)
    
    masterCountRange = [0,1,2,3,4,5,6,7]
    
    
    binaryImageOutStreamRbR = {
        "Data":[],#[Row][Col] == [RRRRRRRR, CCCCCCCC] #R='row', C='Col' flip Col
        "DataFormat":"0b",#format Type ["0b", "0x"]
        "DataImagesPixelCount":[],#List of The Images Pixel Count the Data will generate
        "DataListLength":0, #length of Data List
        }
    dupe_Col_byte_Row_RbR = [False,False,False,False,False,False,False,False]
    rowIndexer_RbR = [0,1,2,3,4,5,6,7]
    
    binaryImageOutStreamCbC = {
        "Data":[],#[Row][Col] == [RRRRRRRR, CCCCCCCC] #R='row', C='Col' flip Col
        "DataFormat":"0b",#format Type ["0b", "0x"]
        "DataImagesPixelCount":[],#List of The Images Pixel Count the Data will generate
        "DataListLength":0,#length of Data List
        }
    dupe_Col_byte_Row_CbC = [False,False,False,False,False,False,False,False]
    columnIndexer_CbC = [0,1,2,3,4,5,6,7]
    
    
    for index in masterCountRange:
        indexRow = index
        indexColumn = index
        
        if (rowIndexer_RbR[indexRow] == indexRow): #skip row because rowIndexer was modifidy with dupe row
            #calculate Column to Print
            #check for Similar Cols and mark the Rows
            bit_byte_Row_Str_RbR = ["0","0","0","0","0","0","0","0"] #create Row Binary
            bit_byte_Col_Str_RbR = stringVerInput_RbR[indexRow] #create Column Binary
            bit_byte_Col_Str_RbR_invert = ["0","0","0","0","0","0","0","0"] #create Column Binary
            dupe_Col_byte_Row_Value_RbR = False
        
        if (columnIndexer_CbC[indexColumn] == indexColumn): #skip column because rowIndexer was modifidy with dupe column
            #check for Similar Cols and mark the Rows
            #calculate Column
            bit_byte_Col_Str_CbC = stringVerInput_CbC[indexColumn] #create Column Binary
            tempList_CbC = ["0", "0", "0", "0", "0", "0", "0", "0"] #create Row Binary
            dupe_Col_byte_Row_Value_CbC = False
        
        
        if (rowIndexer_RbR[indexRow] == indexRow): #skip row because rowIndexer was modifidy with dupe row
            for j in masterCountRange:
                dupe_Col_byte_Row_Value_RbR = (True if (stringVerInput_RbR[j] == bit_byte_Col_Str_RbR) else False)
                rowIndexer_RbR[j] = ( indexRow if (  dupe_Col_byte_Row_Value_RbR  == True) else rowIndexer_RbR[j] ) #allows for dupe Row Calculation to be skipped
                bit_byte_Row_Str_RbR[j] = ("1" if (  dupe_Col_byte_Row_Value_RbR  == True) else "0")  #calculate Row
                bit_byte_Col_Str_RbR_invert[j] = ("0" if (bit_byte_Col_Str_RbR[j]=="1") else "1")  #calculate Column
            del dupe_Col_byte_Row_Value_RbR
            bit_byte_Col_Str_RbR = "".join( bit_byte_Col_Str_RbR_invert )
            del bit_byte_Col_Str_RbR_invert
            bit_byte_Row_Str_RbR = "".join(bit_byte_Row_Str_RbR)
            
            
            shiftDataLinesRbR = [bit_byte_Row_Str_RbR, bit_byte_Col_Str_RbR]
            del bit_byte_Row_Str_RbR, bit_byte_Col_Str_RbR
            
            
            if (shiftDataLinesRbR in binaryImageOutStreamRbR["Data"])==False:
                binaryImageOutStreamRbR["Data"].append( shiftDataLinesRbR )
                binaryImageOutStreamRbR["DataImagesPixelCount"].append( calculateResultImagePixelCount( shiftDataLinesRbR[0], shiftDataLinesRbR[1] ) )
                binaryImageOutStreamRbR["DataListLength"] += 1
        
        
        
        if (columnIndexer_CbC[indexColumn] == indexColumn): #skip column because rowIndexer was modifidy with dupe column
            for j in masterCountRange:
                dupe_Col_byte_Row_Value_CbC = (True if (stringVerInput_CbC[j] == bit_byte_Col_Str_CbC) else False)
                columnIndexer_CbC[j] = ( indexColumn if (  dupe_Col_byte_Row_Value_CbC  ==True) else columnIndexer_CbC[j] ) #allows for dupe Column Calculation to be skipped
                tempList_CbC[j] = ("0"if ( dupe_Col_byte_Row_Value_CbC ==True) else "1") #inverts Here  #calculate Row
            bit_byte_Row_Str_CbC = "".join(tempList_CbC) #calculate Row
            del tempList_CbC
            del dupe_Col_byte_Row_Value_CbC
            
            
            shiftDataLinesCbC = [bit_byte_Col_Str_CbC, bit_byte_Row_Str_CbC]
            del bit_byte_Row_Str_CbC, bit_byte_Col_Str_CbC
            
            if (shiftDataLinesCbC in binaryImageOutStreamCbC["Data"])==False:
                binaryImageOutStreamCbC["Data"].append( shiftDataLinesCbC )
                binaryImageOutStreamCbC["DataImagesPixelCount"].append( calculateResultImagePixelCount( shiftDataLinesCbC[0], shiftDataLinesCbC[1] ) )
                binaryImageOutStreamCbC["DataListLength"] += 1
    
    
    
    imageCheck_Cache = {
                "RbR":binaryImageOutStreamRbR,
                "CbC":binaryImageOutStreamCbC
                }
    del binaryImageOutStreamRbR
    del binaryImageOutStreamCbC
    
    
    return imageCheck_Cache






#converts integer to 8bitString
int28BitString_Cache = {}
def convertInt28BitString(intInput):
    if not(intInput in int28BitString_Cache):
        output8BitString = "{:08b}".format(intInput)
        int28BitString_Cache[intInput] = output8BitString
    else:
        output8BitString = int28BitString_Cache[intInput]
    return output8BitString



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


def bitStringList2intList_other(bitStringList):
    outputList = []
    for index in bitStringList:
        outputList.append( bitString2int( index ) )
    return outputList




#@timed_function
def subtract8X8BitImagefrom8X8BitImage(minuend_StrBitImage, subtrahend_StrBitImage):
    #helpful: #https://stackoverflow.com/questions/1228299/changing-one-character-in-a-string
    #"ms":"d"
    truthTable = {"00":"0",
                  "01":"2", #shoud not Happen
                  "10":"1",
                  "11":"0",
                  }
    #image format: RowByRow, "1"=High, "0"=Low
    difference_StrBitImage = [["0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0"]]
    #indexY = Row,  indexX = Column
    for indexY in [0,1,2,3,4,5,6,7]:
        bitStrList = ["0","0","0","0","0","0","0","0"]
        for indexX in [0,1,2,3,4,5,6,7]:
            bitStrList[indexX] = truthTable[ ( minuend_StrBitImage[indexY][indexX] + subtrahend_StrBitImage[indexY][indexX] ) ]
        difference_StrBitImage[indexY] = "".join( bitStrList )
        difference_StrBitImage[indexY] = bitString2int( difference_StrBitImage[indexY] )
    
    return difference_StrBitImage








#calculate Efficient Image Register Patterns using (Row by Row)&(Column by Column)
#returns image it created so it can be subtracted and that new image is then inputed until image is blank
"""
11111111
10000000
10000000
11111110
10000000
10000000
10000000
10000000
 |
 |
\|/
CbC      | RbR      | CbC or RbR
10000000 | 01111110 | 00000001
10000000 | 00000000 | 00000000
10000000 | 00000000 | 00000000
10000000 | 01111110 | 00000000
10000000 | 00000000 | 00000000
10000000 | 00000000 | 00000000
10000000 | 00000000 | 00000000
10000000 | 00000000 | 00000000
"""

@timed_function
def calculateEfficientImageRegisterPatterns( input_image_array, fastCalculation = False ):
    #uses calculateImageRegisterPatternsRbR() and calculateImageRegisterPatternsCbC()
    #print(f"calculateEfficientImageRegisterPatterns(",input_image_array,"):")
    binaryImageOutStream = {
        "Data":[],#[Row][Col] == [RRRRRRRR, CCCCCCCC] #R='row', C='Col' flip Col
        "DataFormat":"0b",#format Type ["0b", "0x"]
        "DataImagesPixelCount":[],#List of The Images Pixel Count the Data will generate
        "DataListLength":0,#length of Data List
        "DataCalculateType":[],#calculation Type ["CbC", "RbR"]
        }
    
    blank_8x8ByteImage = [0,0,0,0,0,0,0,0]
    cycle_input_image_array = convertImageFormat2RbR( input_image_array )
    
    bestOption = "None"
    cycleCount = 0 # =could be replaced with binaryImageOutStream["DataListLength"]
    if fastCalculation==False:
        #check if complete, if complete Break out of WhileTrue loop
        while ( ( (cycleCount >=1 )or(cycleCount!=0) ) and (cycle_input_image_array == blank_8x8ByteImage) )==False:
            #imageCheck
            """
            imageCheck_Cache = {
                "RbR":calculateImageRegisterPatternsRbR( cycle_input_image_array ),
                "CbC":calculateImageRegisterPatternsCbC( cycle_input_image_array )
                }
            #"""
            imageCheck_Cache = calculateImageRegisterPatternsRbRandCbC( cycle_input_image_array )
            
            #LargestPixelCount
            LargestPixelCount_RbR_Index_Cache = 0
            LargestPixelCount_CbC_Index_Cache = 0
            imageCheck_Cache_CheckList_RbR = imageCheck_Cache["RbR"]["DataImagesPixelCount"]
            imageCheck_Cache_CheckList_CbC = imageCheck_Cache["CbC"]["DataImagesPixelCount"]
            #for newIndex in range(imageCheck_Cache["RbR"]["DataListLength"]):
            #    LargestPixelCount_RbR_Index_Cache = ( newIndex if (imageCheck_Cache["RbR"]["DataImagesPixelCount"][newIndex] > imageCheck_Cache["RbR"]["DataImagesPixelCount"][ LargestPixelCount_RbR_Index_Cache ]) else LargestPixelCount_RbR_Index_Cache )
            #for newIndex in range(imageCheck_Cache["CbC"]["DataListLength"]):
            #    LargestPixelCount_CbC_Index_Cache = ( newIndex if (imageCheck_Cache["CbC"]["DataImagesPixelCount"][newIndex] > imageCheck_Cache["CbC"]["DataImagesPixelCount"][ LargestPixelCount_CbC_Index_Cache ]) else LargestPixelCount_CbC_Index_Cache )
            
            LargestPixelCount_RbR_Index_Cache = imageCheck_Cache_CheckList_RbR.index( max(imageCheck_Cache_CheckList_RbR) )
            LargestPixelCount_CbC_Index_Cache = imageCheck_Cache_CheckList_CbC.index( max(imageCheck_Cache_CheckList_CbC) )
            
            LargestPixelCount_Index_Cache = {
                "RbR":LargestPixelCount_RbR_Index_Cache,
                "CbC":LargestPixelCount_CbC_Index_Cache
                }
            #ensures These Variables wont effect themself Next cycle
            del imageCheck_Cache_CheckList_RbR, imageCheck_Cache_CheckList_CbC
            del LargestPixelCount_RbR_Index_Cache, LargestPixelCount_CbC_Index_Cache
            
            
            #find Best Calculation Option
            bestOption = ("RbR" if (imageCheck_Cache["RbR"]["DataImagesPixelCount"][ LargestPixelCount_Index_Cache["RbR"] ] > imageCheck_Cache["CbC"]["DataImagesPixelCount"][ LargestPixelCount_Index_Cache["CbC"] ] ) else "CbC" )
            #print("bestOption:",bestOption)
            bestOption_LargestPixelCount_Index_Cache = LargestPixelCount_Index_Cache[ bestOption ]
            
            
            #add to < binaryImageOutStream{} >
            binaryImageOutStream["DataFormat"] = "0x"
            dataTemp = imageCheck_Cache[bestOption]["Data"][ LargestPixelCount_Index_Cache[bestOption] ]
            dataTemp[0] = convert_BitString_to_HexString( dataTemp[0] )
            dataTemp[1] = convert_BitString_to_HexString( dataTemp[1] )
            binaryImageOutStream["Data"].append( dataTemp )
            del dataTemp
            binaryImageOutStream["DataImagesPixelCount"].append( imageCheck_Cache[bestOption]["DataImagesPixelCount"][ LargestPixelCount_Index_Cache[bestOption] ] )
            binaryImageOutStream["DataListLength"] += 1
            binaryImageOutStream["DataCalculateType"].append( bestOption )
            
            #create String copy of cycle_input_image_array
            cycle_input_image_Str_array = ["{:08b}".format(cycle_input_image_array[i]) for i in [0,1,2,3,4,5,6,7]]
            #cycle_input_image_Str_array = [convertInt28BitString( cycle_input_image_array[i] ) for i in [0,1,2,3,4,5,6,7]]
            
            #prepare for next cycle
            """ #make this usable for "0x"!
            minuend_BitImage = mipf.convertImageFormat2PixelList( bitStringList2intList( cycle_input_image_Str_array ) )
            subtrahend_BitImage = mipf.convertImageFormat2PixelList(  bitStringList2intList( calculateResultImage( imageCheck_Cache[bestOption]["Data"][ LargestPixelCount_Index_Cache[bestOption] ][0], imageCheck_Cache[bestOption]["Data"][ LargestPixelCount_Index_Cache[bestOption] ][1]) ) )
            differenceBitStrArray = mipf.subtractBitImagefromBitImage(minuend_BitImage, subtrahend_BitImage)
            differenceBitStrArray = mipf.convertImageFormat2RbR( differenceBitStrArray )
            del minuend_BitImage, subtrahend_BitImage
            #"""
            currentRowRegister = convert_HexString_to_BitString( imageCheck_Cache[bestOption]["Data"][ LargestPixelCount_Index_Cache[bestOption] ][0] )
            currentColumnRegister = convert_HexString_to_BitString(  imageCheck_Cache[bestOption]["Data"][ LargestPixelCount_Index_Cache[bestOption] ][1])
            currentCalImage = calculateResultImage( currentRowRegister , currentColumnRegister )
            del currentRowRegister, currentColumnRegister
            differenceBitStrArray = subtract8X8BitImagefrom8X8BitImage(cycle_input_image_Str_array,  currentCalImage )
            del currentCalImage
            cycle_input_image_array = differenceBitStrArray
            
            
            cycleCount += 1
            del LargestPixelCount_Index_Cache
            del bestOption
            del imageCheck_Cache
        print(f"CycleCount: {cycleCount}")
    elif fastCalculation==True:
        image_Cache = calculateImageRegisterPatternsRbR( cycle_input_image_array )
        binaryImageOutStream["Data"] = image_Cache["Data"]
        binaryImageOutStream["DataListLength"] = len(image_Cache["Data"])
        binaryImageOutStream["DataImagesPixelCount"] = image_Cache["DataImagesPixelCount"]
        binaryImageOutStream["DataCalculateType"] = "FastCal"
        del image_Cache
        return binaryImageOutStream
        
    gc.collect()
    #print("", binaryImageOutStream)
    return binaryImageOutStream
    
    







