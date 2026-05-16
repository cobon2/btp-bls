import tkinter as tk # base tkinter
from tkinter import ttk as ttk # tkinter DLC
import pandas as pan # handling the excel files 
import numpy as np # randomization
import os # file handling

# Classes
## Error Classes
class InsuficientWords:
    """The provided iterable does not have enough words"""
    # Raised when the input iterable is less than the length of the required output iterable.

class UnknownArgument:
    """An argument is not recognized by the function."""

class CorruptedBinary:
    """The provided binary is not a byte and is considered as an corupted binary line."""

# Functions:
## placeholder:
def buttonPlaceholder():
    print("[LOG] - buttonPlaceholder() called.")
    pass

def placeholder():
    print("[LOG] - placeholder() called.")
    pass

## Levels
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



## UI


## Translation
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

## support/others
### Editing Program
def editingProgram(iterable):
    # Subfunctions:
    def addEntry():
        editListbox.insert(editListbox.size(), editEntrybox.get())
        editListbox.config(height = editListbox.size())

    def deleteEntry():
        for i in reversed(editListbox.curselection()):
            editListbox.delete(i)

    def saveList():
        outputlist = []
        print(editListbox.curselection())
        outputlist = list(editListbox.get(0, tk.END))
        print(f"[saveList] - Currently saved list: {str(outputlist)}")
        return outputlist
    
    # windowWordEdit
    windowWordEdit = tk.Tk()
    windowWordEdit.title = "Edit"
    wordEditLogo = tk.PhotoImage(file = logoFileNameConstant())
    windowWordEdit.iconphoto(True, wordEditLogo)

    # Three frames:
    ## listbox
    wordEditFrame = ttk.Frame(master=windowWordEdit)
    wordEditFrame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    ## query
    queryEditFrame = ttk.Frame(master=windowWordEdit)
    queryEditFrame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    buttonWordEditAccess = ttk.Frame()
    buttonWordEditAccess.rowconfigure(0, weight=1)
    buttonWordEditAccess.columnconfigure(0, weight=1)
    buttonWordEditAccess.columnconfigure(1, weight=1)
    buttonWordEditAccess.columnconfigure(2, weight=1)
    buttonWordEditAccess.columnconfigure(3, weight=1)
    buttonWordEditAccess.pack()

    # scrollbar
    wordEditFrameScrollbar = ttk.Scrollbar(wordEditFrame)
    wordEditFrameScrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # listbox
    editListbox = tk.Listbox(width = 12, selectmode=tk.MULTIPLE, master= wordEditFrame,
                            font=("Arial", 20))
    editListbox.pack()

    for i in range(len(iterable)):
        editListbox.insert(i, iterable[i])

    editListbox.config(height= editListbox.size())

    # Entrybox
    entryboxLabel = tk.Label(master=queryEditFrame, text="Add Entry:", font=("Arial", 10))
    entryboxLabel.pack(side = tk.LEFT)
    editEntrybox = tk.Entry(master=queryEditFrame)
    editEntrybox.pack(side = tk.RIGHT)

    # buttonWordEditAccess
    addButton = tk.Button(text="Add", command=addEntry, master= buttonWordEditAccess)
    addButton.grid(row=0, column=0)

    deleteButton = tk.Button(text="Delete", command=deleteEntry, master= buttonWordEditAccess)
    deleteButton.grid(row=0, column=1)

    saveButton = tk.Button(text="Save", command=saveList, master= buttonWordEditAccess)
    saveButton.grid(row=0, column=2)

    # wordEditFrame Scrollbar Access
    editListbox['yscrollcommand']=wordEditFrameScrollbar.set
    wordEditFrameScrollbar.config(command=editListbox.yview)

    # mainloop()
    windowWordEdit.mainloop()

### File Handling
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
    return DataFrame.columns.tolist()

def extractDataFrames(dataframe, levelName = "Level1"):
    "extracts a column of a dataframe and is converted to a list."
    nestedLevels = dataframe[levelName].tolist()
    return nestedLevels


