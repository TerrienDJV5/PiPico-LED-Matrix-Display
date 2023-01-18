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

#python -m mpy_cross "matrix_image_prcessing_functions.py" how to Compile to .mpy


import sys
sys_mpy = sys.implementation._mpy
arch = [None, 'x86', 'x64',
    'armv6', 'armv6m', 'armv7m', 'armv7em', 'armv7emsp', 'armv7emdp',
    'xtensa', 'xtensawin'][sys_mpy >> 10]
print('mpy version:', sys_mpy & 0xff)
print('mpy sub-version:', sys_mpy >> 8 & 3)
print('mpy flags:', end='')
if arch:
    print(' -march=' + arch, end='')
print()




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
bitwiseMath = bSBitwiseLogic.BinaryStringBitwiseLogic()
  
bitwise0Str = bitwiseMath.bitwiseNOT( "0000000011111111" )
#bitwise1Str = bitwiseMath.bitwiseAND(bitwise0Str ,"0000000011111111")
#bitwise2Str = bitwiseMath.bitwiseAND(input,"1111111100000000")
#bitwise3Str = bitwiseMath.bitwiseOR( bitwise2Str , bitwise1Str )
  
  
#inputString = bitwiseMath.bitwiseAND(input ,"1111111111111111")
#"""
del bSBitwiseLogic



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
            if binaryImageOutStream["DataFormat"]=="0b":
                better_shift_out_update(binaryImageOutStream["Data"][dataIndex], dataPIN , clockPIN, latchPIN)
            elif binaryImageOutStream["DataFormat"]=="0x":
                dataTemp = binaryImageOutStream["Data"][dataIndex]
                rowRegister = mipf.convert_HexString_to_BitString( dataTemp[0] )
                columnReister = mipf.convert_HexString_to_BitString( dataTemp[1] )
                better_shift_out_update([rowRegister, columnReister], dataPIN , clockPIN, latchPIN)
                del dataTemp, rowRegister, columnReister
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
        sLock.acquire()
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
            randomImageArray = mipf.convertImageFormat2PixelList( randomImageArray )
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
    imageNameList += _MasterImageDictionary.keys() #Main Dictionary
    
    lframeIndex = 0
    for imageName in imageNameList:
        displayImageArray = (_MasterImageDictionary[ imageName ] if (imageName in _MasterImageDictionary) else displayImageArray) #check _MasterImageDictionary
        gc.collect()
        print("1-FreeMemory: ", gc.mem_free())
        if (imageName in registerDisplayImageCache)==False:
            registerDisplayImageCache[ imageName ] = mipf.calculateEfficientImageRegisterPatterns( displayImageArray )
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


#del _MasterImageDictionary







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
    sLock.acquire()
    gc.collect() #clean up Ram
    #print("");print("");print("");print("");print("");print("");
    ##print("Entering main Thread")
    ##print("FreeMemory: ", gc.mem_free())
    
    ###print("T1 - Memory: ", micropython.mem_info())
    lettersList = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    imageName = lettersList[accu0 % len(lettersList)]
    #imageName = nameCacheList[ accu0 % len(nameCacheList) ]
    
    
    display_Image_Name = imageName
    ###print(display_Image_Name)
    
    if (display_Image_Name in registerDisplayImageCache):
        shiftFromBinaryImageStream( registerDisplayImageCache[ display_Image_Name ] ,dataPIN ,clockPIN,latchPIN)
    
    
    
    ##print("Create Random Image")
    randomImageArray = [0,0,0,0,0,0,0,0]
    for i in range(8):
        randomImageArray[i] = random.randint(0, 255)
    #randomImageArray = [0b00000001, 0b00000010, 0b00000100, 0b00001000, 0b00010000, 0b00100000, 0b01000000, 0b10000000]
    randomImageArray = mipf.convertImageFormat2PixelList( randomImageArray )
    #randomImageArray = mipf.resize_Image( randomImageArray, reSizedX=8, reSizedY=8 )
    #randomImageArray = mipf.offset_Image( randomImageArray, offsetX = 0, offsetY = -1 )
    #shiftFromBinaryImageStream( mipf.calculateEfficientImageRegisterPatterns( randomImageArray, fastCalculation = True ) ,dataPIN ,clockPIN,latchPIN)
    #print("Optimize")
    #shiftFromBinaryImageStream( mipf.calculateEfficientImageRegisterPatterns( randomImageArray, fastCalculation = False ) ,dataPIN ,clockPIN,latchPIN)
    
    
    
    
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
    
    ##print("FreeMemory: ", gc.mem_free())
    ##print("Exiting main Thread")
    ##print("")
    
    #utime.sleep_ms(1000)
    sLock.release()

sLock.acquire()

