import tkinter as tk # base tkinter
from tkinter import ttk as ttk # tkinter DLC
import pandas as pan # handling the excel files 
import numpy as np # randomization
import os # file handling
import time # for inducing delays

# Classes
class UnknownArgument:
    """An argument is not recognized by the function."""

# Function
def placeholder():
    print("[LOG] - placeholder() called.")
    pass

def excelFileNameConstant(fileName):
    """Gets the file path of the logo"""
    mainDirectory = os.path.dirname(os.path.abspath(__file__))
    logoPath = os.path.join(mainDirectory, "..", "levels", fileName)
    filenameConstant = os.path.normpath(logoPath)
    return filenameConstant

def readExcel(filename):
    """reads the Excel file into a DataFrame"""
    print("[readExcel] - Argument Recieved.")
    output = pan.read_excel(io=excelFileNameConstant("Levels.xlsx"), sheet_name = filename, index_col=[0])
    print("[readExcel] - Output returned")
    return output

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

def logoFileNameConstant():
    """Gets the file path of the logo"""
    mainDirectory = os.path.dirname(os.path.abspath(__file__))
    logoPath = os.path.join(mainDirectory, "..", "images", "logo.png")
    filenameConstant = os.path.normpath(logoPath)
    return filenameConstant

def imageFileNameConstant(fileName):
    """Gets the file path of the logo"""
    mainDirectory = os.path.dirname(os.path.abspath(__file__))
    logoPath = os.path.join(mainDirectory, "..", "images", fileName)
    filenameConstant = os.path.normpath(logoPath)
    return filenameConstant

def dtColumns(DataFrame):
    """extracts a column names of a dataframe and is converted to a list."""
    return DataFrame.columns.tolist()

def extractDataFrames(dataframe, levelName = "Level1"):
    """extracts a column of a dataframe and is converted to a list."""
    nestedLevels = dataframe[levelName].tolist()
    return nestedLevels

# ...
# Main
def Quiz(strLevel, strOption):
    """Quiz itself"""
    # constants
    quizItems = 10
    # local Functions:
    def gugugaga():
        pass

    # Encoders
    match strOption:
        case "DEC to ASCII":
            strQuestionMode = "decimal"
            strAnswerMode = "original"
        case "ASCII to DEC":
            strQuestionMode = "original"
            strAnswerMode = "decimal"
        case "Binary To ASCII":
            strQuestionMode = "binary"
            strAnswerMode = "original"
        case "ASCII to Binary":
            strQuestionMode = "original"
            strAnswerMode = "binary"
        case "Binary to DEC":
            strQuestionMode = "binary"
            strAnswerMode = "decimal"
        case "DEC to Binary":
            strQuestionMode = "decimal"
            strAnswerMode = "binary"
    quizBaselist = randomSelection(extractDataFrames(readExcel("Levels.xlsx"), strLevel), quizItems)
    quizQuestionList = omniEncoder(quizBaselist, strQuestionMode)
    quizAnswerList = omniEncoder(quizBaselist, strAnswerMode)

    # UI
    quizwindow = tk.Tk()
    quizwindow.title("Game Activity")
    quizwindow.
    

# ...