# main
def BTPBLS():
    """Main UI"""
    # dataframe Initialization
    levelsDataFrame = readExcel("Levels.xlsx")
    dtColumnName = dtColumns(readExcel("Levels.xlsx"))
    # window(root) settings
    mainWindow = tk.Tk()
    mainWindow.title("BTP-BLS")
    mainWindow.geometry("600x400")
    logo = tk.PhotoImage(file = logoFileNameConstant())
    mainWindow.iconphoto(True, logo)

    ## notebook declaration
    mainNotebook = ttk.Notebook(mainWindow)
    mainNotebook.pack(expand=True)


    # Translation Page
    placeholderTranslationPage = ttk.Frame(mainNotebook) # Placeholder
    placeholderTranslationPage.pack(fill='both', expand=True)
    

    # Game UI
    ## Main Frame
    gameactivityRoot = tk.Frame(mainNotebook)
    gameactivityRoot.rowconfigure(0, weight= 1)
    gameactivityRoot.rowconfigure(1, weight= 1)
    gameactivityRoot.rowconfigure(2, weight= 1)
    gameactivityRoot.columnconfigure(0, weight= 1)
    gameactivityRoot.columnconfigure(1, weight= 1)

    ### Listbox
    gameactivityLevelSelectionLabel = tk.Label(master=gameactivityRoot, text="Level:", font=("Arial", 20, "bold"))
    gameactivityLevelSelectionLabel.grid(row=0, column=0, sticky="W")
    gameactivityLevelSelection = tk.Listbox(master=gameactivityRoot, height=32)
    gameactivityLevelSelection.grid(row=1, column=0, rowspan=2)
    for i in range(len(dtColumnName)):
        gameactivityLevelSelection.insert(i, dtColumnName[i])

    ### Image Statistic
    gameactivityImageLabel = tk.Label(master=gameactivityRoot, text="Statistic:", font=("Arial", 20, "bold"))
    gameactivityImageLabel.grid(row=0, column=1, sticky="W")
    gameactivityImageFrame = tk.Frame(master=gameactivityRoot)
    gameactivityImageFrame.grid(row=1, column=1)
    gameActivityImageLabel = tk.Label(gameactivityImageFrame, text="Play at least 10 games to show statistic.")
    placeholderStatistic = tk.PhotoImage(file=imageFileNameConstant("PlaceholderStatistic.png"))
    gameActivityImageLabel.config(image=placeholderStatistic, compound= tk.BOTTOM)
    gameActivityImageLabel.pack(anchor='n')
    
    ### Mode Selection
    gameactivityModeSelectionFrame = tk.Frame(master=gameactivityRoot)
    gameactivityModeSelectionFrame.grid(row=2, column=1)
    gameactivityModeSelectionFrame.rowconfigure(0, weight=1)
    gameactivityModeSelectionFrame.rowconfigure(1, weight=1)
    gameactivityModeSelectionFrame.rowconfigure(2, weight=1)
    gameactivityModeSelectionFrame.columnconfigure(0, weight=1)
    gameactivityModeSelectionFrame.columnconfigure(1, weight=1)

    gameactivityModeSelectionTitle = tk.Label(master=gameactivityModeSelectionFrame, text= "Mode:",
                                              font=("Arial", 20, "bold"))
    gameactivityModeSelectionTitle.grid(row=0, column=0, sticky='W')
    gameactivityOptionSelectionTitle = tk.Label(master=gameactivityModeSelectionFrame, text= "Options:",
                                              font=("Arial", 20, "bold"))
    gameactivityOptionSelectionTitle.grid(row=0, column=1, sticky='W')

    listModeOptions = ["OCT to ASCII", "ASCII to OCT", "Binary To ASCII",
                       "ASCII to Binary", "Binary to OCT", "OCT to Binary"]
    translationMode = tk.IntVar()
    for i in range(len(listModeOptions)):
        gameactivityModeSelection = tk.Radiobutton(master=gameactivityModeSelectionFrame,
                                               text= listModeOptions[i],
                                               variable=translationMode,
                                               value=i,
                                               pady=10,
                                               command=placeholder)
    gameactivityModeSelection.grid(row=1, column=0, sticky='NW')

    # Page 3: Chart
    placeholderChartPage = ttk.Frame(mainNotebook) # Placeholder
    placeholderChartPage.pack(fill='both', expand=True)


    # mainNotebook Compiling
    mainNotebook.add(placeholderTranslationPage, text='translation')
    mainNotebook.add(gameactivityRoot, text='Game Activity')
    mainNotebook.add(placeholderChartPage, text='chart')

    mainWindow.mainloop()

## mainloop
BTPBLS()