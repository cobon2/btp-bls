import pandas as pan # handling the excel files 
import numpy as np # randomization
import os

# Todo:
# - make a excel file making function (turn to class whenever posible)
# - make a excel file reading class (Turn to class whernever posible)

# Errors
class InsuficientWords:
    """The provided iterable does not have enough words"""
    # Raised when the input iterable is less than the length of the required output iterable.

class UnknownArgument:
    """An argument is not recognized by the function."""

class CorruptedBinary:
    """The provided binary is not a byte and is considered as an corupted binary line."""

# Functions
def excelFileNameConstant(fileName):
    """Gets the file path of the logo"""
    mainDirectory = os.path.dirname(os.path.abspath(__file__))
    logoPath = os.path.join(mainDirectory, "..", "levels", fileName)
    filenameConstant = os.path.normpath(logoPath)
    return filenameConstant

def writeExcel(sampleDataFrame, filename):
    """reads the Excel file into a DataFrame"""
    print("[writeExcel] - Arguments Recieved.")
    sampleDataFrame.to_excel(excel_writer=excelFileNameConstant("Levels.xlsx"), sheet_name = filename)
    print("[writeExcel] - File Created.")

def readExcel(filename):
    """reads the Excel file into a DataFrame"""
    print("[readExcel] - Argument Recieved.")
    output = pan.read_excel(io=excelFileNameConstant("Levels.xlsx"), sheet_name = filename, index_col=[0])
    print("[readExcel] - Output returned")
    return output

def randomSelection(iterable, length):
    """Selects a set amount of words into a nth size iterable"""
    # note: Uses an improved corrosive sort
    wordBasket = iterable
    wordLength = length
    resultBasket = []
    print("[randomSelection] - Arguments Recieved.")
    for i in range(len(iterable)):
        if wordLength == 0:
            break
        randomIndex = np.random.randint(wordLength)
        resultBasket.append(wordBasket[randomIndex])
        wordBasket.remove(wordBasket[randomIndex])
        wordLength -= 1
        
    print("[randomSelection] - resultBasket returned")
    return resultBasket

def level(iterable):                                                                                                # not done
    """Draws the Quiz project."""
    print("[level] - Argument Recieved.")
    pass

def extractDataFrames(dataframe, levelName = "Level1"):
    "extracts a column of a dataframe and is converted to a list."
    nestedLevels = dataframe[levelName].tolist()
    return nestedLevels

def startupProbe():
    dictTest = {
    "Level1" : ["art", "two", "son", "pie", "law",
                "sir", "way", "map", "mom", "mud", 
                "tea", "dad", "hat", "lab", "ear",
                "fun", "cut", "fax", "pan", "owe"],
    "Level2" : ["care", "meal", "hill", "zone", "dawn",
                "sigh", "chin", "hate", "week", "herd",
                "whole", "harsh", "chair", "first", "quote",
                "child", "level", "fault", "bride", "reach"],
    "Level3" : ["tumble", "orange", "sacred", "valley", "murder",
                "strong", "weapon", "series", "ballet", "defeat",
                "illness", "economy", "pyramid", "lineage", "variety",
                "biscuit", "support", "inflate", "descent", "compact"]
}
    dataframeTest = pan.DataFrame(dictTest)
    dataframeTest.to_excel(excel_writer=excelFileNameConstant("Levels.xlsx"), sheet_name = "Levels.xlsx")
    extractedLevel = extractDataFrames(dataframeTest, levelName = "Level1")
    selectedLevel = randomSelection(extractedLevel, 10)
    print(str(extractedLevel))
    print(str(selectedLevel))
    selectedLevel.sort()
    print(str(selectedLevel))

def omniEncoder(listLevel, output):
    "Converts the string (ASCII) elements into the desired code."
    # must encode sting to binary, ascii, and hex
    # codes in respective order:
    # hexadecimal = hex
    # binary = bin
    # decimal = ord
    if output == "binary":
        # binary Translation
        outputListLevel = listLevel
        for i in range(len(listLevel)):
            wordlist = []
            for letter in listLevel[i]:
                wordlist.append(letter)
            wordlist = map(lambda x : "0" + str(bin(ord(x))[2:len(bin(ord(x)))]), wordlist)
            outputListLevel[i] = " ".join(wordlist)
        return outputListLevel
    elif output == "hexadecimal":
        # hexadecimal Translation
        outputListLevel = listLevel
        for i in range(len(listLevel)):
            wordlist = []
            for letter in listLevel[i]:
                wordlist.append(letter)
            wordlist = map(lambda x : "0" + str(hex(ord(x))[2:len(hex(ord(x)))]), wordlist)
            outputListLevel[i] = " ".join(wordlist)
        return outputListLevel
    elif output == "decimal":
        # decimal translation
        outputListLevel = listLevel
        for i in range(len(listLevel)):
            wordlist = []
            for letter in listLevel[i]:
                wordlist.append(letter)
            wordlist = map(lambda x : "0" + str(ord(x)), wordlist)
            outputListLevel[i] = " ".join(wordlist)
        return outputListLevel
    else:
        raise UnknownArgument

def binaryCheck(text):
    if len(text) == 8:
        print("[binaryCheck] - binary code verified and valid")
    else:
        raise CorruptedBinary

# Testing variables
print(omniEncoder(["PpPPp", "Avacus", "Fireball"], "binary"))
binaryCheck("0101000")


## todo: check the error classes as it seems to be not be working properly.