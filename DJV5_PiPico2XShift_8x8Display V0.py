# Author: Darrien J-G Varrette (TerrienDJV5)
# Date: Nov 24th, 2022
# Later Date: Dec 19th, 2022
# Version: 0.3.0 (Dec 26 2022) (last ver 3.2.5)
# Fixes (0.3.0)
# 
# 
# additions (0.3.0)
# - newImageFormat for better flexibility
# - new Function calculateImageRegisterPatternsRbRandCbC(input_image_array)
# -> calculates RbR and CbC in the same Loop (should be overall Faster!)
# 


import sys
import _thread
import micropython

from machine import Pin
from micropython import const

import utime
import random

import time



import gc
gc.collect()
print("FreeMemory: ", gc.mem_free())



#my Programs
import MyModules.binaryStringBitwiseLogic as bSBitwiseLogic

""" Helpful URLs
Check "urls.txt"


->for memory optimization
Check "urls.txt"


->for Dual Core Programing
Check "urls.txt"


->Other Stuff
Check "urls.txt"


"""
"""
#bitwiseMath = bSBitwiseLogic.BinaryStringBitwiseLogic()
  
  #bitwise0Str = bitwiseMath.bitwiseNOT( input )
  #bitwise1Str = bitwiseMath.bitwiseAND(bitwise0Str ,"0000000011111111")
  #bitwise2Str = bitwiseMath.bitwiseAND(input,"1111111100000000")
  #bitwise3Str = bitwiseMath.bitwiseOR( bitwise2Str , bitwise1Str )
  
  
  #inputString = bitwiseMath.bitwiseAND(input ,"1111111111111111")
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





#sys.getsizeof(variable)



#define PINs according to cabling
_SET_dataPIN = const(0x14)#20
_SET_latchPIN = const(0x16)#22
_SET_clockPIN = const(0x15)#21


#set pins to output PIN objects
dataPIN=Pin(_SET_dataPIN, Pin.OUT)
latchPIN=Pin(_SET_latchPIN, Pin.OUT)
clockPIN=Pin(_SET_clockPIN, Pin.OUT)






import MyModules.matrix_image_prcessing_functions as mipf #make sure functions from here start with "mipf."


"""
Load _MasterImageDictionary and _MasterAnimationDictionary
"""
import master_image_dictionary
_MasterImageDictionary = {
    
    }
_MasterAnimationDictionary = {
    
    }
_MasterImageDictionary = master_image_dictionary._MasterImageDictionary
_MasterAnimationDictionary = master_image_dictionary._MasterAnimationDictionary
del master_image_dictionary




#print(_MasterImageDictionary)






"""
cache Variables
"""
registerDisplayImageCache = {}




"""
Better Shift Function
"""
#Try using This
#https://docs.micropython.org/en/latest/library/machine.SPI.html

lastOldInputList = ["00000000","00000000"] #should only be used in this function
#@timed_function
def better_shift_out_update(inputList,data,clock,latch): #LSBFIRST
  #inputList format=  ["01010101", "01010101"] each string is 8 chars long only 2 Registers
  global lastOldInputString
  
  
  #put latch down to start data sending
  clock.value(0)
  latch.value(0)
  clock.value(1)
  
  #clear some
  for i in [7,6,5,4,3,2,1,0]:
      clock.value(0)
      data.value(1)
      clock.value(1)
  for i in [7,6,5,4,3,2,1,0]:
      clock.value(0)
      data.value(0)
      clock.value(1)
  
  #write Values
  #"""
  for i in [7,6,5,4,3,2,1,0]:
    clock.value(0)
    data.value(int(inputList[1][i]))
    clock.value(1)
  for i in [7,6,5,4,3,2,1,0]:
    clock.value(0)
    data.value(int(inputList[0][i]))
    clock.value(1)
  #"""
  
  
  clock.value(0)
  latch.value(1)
  clock.value(1)
  
  #backup inputString
  lastOldInputList = inputList






