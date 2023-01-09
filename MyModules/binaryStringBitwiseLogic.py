# Author: Darrien J-G Varrette (TerrienDJV5)
# Date: Nov 24th, 2022
# Version: 1.0

"""Helpful URLs
https://www.geeksforgeeks.org/private-methods-in-python/
https://frankcomputerscience.wordpress.com/chapter-3/
https://pythonexamples.org/python-find-index-of-item-in-list/
https://www.digitalocean.com/community/tutorials/understanding-class-and-instance-variables-in-python-3
https://docs.micropython.org/en/latest/genrst/builtin_types.html

"""


logicGatesTruthTable_old = {
    "NOT" :{"A":[0,1], "X":[1,0]},
    "AND" :{"A":[0,1,0,1], "B":[0,0,1,1], "X":[0,0,0,1]},
    "NAND":{"A":[0,1,0,1], "B":[0,0,1,1], "X":[1,1,1,0]},
    "OR"  :{"A":[0,1,0,1], "B":[0,0,1,1], "X":[0,1,1,1]},
    "NOR" :{"A":[0,1,0,1], "B":[0,0,1,1], "X":[1,0,0,0]},
    "XOR" :{"A":[0,1,0,1], "B":[0,0,1,1], "X":[0,1,1,0]},
    "XNOR":{"A":[0,1,0,1], "B":[0,0,1,1], "X":[1,0,0,1]},
    } #(A)input #(B)input #(X)result


class logicGates(object):
    truthTable = {
        "NOT" :{"A":["0","1"], "X":["1","0"]},
        "AND" :{"AB":["00","01","10","11"], "X":["0","0","0","1"]},
        "NAND":{"AB":["00","01","10","11"], "X":["1","1","1","0"]},
        "OR"  :{"AB":["00","01","10","11"], "X":["0","1","1","1"]},
        "NOR" :{"AB":["00","01","10","11"], "X":["1","0","0","0"]},
        "XOR" :{"AB":["00","01","10","11"], "X":["0","1","1","0"]},
        "XNOR":{"AB":["00","01","10","11"], "X":["1","0","0","1"]},
        } #(A)input #(B)input #(X)result
    



class BinaryStringBitwiseLogic(object):
    def __init__(self):
        
        pass
        
    # Declaring private method
    def __returnLargestValueAndDiff(self, xl, yl):
        size = (xl if (xl > yl) else yl)#get largest Size
        sizediff = xl - yl #if positive then x>y #if negitive then x<y
        return size,sizediff
    
    
    def __return_x_y_size_sizediff(self, xin, yin):
        x,y = xin,yin
        size,sizediff = self.__returnLargestValueAndDiff(len(x), len(y))
        leadingZero = "0"*abs(sizediff)
        if sizediff!=0:
            if sizediff>0:
                y = leadingZero + y
            elif sizediff<0:
                x = leadingZero + x
        return x,y,size,sizediff
                
            
    # Declaring private method
    def __replaceCharacterAtPos(self, stringInput, new_character, position_index):
        temp = list(stringInput)
        temp[position_index] = new_character
        stringOutput = "".join(temp)
        return stringOutput
    
    
    def __bitwiseNOT(self, xin, totalBitSize = None):
        #totalBitSize = (len(xin) if totalBitSize==None else totalBitSize)
        """
        x = xin
        if len(xin)<totalBitSize:
            x = "0"*(totalBitSize-len(xin)) + xin
        """
        if totalBitSize!=None:
            x,y,size,sizediff = self.__return_x_y_size_sizediff(xin, "0"*totalBitSize)
        else:
            x = xin
        
        #z = "0"*size #z starts as all '0' the length of 'size'
        #z = list( z )
        
        #selectedTruthTable = logicGates().truthTable["NOT"]
        #for index in range(totalBitSize):
        #    find_index = selectedTruthTable["A"].index( x[index] )
        #    z[index] = selectedTruthTable["X"][find_index]
        z = list(x)
        for index in range(len(z)):
            z[index] = ("1" if (z[index] == "0") else "0")
            
        return "".join(z)
    
    def bitwiseNOT(self, xin, totalBitSize = None):
        if totalBitSize==None:
            return self.__bitwiseNOT(xin, len(xin))
        else:
            return self.__bitwiseNOT(xin, totalBitSize)
    
    def bitwiseAND(self, xin, yin):
        x,y,size,sizediff = self.__return_x_y_size_sizediff(xin, yin)
        
        z = "0"*size #z starts as all '0' the length of 'size'
        z = list( z )
        selectedTruthTable = logicGates().truthTable["AND"]
        for index in range(size):
            find_index = selectedTruthTable["AB"].index( (x[index] + y[index]) )
            z[index] = selectedTruthTable["X"][find_index]
        return "".join(z)
        
        
    def bitwiseOR(self, xin, yin):
        x,y,size,sizediff = self.__return_x_y_size_sizediff(xin, yin)
        
        z = "0"*size #z starts as all '0' the length of 'size'
        z = list( z )
        selectedTruthTable = logicGates().truthTable["OR"]
        for index in range(size):
            find_index = selectedTruthTable["AB"].index( (x[index] + y[index]) )
            z[index] = selectedTruthTable["X"][find_index]
        return "".join(z)
    
    def bitwiseXOR(self, xin, yin):
        x,y,size,sizediff = self.__return_x_y_size_sizediff(xin, yin)
        
        z = "0"*size #z starts as all '0' the length of 'size'
        z = list( z )
        selectedTruthTable = logicGates().truthTable["XOR"]
        for index in range(size):
            find_index = selectedTruthTable["AB"].index( (x[index] + y[index]) )
            z[index] = selectedTruthTable["X"][find_index]
        return "".join(z)

testBSBL = BinaryStringBitwiseLogic()
print("result (NOT):", testBSBL.bitwiseNOT("10101010") )
print("result (NOT):", testBSBL.bitwiseNOT("10101010", 16) )
print("result (AND):", testBSBL.bitwiseAND("00001111","10101010") )
print("result (OR):", testBSBL.bitwiseOR("00001111","10101010") )
print("result (XOR):", testBSBL.bitwiseXOR("00001111","10101010") )
del testBSBL