#main program, calling shift register function





#rotateImage 270 degrees 8X8 image
def rotateStrImage270(input_image_array):
    flipped_image_String_array = [["0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0"]]
    for i in [0,1,2,3,4,5,6,7]:
        for j in [0,1,2,3,4,5,6,7]:
            flipped_image_String_array[i][j] = input_image_array[j][i]
        flipped_image_String_array[i] = "".join(flipped_image_String_array[i])
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
@timed_function
def calculateImageRegisterPatternsRbR(input_image_array):
    stringVerInput = ["{:08b}".format(input_image_array[i]) for i in range(len(input_image_array))]
    
    masterCountRange = [0,1,2,3,4,5,6,7]
    binaryImageOutStream = {
        "Data":[],#[Row][Col] == [RRRRRRRR, CCCCCCCC] #R='row', C='Col' flip Col
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
@timed_function
def calculateImageRegisterPatternsCbC(input_image_array):
    stringVerInput = ["{:08b}".format(input_image_array[i]) for i in range(len(input_image_array))]
    stringVerInput = rotateStrImage270(stringVerInput)
    
    
    masterCountRange = [0,1,2,3,4,5,6,7]
    binaryImageOutStream = {
        "Data":[],#[Row][Col] == [RRRRRRRR, CCCCCCCC] #R='row', C='Col' flip Col
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
@timed_function
def calculateImageRegisterPatternsRbRandCbC(input_image_array):
    stringVerInput_RbR = ["{:08b}".format(input_image_array[i]) for i in range(len(input_image_array))]
    stringVerInput_CbC = ["{:08b}".format(input_image_array[i]) for i in range(len(input_image_array))]
    
    stringVerInput_CbC = rotateStrImage270(stringVerInput_CbC)
    
    masterCountRange = [0,1,2,3,4,5,6,7]
    
    
    binaryImageOutStreamRbR = {
        "Data":[],#[Row][Col] == [RRRRRRRR, CCCCCCCC] #R='row', C='Col' flip Col
        "DataImagesPixelCount":[],#List of The Images Pixel Count the Data will generate
        "DataListLength":0, #length of Data List
        }
    dupe_Col_byte_Row_RbR = [False,False,False,False,False,False,False,False]
    rowIndexer_RbR = [0,1,2,3,4,5,6,7]
    
    binaryImageOutStreamCbC = {
        "Data":[],#[Row][Col] == [RRRRRRRR, CCCCCCCC] #R='row', C='Col' flip Col
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
            #check for Similar Cols and mark the Rows
            #calculate Column
            bit_byte_Col_Str_CbC = stringVerInput_CbC[indexColumn] #create Column Binary
            tempList_CbC = ["0", "0", "0", "0", "0", "0", "0", "0"] #create Row Binary
            dupe_Col_byte_Row_Value_CbC = False
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
    
    
    return imageCheck_Cache








#converts bitString to integer
def bitString2int(bitString):
    #find a way to make this Much faster
    #try int(bitString, 2)
    integerOut = 0
    for index in range(len(bitString)):
        integerOut += (2**(len(bitString)-1-index))*(bitString[index]=="1")
    #print(bitString, "==", integerOut, "==", "{:08b}".format(integerOut))
    return integerOut




def subtract8X8BitImagefrom8X8BitImage(minuend_StrBitImage, subtrahend_StrBitImage):
    #helpful: #https://stackoverflow.com/questions/1228299/changing-one-character-in-a-string
    #"ms":"d"
    truthTable = {"00":"0",
                  "01":"2", #shoud not Happen
                  "10":"1",
                  "11":"0",
                  }
    #image format: RowByRow, "1"=High, "0"=Low
    difference_StrBitImage = ["00000000","00000000","00000000","00000000","00000000","00000000","00000000","00000000"]
    #indexY = Row,  indexX = Column
    for indexY in [0,1,2,3,4,5,6,7]:
        bitStrList = list(difference_StrBitImage[indexY])
        for indexX in [0,1,2,3,4,5,6,7]:
            bitStrList[indexX] = truthTable[ ( minuend_StrBitImage[indexY][indexX] + subtrahend_StrBitImage[indexY][indexX] ) ]
        difference_StrBitImage[indexY] = "".join( bitStrList )
    difference_StrBitImage = [bitString2int( difference_StrBitImage[i] ) for i in [0,1,2,3,4,5,6,7]]
    
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
        ###"DataImages":[],#List of Images the Data will generate
        "DataImagesPixelCount":[],#List of The Images Pixel Count the Data will generate
        "DataListLength":0,#length of Data List
        "DataCalculateType":[],#calculation Type ["CbC", "RbR"]
        }
    
    blank_8x8ByteImage = [0,0,0,0,0,0,0,0]
    cycle_input_image_array = mipf.convertImageFormat2RbR(  input_image_array )
    
    bestOption = "None"
    cycleCount = 0 # =could be replaced with binaryImageOutStream["DataListLength"]
    if fastCalculation==False:
        #check if complete, if complete Break out of WhileTrue loop
        while ( ( (cycleCount >=1 )or(cycleCount!=0) ) and (cycle_input_image_array == blank_8x8ByteImage) )==False:
            #create String copy of cycle_input_image_array
            cycle_input_image_Str_array = ["{:08b}".format(cycle_input_image_array[i]) for i in [0,1,2,3,4,5,6,7]]
            
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
            for newIndex in range(imageCheck_Cache["RbR"]["DataListLength"]):
                LargestPixelCount_RbR_Index_Cache = ( newIndex if (imageCheck_Cache["RbR"]["DataImagesPixelCount"][newIndex] > imageCheck_Cache["RbR"]["DataImagesPixelCount"][ LargestPixelCount_RbR_Index_Cache ]) else LargestPixelCount_RbR_Index_Cache )
            for newIndex in range(imageCheck_Cache["CbC"]["DataListLength"]):
                LargestPixelCount_CbC_Index_Cache = ( newIndex if (imageCheck_Cache["CbC"]["DataImagesPixelCount"][newIndex] > imageCheck_Cache["CbC"]["DataImagesPixelCount"][ LargestPixelCount_CbC_Index_Cache ]) else LargestPixelCount_CbC_Index_Cache )
            
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
            binaryImageOutStream["Data"].append( imageCheck_Cache[bestOption]["Data"][ LargestPixelCount_Index_Cache[bestOption] ] )
            #tempDataStream = imageCheck_Cache[bestOption]["Data"][ LargestPixelCount_Index_Cache[bestOption] ]
            #binaryImageOutStream["DataImages"].append( calculateResultImage(tempDataStream[0], tempDataStream[1]) )
            #del tempDataStream
            binaryImageOutStream["DataImagesPixelCount"].append( imageCheck_Cache[bestOption]["DataImagesPixelCount"][ LargestPixelCount_Index_Cache[bestOption] ] )
            binaryImageOutStream["DataListLength"] += 1
            binaryImageOutStream["DataCalculateType"].append( bestOption )
            
            #prepare for next cycle
            differenceBitStrArray = subtract8X8BitImagefrom8X8BitImage(cycle_input_image_Str_array, calculateResultImage( imageCheck_Cache[bestOption]["Data"][ LargestPixelCount_Index_Cache[bestOption] ][0], imageCheck_Cache[bestOption]["Data"][ LargestPixelCount_Index_Cache[bestOption] ][1]) )
            cycle_input_image_array = differenceBitStrArray
            
            
            cycleCount += 1
            del LargestPixelCount_Index_Cache
            del bestOption
            del imageCheck_Cache
    elif fastCalculation==True:
        image_Cache = calculateImageRegisterPatternsRbR( cycle_input_image_array )
        binaryImageOutStream["Data"] = image_Cache["Data"]
        binaryImageOutStream["DataListLength"] = len(image_Cache["Data"])
        binaryImageOutStream["DataImagesPixelCount"] = image_Cache["DataImagesPixelCount"]
        binaryImageOutStream["DataCalculateType"] = "FastCal"
        #for index in range(len(image_Cache["Data"])):
        #    tempDataStream = image_Cache["Data"][ index ]
        #    binaryImageOutStream["DataImages"].append( calculateResultImage(tempDataStream[0], tempDataStream[1]) )
        #del tempDataStream
        del image_Cache
        return binaryImageOutStream
        
    gc.collect()
    
    #print("", binaryImageOutStream)
    return binaryImageOutStream
    
    





"""
Start Up Wait
"""
better_shift_out_update(["00000000","11111111"],dataPIN ,clockPIN,latchPIN)#clear
utime.sleep(2) #sleep 2 Seconds

"""
Sub Calculations Complete
"""



#print from Binary image stream
#@timed_function
def shiftFromBinaryImageStream(binaryImageOutStream,data,clock,latch, clearFlag = True):
    displayTimeUS = 8000 #microseconds to display frame
    #helpful: #https://docs.micropython.org/en/v1.15/library/utime.html
    
    if "Data" in binaryImageOutStream:
        for dataIndex in range(len(binaryImageOutStream["Data"])):
            better_shift_out_update(binaryImageOutStream["Data"][dataIndex], dataPIN , clockPIN, latchPIN)
            utime.sleep_us(int(displayTimeUS/len(binaryImageOutStream["Data"])))
            #print(len(binaryImageOutStream["Data"]), binaryImageOutStream["Data"][dataIndex])
            #utime.sleep(1)
    if clearFlag:
        better_shift_out_update(["00000000","11111111"],dataPIN ,clockPIN,latchPIN)#clear
        pass






"""
Creating Global variables
"""
display_Image_Name = "_Noise"
gc.collect()



"""
Second Thread Function
"""
sLock = _thread.allocate_lock() #baton

def second_thread_CoreTask():
    print("second_thread_CoreTask")
    while True:
        ###print("Entering second Thread")
        
        #print("T2 - Memory: ", micropython.mem_info())
        
        #inititalizing d with dir()
        ##d = dir()
        #printing the directory
        ##print(d)
        
        
        # inititalizing g with globals()
        ##g = globals()
        ##print(g)
        #if (display_Image_Name!=""):
        if (display_Image_Name=="_Noise"):
            randomImageArray = [0,0,0,0,0,0,0,0]
            for i in range(8):
                randomImageArray[i] = random.randint(0, 255)
            shiftFromBinaryImageStream( calculateEfficientImageRegisterPatterns( randomImageArray, fastCalculation = True ) ,dataPIN ,clockPIN,latchPIN)
        elif (display_Image_Name in registerDisplayImageCache.keys()):
            shiftFromBinaryImageStream( registerDisplayImageCache[ display_Image_Name ] ,dataPIN ,clockPIN,latchPIN)
        
        utime.sleep_ms(5)
        ###print("Exiting second Thread")
        sLock.release()












"""
Precompile List
"""



@timed_function
def runPreComple():
    import json
    global registerDisplayImageCache
    displayImageArray = []
    
    imageNameList = []
    #imageNameList += loading_images.keys()
    #imageNameList += letters8x8_images.keys()
    imageNameList += _MasterImageDictionary.keys() #Main Dictionary
    
    lframeIndex = 0
    for imageName in imageNameList:
        #displayImageArray = (letters8x8_images[ imageName ] if (imageName in letters8x8_images) else displayImageArray) #check letters8x8_images
        #displayImageArray = (loading_images[ imageName ] if (imageName in loading_images) else displayImageArray) #check loading_images
        displayImageArray = (_MasterImageDictionary[ imageName ] if (imageName in _MasterImageDictionary) else displayImageArray) #check _MasterImageDictionary
        gc.collect()
        print("1-FreeMemory: ", gc.mem_free())
        if (imageName in registerDisplayImageCache)==False:
            #registerDisplayImageCache[ imageName ] = calculateEfficientImageRegisterPatterns( convertImageFormat2RbR( convertImageFormat2PixelList( displayImageArray ) ) )
            #registerDisplayImageCache[ imageName ] = calculateEfficientImageRegisterPatterns( convertImageFormat2RbR( displayImageArray ) )
            registerDisplayImageCache[ imageName ] = calculateEfficientImageRegisterPatterns( displayImageArray )
        print("2-FreeMemory: ", gc.mem_free())
        
        print(f"lframeIndex:{lframeIndex}")
        
        #display a beautiful Loading animation!
        aniframeName = _MasterAnimationDictionary["loadingAnimation"][ lframeIndex % len( _MasterAnimationDictionary["loadingAnimation"] ) ]
        if aniframeName in registerDisplayImageCache.keys():
            shiftFromBinaryImageStream( registerDisplayImageCache[ aniframeName ] ,dataPIN ,clockPIN,latchPIN)
        lframeIndex += 1
        
    #delete variables that are not longer Needed!, help prevernt "memory leaks", "memory corruption" and "program crashes"
    del imageNameList
    del displayImageArray
    del lframeIndex, aniframeName
    # Serialize data into file:
    json.dump( registerDisplayImageCache, open( "file_name.json", 'w' ) )



import json

try:
    # Read data from file:
    registerDisplayImageCache = json.load( open( "file_name.json", 'r' ) )
except OSError:  # open failed
   # handle the file open case
   runPreComple()


del _MasterImageDictionary






"""
Start Second Thread
"""
gc.collect()
print("FreeMemory: ", gc.mem_free())
#_thread.start_new_thread(second_thread_CoreTask, ())


"""
Entering Main Loop Forever
"""
accu0 = 0
accu1 = 0

nameCacheList = []
nameCacheList += registerDisplayImageCache.keys()

#https://docs.micropython.org/en/latest/reference/speed_python.html

while True:
    #sLock.acquire()
    gc.collect() #clean up Ram
    #print("");print("");print("");print("");print("");print("");
    print("Entering main Thread")
    print("FreeMemory: ", gc.mem_free())
    
    ###print("T1 - Memory: ", micropython.mem_info())
    lettersList = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    imageName = lettersList[accu0 % len(lettersList)]
    #imageName = nameCacheList[ accu0 % len(nameCacheList) ]
    
    display_Image_Name = imageName
    print(display_Image_Name)
    
    if (display_Image_Name in registerDisplayImageCache):
        shiftFromBinaryImageStream( registerDisplayImageCache[ display_Image_Name ] ,dataPIN ,clockPIN,latchPIN)
        
    randomImageArray = [0,0,0,0,0,0,0,0]
    for i in range(8):
        randomImageArray[i] = random.randint(0, 255)
    randomImageArray = mipf.convertImageFormat2PixelList( randomImageArray )
    shiftFromBinaryImageStream( calculateEfficientImageRegisterPatterns( randomImageArray, fastCalculation = True ) ,dataPIN ,clockPIN,latchPIN)
    shiftFromBinaryImageStream( calculateEfficientImageRegisterPatterns( randomImageArray, fastCalculation = False ) ,dataPIN ,clockPIN,latchPIN)
    
    
    
    #inititalizing d with dir()
    """
    d = dir()
    #printing the directory
    print(d)
    #"""
    
    # inititalizing g with globals()
    """
    g = globals()
    print(g)
    #"""
    
    
    accu1 += 1
    if accu1>= (32/2):
        accu0 += 1
        accu1 = 0
    accu1 %= 1024
    
    print("FreeMemory: ", gc.mem_free())
    print("Exiting main Thread")
    print("")
    utime.sleep_ms(1000)
    #sLock.release()

sLock.acquire()

