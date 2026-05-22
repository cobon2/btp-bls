import tkinter as tk # base tkinter
from tkinter import ttk as ttk # tkinter DLC
from tkinter.scrolledtext import ScrolledText # Scrollbox Feature of tkinter
from tkinter import messagebox # for displaying errors
import pandas as pan # handling the excel files 
import numpy as np # randomization
import os # file handling
import matplotlib.pyplot as pl # statistic bars
import time # for inducing delays

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

def levelselect():
    """Converts the Listbox Options to a string-appropriate level"""
    # Custom Function Depenencies: dtcolumns(),
    try:
        option = list(gameactivityLevelSelection.curselection()) # sanitizes the listbox options
        levels = dtColumns(levelsDataFrame)
        if option[0] in range(len(levels)):
            gameactivityOptionSelectionPlayLevel.config(text=f"Level: {levels[option[0]]}")
            print(f"[LOG] - radioboxSelect() got {levels[option[0]]}")
            return levels[option[0]]
        else:
            print("[LOG] - levelselect() detected out of range options!")
            pass
    except IndexError:
        print(f"[levelselect] - user has not selected its level option")
        messagebox.showwarning(title="IndexError Raised", message="Error: No Level Selected")

def radioboxSelect():
    """Converts the RadioBox Options to a string-appropriate level"""
    option = translationMode.get()
    print(f"[LOG] - radioboxSelect() got {listModeOptions[option]}")
    return listModeOptions[option]

### GUH
def statisticsButton():
    statisticLevelInitialization(levelselect())

def statisticLevelInitialization(LevelName):
    """statistic Initialization"""
    # Tasks:
    # Load prior txt files
    # process some statistical data
    # plot latest matplotlib
    def average(iterable):
        return sum(iterable)/len(iterable)

    def plotFileNameConstant(fileName):
        """Gets the file path of the matplotlib line plot"""
        mainDirectory = os.path.dirname(os.path.abspath(__file__))
        logoPath = os.path.join(mainDirectory, "..", "statistics", fileName)
        filenameConstant = os.path.normpath(logoPath)
        return filenameConstant
    
    def streakWinsConstant():
        streakWins = 0
        for i in range(len(listWins)):
            if listWins[i] > 0:
                streakWins += 1
            else:
                streakWins = 0
    
    # inputs:
    levelChosen = levelselect()
    listWins = txtToIntList(f"{LevelName} Win Statistic.txt")
    listLoss = txtToIntList(f"{LevelName} Loss Statistic.txt")
    
    if (len(listWins) >= 10) and (len(listLoss) >= 10):
        # globals
        global meanWinData
        global sumWinData
        global sumLoseData
        global gameActivityImageLabel
        global placeholderStatistic

        # Data Processing
        meanWinData = average(listWins)
        sumWinData = sum(listWins)
        sumLoseData = sum(listLoss)

        # Plotting
        pl.plot(range(len(listWins)), listWins)
        pl.title(levelChosen)
        pl.xlabel("Timeline")
        pl.ylabel("Wins")

        # plot Saving
        currentDir = os.getcwd()
        tempDir = os.path.dirname(os.path.abspath(__file__))
        tempDir = os.path.join(tempDir, "..", "statistics")
        os.chdir(tempDir)
        pl.savefig(f"{levelChosen}_Statistic.png", dpi = 300, bbox_inches='tight')

        # test display
        statisticwindow = tk.Tk()
        statisticwindow.title("Statistic")
        print(os.getcwd())
        #plotFileNameConstant(f"{levelChosen}_Statistic.png")
        print(levelChosen)
        #gameActivityImageLabel.destroy()
        placeholderStatistic = tk.PhotoImage(f"{levelChosen}_Statistic.png")
        #gameActivityImageLabel.configure(text=pl.show())
        os.chdir(currentDir)

        statisticFrame = tk.Frame(master=statisticwindow)
        statisticFrame.pack()

        statisticFrame.rowconfigure(0, weight=1)
        statisticFrame.rowconfigure(1, weight=1)
        statisticFrame.rowconfigure(2, weight=1)
        statisticFrame.rowconfigure(3, weight=1)
        statisticFrame.rowconfigure(4, weight=1)

        statisticFrame.columnconfigure(0, weight=1)
        statisticFrame.columnconfigure(1, weight=1)

        statisticText1 = tk.Label(master=statisticFrame, text="Statistics", font=("Arial", 20, "bold"))
        statisticText1.grid(column=0, row=0, sticky=tk.W)

        statisticText2 = tk.Label(master=statisticFrame, text="Total Wins:")
        statisticText2.grid(column=0, row=1, sticky=tk.W)

        statisticText3 = tk.Label(master=statisticFrame, text="Mean Wins:")
        statisticText3.grid(column=0, row=2, sticky=tk.W)

        statisticText4 = tk.Label(master=statisticFrame, text="Total Losses:")
        statisticText4.grid(column=0, row=3, sticky=tk.W)

        statisticText5 = tk.Label(master=statisticFrame, text=sumWinData)
        statisticText5.grid(column=1, row=1, sticky=tk.W)

        statisticText6 = tk.Label(master=statisticFrame, text=meanWinData)
        statisticText6.grid(column=1, row=2, sticky=tk.W)

        statisticText7 = tk.Label(master=statisticFrame, text=sumLoseData)
        statisticText7.grid(column=1, row=3, sticky=tk.W)

        statisticText8 = tk.Label(master=statisticFrame, text=pl.show())
        statisticText8.grid(column=1, row=4, sticky=tk.W)


    else:
        print("[statistics] - less than 10 elements found between the provided elements.")
        pass
#

## UI
def Quiz():
    # strLevel, strOption
    """Quiz itself"""
    # local Functions:
    def funcDelete():
        """Deletes the entry"""
        quizEntrybox.delete(0, tk.END)
    
    def nextPage():
        """loads the next page of the question."""
        # saving userInput
        global page
        pages = page
        userAnswers[pages] = quizEntrybox.get()
        # move to next
        pages += 1
        print(f"[nextPage] page: {pages+1}")

        # modifying the next page:
        if pages == len(userAnswers) - 1:
            quizQuestion.config(text=quizQuestionList[pages])
            quizPreviousButton.config(state="active")
            quizNextButton.config(state="disabled")
            quizSubmitButton.config(state="active")
            quizQuestionCount.config(text=f"Question {len(userAnswers)}")
            if (userAnswers[page] == "Translate") or (userAnswers[page] == ""):
                quizEntrybox.delete(0, tk.END)
                quizEntrybox.insert(0, "Translate")
            else:
                quizEntrybox.delete(0, tk.END)
                quizEntrybox.insert(0, userAnswers[page])

            quizPreviousButton["relief"] = "raised"
            quizNextButton["relief"] = "sunken"
            quizSubmitButton["relief"] = "raised"

        elif pages == 0:
            quizQuestion.config(text=quizQuestionList[pages])
            quizPreviousButton.config(state="disabled")
            quizNextButton.config(state="active")
            quizSubmitButton.config(state="disabled")
            quizQuestionCount.config(text="Question 1")
            if (userAnswers[page] == "Translate") or (userAnswers[page] == ""):
                quizEntrybox.delete(0, tk.END)
                quizEntrybox.insert(0, "Translate")
            else:
                quizEntrybox.delete(0, tk.END)
                quizEntrybox.insert(0, userAnswers[page])

            quizPreviousButton["relief"] = "sunken"
            quizNextButton["relief"] = "raised"
            quizSubmitButton["relief"] = "sunken"
        else:
            quizQuestion.config(text=quizQuestionList[pages])
            quizQuestionCount.config(text="Question " + str(pages + 1))
            quizPreviousButton.config(state="active")
            quizNextButton.config(state="active")
            quizSubmitButton.config(state="disabled")
            if (userAnswers[page] == "Translate") or (userAnswers[page] == ""):
                quizEntrybox.delete(0, tk.END)
                quizEntrybox.insert(0, "Translate")
            else:
                quizEntrybox.delete(0, tk.END)
                quizEntrybox.insert(0, userAnswers[page])

            quizPreviousButton["relief"] = "raised"
            quizNextButton["relief"] = "raised"
            quizSubmitButton["relief"] = "sunken"
        page = pages
    
    def previousPage():
        """loads the next page of the question."""
        # saving userInput
        global page
        pages = page
        userAnswers[pages] = quizEntrybox.get()
        # move to next
        pages -= 1
        print(f"[nextPage] page: {pages+1}")

        # modifying the next page:
        if pages == len(userAnswers) - 1:
            quizQuestion.config(text=quizQuestionList[pages])
            quizPreviousButton.config(state="active")
            quizNextButton.config(state="disabled")
            quizSubmitButton.config(state="active")
            if (userAnswers[page] == "Translate") or (userAnswers[page] == ""):
                quizEntrybox.delete(0, tk.END)
                quizEntrybox.insert(0, "Translate")
            else:
                quizEntrybox.delete(0, tk.END)
                quizEntrybox.insert(0, userAnswers[page])

            quizPreviousButton["relief"] = "raised"
            quizNextButton["relief"] = "sunken"
            quizSubmitButton["relief"] = "raised"

        elif pages == 0:
            quizQuestion.config(text=quizQuestionList[pages])
            quizPreviousButton.config(state="disabled")
            quizNextButton.config(state="active")
            quizSubmitButton.config(state="disabled")
            quizQuestionCount.config(text="Question 1")
            if (userAnswers[page] == "Translate") or (userAnswers[page] == ""):
                quizEntrybox.delete(0, tk.END)
                quizEntrybox.insert(0, "Translate")
            else:
                quizEntrybox.delete(0, tk.END)
                quizEntrybox.insert(0, userAnswers[page])

            quizPreviousButton["relief"] = "sunken"
            quizNextButton["relief"] = "raised"
            quizSubmitButton["relief"] = "sunken"
        else:
            
            quizQuestion.config(text=quizQuestionList[pages])
            quizQuestionCount.config(text="Question " + str(pages + 1))
            quizPreviousButton.config(state="active")
            quizNextButton.config(state="active")
            quizSubmitButton.config(state="disabled")
            quizEntrybox.insert(0, "Translate")
            if (userAnswers[page] == "Translate") or (userAnswers[page] == ""):
                quizEntrybox.delete(0, tk.END)
                quizEntrybox.insert(0, "Translate")
            else:
                quizEntrybox.delete(0, tk.END)
                quizEntrybox.insert(0, userAnswers[page])

            quizPreviousButton["relief"] = "raised"
            quizNextButton["relief"] = "raised"
            quizSubmitButton["relief"] = "sunken"
        page = pages

    def submit():
        """Verifies user input"""
        # global
        global functionEvaluation
        global CorrectAnswers
        global currentIncorrectAnswers
        ## scrubbing
        userAnswers[page] = quizEntrybox.get()
        quizWindow.destroy()
        def check(userAnswers, answerSheet):
            """checks the user's questions"""
            global functionEvaluation
            output = []
            for i in range(len(userAnswers)):
                if userAnswers[i] == answerSheet[i]:
                    output.append("Correct")
                else:
                    output.append("Incorrect")
            return output
        
        def correctAnswers(iterable):
            """Counts the correct user answers"""
            qtyOfCorrect = 0
            for i in iterable:
                if i == "Correct":
                    qtyOfCorrect += 1
                else:
                    continue
            print(qtyOfCorrect)
            return qtyOfCorrect
        
        def wrongAnswers(iterable):
            """Counts the correct user answers"""
            qtyOfCorrect = 0
            for i in iterable:
                if i == "Incorrect":
                    qtyOfCorrect += 1
                else:
                    continue
            print(qtyOfCorrect)
            return qtyOfCorrect
        
        # iterable saving
        functionEvaluation = check(userAnswers, quizAnswerList)
        currentCorrectAnswers = correctAnswers(functionEvaluation)
        currentIncorrectAnswers = wrongAnswers(functionEvaluation)
        CorrectAnswers = txtToIntList(f"{selectedLevel} Win Statistic.txt")
        IncorrectAnswers = txtToIntList(f"{selectedLevel} Loss Statistic.txt")
        IncorrectAnswers.append(currentCorrectAnswers)
        CorrectAnswers.append(currentCorrectAnswers)
        intListToTxT(CorrectAnswers, f"{selectedLevel} Win Statistic.txt")
        print(f"[correctAnswers] - Total Correct Answers per Session: {CorrectAnswers}" )
        intListToTxT(IncorrectAnswers, f"{selectedLevel} Loss Statistic.txt")
        print(f"[correctAnswers] - Total Incorrect Answers per Session: {IncorrectAnswers}" )
        statisticLevelInitialization(levelselect())
        print("[Quiz.Submit] - Data Saved.")

        

        # UI
        submitWindow = tk.Tk()
        submitWindow.title("Results")
        submitWindow.geometry("480x600")
        submitWindowFrame = tk.Frame(master=submitWindow)
        submitWindowFrame.pack()
        
        submitWindowFrame.columnconfigure(0, weight=1)
        submitWindowFrame.columnconfigure(1, weight=1)
        submitWindowFrame.columnconfigure(2, weight=1)
        submitWindowFrame.columnconfigure(3, weight=1)
        submitWindowFrame.rowconfigure(0, weight=1)
        for i in range(len(userAnswers)):
            submitWindowFrame.rowconfigure(i+1, weight=1)

        submitWindowTitle1 = tk.Label(master=submitWindowFrame, text="Questions",
                                     font=("Arial", 12, "bold"), padx=10)
        submitWindowTitle1.grid(row=0, column=0, sticky="W")
        submitWindowTitle2 = tk.Label(master=submitWindowFrame, text="Your Answer",
                                     font=("Arial", 12, "bold"), padx=10)
        submitWindowTitle2.grid(row=0, column=1, sticky="W")
        submitWindowTitle3 = tk.Label(master=submitWindowFrame, text="Answer",
                                     font=("Arial", 12, "bold"), padx=10)
        submitWindowTitle3.grid(row=0, column=2, sticky="W")
        submitWindowTitle3 = tk.Label(master=submitWindowFrame, text="Remarks",
                                     font=("Arial", 12, "bold"), padx=10)
        submitWindowTitle3.grid(row=0, column=3, sticky="W")
        
        for i in range(len(userAnswers)):
            submitWindowColumn1 = tk.Label(master=submitWindowFrame,
                                           text=f"Question {i+1}")
            submitWindowColumn1.grid(column=0, row=i+1)
            submitWindowColumn2 = tk.Label(master=submitWindowFrame,
                                           text=userAnswers[i])
            submitWindowColumn2.grid(column=1, row=i+1)
            submitWindowColumn3 = tk.Label(master=submitWindowFrame,
                                           text=quizAnswerList[i])
            submitWindowColumn3.grid(column=2, row=i+1)
            submitWindowColumn3 = tk.Label(master=submitWindowFrame,
                                           text=functionEvaluation[i])
            submitWindowColumn3.grid(column=3, row=i+1)
        
        submitWindow.mainloop()

    # Globals:
    global page
    global quizAnswerList
    # constants
    quizItems = 10
    userAnswers = list(range(quizItems))
    for i in range(quizItems):
        userAnswers[i] = 0

    # Encoders
    strOption = radioboxSelect()
    match strOption:
        case "DEC to ASCII":
            strQuestionMode = "decimal"
            strAnswerMode = "ascii"
        case "ASCII to DEC":
            strQuestionMode = "ascii"
            strAnswerMode = "decimal"
        case "Binary To ASCII":
            strQuestionMode = "binary"
            strAnswerMode = "ascii"
        case "ASCII to Binary":
            strQuestionMode = "ascii"
            strAnswerMode = "binary"
        case "Binary to DEC":
            strQuestionMode = "binary"
            strAnswerMode = "decimal"
        case "DEC to Binary":
            strQuestionMode = "decimal"
            strAnswerMode = "binary"
    
    selectedLevel = levelselect()
    baseList = randomSelection(extractDataFrames(readExcel("Levels.xlsx"), levelselect()), quizItems)
    inputBaseList1 = baseList.copy()
    inputBaseList2 = baseList.copy()
    quizQuestionList = omniEncoder(inputBaseList1, strQuestionMode)
    quizAnswerList = omniEncoder(inputBaseList2, strAnswerMode)

    page = 0

    # UI
    quizWindow = tk.Tk()
    quizWindow.title("Game Activity")
    quizWindow.geometry("600x120")
    
    # uncoment when it is at the main program

    quiztitle = tk.Label(text="Translate:", master=quizWindow, font=("Arial", 15, "bold"))
    quiztitle.pack(anchor="n")
    quizQuestionCount = tk.Label(text="Question 1", master=quizWindow, font=("Arial", 8))
    quizQuestionCount.pack()
    quizQuestion = tk.Label(text=quizQuestionList[0], master=quizWindow, font=("Arial", 10))
    quizQuestion.pack()
    quizEntrybox = tk.Entry(master=quizWindow, width=40)
    quizEntrybox.insert(0, "Translate")
    quizEntrybox.pack()

    ## Frame:
    quizButtonFrame = tk.Frame(master=quizWindow)
    quizButtonFrame.pack()
    quizEraseButton = tk.Button(master=quizButtonFrame, text="Delete", command=funcDelete)
    quizEraseButton.pack(side="left")
    quizPreviousButton = tk.Button(master=quizButtonFrame, text="Previous", command=previousPage)
    quizPreviousButton.pack(side="left")
    quizPreviousButton.config(state="disabled")
    quizPreviousButton["relief"] = "sunken"
    quizNextButton = tk.Button(master=quizButtonFrame, text="Next", command=nextPage)
    quizNextButton.pack(side="left")
    quizSubmitButton = tk.Button(master=quizButtonFrame, text="Submit", command=submit)
    quizSubmitButton.pack(side="left")
    quizSubmitButton.config(state="disabled")
    quizSubmitButton["relief"] = "sunken"

    # mainloop()
    quizWindow.mainloop()

## Translation
def omniEncoder(hlistLevelinput, output):
    "Converts the string (ASCII) elements into the desired code."
    # must encode sting to binary, ascii, and hex
    # codes in respective order:
    # hexadecimal = hex
    # binary = bin
    # decimal = ord
    listLevelinput = hlistLevelinput
    originalList = listLevelinput.copy()
    if output == "binary":
        # binary Translation
        outputListLevel = listLevelinput
        for i in range(len(listLevelinput)):
            wordlist = []
            for letter in listLevelinput[i]:
                wordlist.append(letter)
            wordlist = map(lambda x : "0" + str(bin(ord(x))[2:len(bin(ord(x)))]), wordlist)
            outputListLevel[i] = " ".join(wordlist)
        return outputListLevel
    elif output == "hexadecimal":
        # hexadecimal Translation
        outputListLevel = listLevelinput
        for i in range(len(listLevelinput)):
            wordlist = []
            for letter in listLevelinput[i]:
                wordlist.append(letter)
            wordlist = map(lambda x : "0" + str(hex(ord(x))[2:len(hex(ord(x)))]), wordlist)
            outputListLevel[i] = " ".join(wordlist)
        return outputListLevel
    elif output == "decimal":
        # decimal translation
        outputListLevel = listLevelinput
        for i in range(len(listLevelinput)):
            wordlist = []
            for letter in listLevelinput[i]:
                wordlist.append(letter)
            wordlist = map(lambda x : "0" + str(ord(x)), wordlist)
            outputListLevel[i] = " ".join(wordlist)
        return outputListLevel
    elif output == "ascii":
        return originalList 
    else:
        raise UnknownArgument
    
def omniDecoder(iterable, inputMode):
    """Converts any of the existing code into ascii code"""
    match inputMode:
        case "binary":
            for word in range(len(iterable)):
                wordBasket = iterable[word].split()
                for i in range(len(wordBasket)):
                    wordBasket[i] = chr(int(wordBasket[i], 2))
            return "".join(wordBasket)
        case "decimal":
            for word in range(len(iterable)):
                wordBasket = iterable[word].split()
                for i in range(len(wordBasket)):
                    wordBasket[i] = chr(int(wordBasket[i], 10))
            return "".join(wordBasket)
        case "hexadecimal":
            for word in range(len(iterable)):
                wordBasket = iterable[word].split()
                for i in range(len(wordBasket)):
                    wordBasket[i] = chr(int(wordBasket[i], 16))
            return "".join(wordBasket)
        case "original":
            return iterable
        case "ascii":
            return iterable

def binaryCheck(text):
    """Verifies the length of the binary"""
    if len(text) == 8:
        print("[binaryCheck] - binary code verified and valid")
    else:
        raise CorruptedBinary

## support/others
### Editing Program
def editingProgram():
    """Editting Program of the BTPTLS"""
    # Todo: buit a feature that is able to save it to the database
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
        exportDataframe = readExcel("Levels.xlsx")
        exportDataframe[levelselect()] = outputlist
        writeExcel(exportDataframe, "Levels.xlsx")
        return outputlist
    
    iterable = extractDataFrames(readExcel("Levels.xlsx"), levelselect())
    # windowWordEdit
    windowWordEdit = tk.Tk()
    windowWordEdit.title("Edit")

    # Three frames:
    ## query
    queryEditFrame = ttk.Frame(master=windowWordEdit)
    queryEditFrame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    buttonWordEditAccess = ttk.Frame(master=windowWordEdit)
    buttonWordEditAccess.rowconfigure(0, weight=1)
    buttonWordEditAccess.columnconfigure(0, weight=1)
    buttonWordEditAccess.columnconfigure(1, weight=1)
    buttonWordEditAccess.columnconfigure(2, weight=1)
    buttonWordEditAccess.columnconfigure(3, weight=1)
    buttonWordEditAccess.pack()

    ## listbox
    wordEditFrame = ttk.Frame(master=windowWordEdit)
    wordEditFrame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    # buttonWordEditAccess
    addButton = tk.Button(text="Add", command=addEntry, master= buttonWordEditAccess)
    addButton.grid(row=0, column=0)

    deleteButton = tk.Button(text="Delete", command=deleteEntry, master= buttonWordEditAccess)
    deleteButton.grid(row=0, column=1)

    saveButton = tk.Button(text="Save", command=saveList, master= buttonWordEditAccess)
    saveButton.grid(row=0, column=2)

    # scrollbar
    wordEditFrameScrollbar = ttk.Scrollbar(windowWordEdit)
    wordEditFrameScrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # listbox
    editListbox = tk.Listbox(width = 12, height = 1, selectmode=tk.MULTIPLE, master= wordEditFrame,
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

    # wordEditFrame Scrollbar Access
    editListbox['yscrollcommand']=wordEditFrameScrollbar.set
    wordEditFrameScrollbar.config(command=editListbox.yview)

    # mainloop()
    windowWordEdit.mainloop()

# others
def translatebutton():
    """Back-end function of the translation program"""
    def sanitizeList(iterable):
        print(type(iterable))
        if type(iterable) == list:
            extractedword = iterable[0]
        else:
            extractedword = iterable
        extractedlist = extractedword.split('\n')
        if len(extractedlist) > 1:
            extractedlist.pop()
            return extractedlist
        else:
            return extractedlist
    try: 
        # Getting some variables
        translateInput = selectionFrameTranslationCombobox1.get()
        translateOutput = selectionFrameTranslationCombobox2.get()
        translateUserInputList = [""]
        translateUserInputList[0] = scrollentryInputTranslationPage1.get(1.0, tk.END)
        match translateInput:
            case "Hexedecimal":
                translateModeInput = "hexadecimal"
            case "Binary":
                translateModeInput = "binary"
            case "Decimal":
                translateModeInput = "decimal"
            case "ASCII (Text)":
                translateModeInput = "ascii"

        match translateOutput:
            case "Hexedecimal":
                translateModeOutput = "hexadecimal"
            case "Binary":
                translateModeOutput = "binary"
            case "Decimal":
                translateModeOutput = "decimal"
            case "ASCII (Text)":
                translateModeOutput = "ascii"

        # Code Processing
        sanitizedoutput = sanitizeList(omniDecoder(translateUserInputList, translateModeInput))
        #sanitizedoutput.pop()
        print(f"[translatebutton] - sanitizedoutput ({sanitizedoutput})")
        outputlist = omniEncoder(sanitizedoutput, translateModeOutput)
        print(f"[translatebutton] - outputlist ({outputlist})")

        # Placement
        scrollentryInputTranslationPage2.config(state= 'normal')
        scrollentryInputTranslationPage2.delete("1.0", tk.END)
        scrollentryInputTranslationPage2.insert(tk.INSERT, (outputlist[0]))
        scrollentryInputTranslationPage2.config(state= 'disable')
        ## (no selection of options will result in UnboundLocalError)
        ## (incorrect selection will result in ValueError)
    except UnboundLocalError:
        messagebox.showwarning(title="UnboundLocalError Raised", message="Please set your input and output modes.")
    except ValueError:
        messagebox.showwarning(title="UnboundLocalError Raised", message="Please correctly set your input/output modes and input text.")


### File Handling
def logoFileNameConstant():
    """Logo.png file directory constant"""
    mainDirectory = os.path.dirname(os.path.abspath(__file__))
    logoPath = os.path.join(mainDirectory, "..", "images", "Logo.png")
    filenameConstant = os.path.normpath(logoPath)
    return filenameConstant

def imageFileName(fileName):
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

def intListToTxT(iterable, fileName):
    currentDir = os.getcwd()
    tempDir = os.path.dirname(os.path.abspath(__file__))
    tempDir = os.path.join(tempDir, "..", "statistics")
    os.chdir(tempDir)
    tempIterable = iterable
    for i in range(len(tempIterable)):
        tempIterable[i] = str(tempIterable[i])
    exportFile = " - ".join(tempIterable)
    with open(fileName, "w") as file:
        file.write(exportFile)
    os.chdir(currentDir)
    print("[intListToTxT] - Txt overwritten.")

def txtToIntList(fileName):
    currentDir = os.getcwd()
    tempDir = os.path.dirname(os.path.abspath(__file__))
    tempDir = os.path.join(tempDir, "..", "statistics")
    os.chdir(tempDir)
    print(f"[txtToIntList] - {fileName} directory: {os.getcwd()}")
    with open(fileName) as file:
        fileString = file.read()
    outputIterable = fileString.split(" - ")
    for i in range(len(outputIterable)):
        outputIterable[i] = int(outputIterable[i])
    print(f"[txtToIntList] - {fileName} has been converted into an iterable")
    os.chdir(currentDir)
    return outputIterable
    


# main
def BTPBLS():
    """Main UI"""
    # global selection:
    global translationMode
    global listModeOptions
    global gameactivityLevelSelection
    global levelsDataFrame
    global gameactivityOptionSelectionPlayLevel

    global selectionFrameTranslationCombobox1
    global selectionFrameTranslationCombobox2
    global scrollentryInputTranslationPage1
    global scrollentryInputTranslationPage2
    global gameActivityImageLabel
    global placeholderStatistic

    # global variables
    quizSelection = ""

    # dataframe Initialization
    levelsDataFrame = readExcel("Levels.xlsx")
    dtColumnName = dtColumns(levelsDataFrame)
    # window(root) settings
    mainWindow = tk.Tk()
    mainWindow.title("BTP-BLS")
    mainWindow.geometry("780x870")
    mainWindow.config(bg="#546B41")
    logo = tk.PhotoImage(file = logoFileNameConstant())
    mainWindow.iconphoto(True, logo)



    ## notebook declaration
    mainNotebook = ttk.Notebook(mainWindow)
    mainNotebook.pack(expand=True)
    
    

    # Translation Page
    TranslationPage = ttk.Frame(mainNotebook) # Placeholder
    TranslationPage.pack(fill='both', expand=True)

    titleInputTranslationPage1 = tk.Label(master=TranslationPage, text= "Input", font=("Arial", 20, "bold"))
    titleInputTranslationPage1.pack(anchor= tk.W)
    

    scrollentryInputTranslationPage1 = ScrolledText(master=TranslationPage, width=95,  height=21)
    scrollentryInputTranslationPage1.pack(anchor= tk.W)

    selectionFrameTranslation = tk.Frame(master=TranslationPage)
    selectionFrameTranslation.pack(anchor= tk.W)

    selectionFrameTranslationText1 = tk.Label(master = selectionFrameTranslation, text = "Input")
    selectionFrameTranslationText1.pack(side="left")

    translationOptions = ["Hexedecimal", "Binary", "Decimal", "ASCII (Text)"]

    selectionFrameTranslationCombobox1 = ttk.Combobox(master=selectionFrameTranslation, values = translationOptions)
    selectionFrameTranslationCombobox1.set("Code Options (Input)")
    selectionFrameTranslationCombobox1.pack(side="left")

    selectionFrameTranslationText2 = tk.Label(master = selectionFrameTranslation, text = "                                                  ")
    selectionFrameTranslationText2.pack(side="left")

    selectionFrameTranslationText3 = tk.Label(master = selectionFrameTranslation, text = "Output")
    selectionFrameTranslationText3.pack(side="left")

    selectionFrameTranslationCombobox2 = ttk.Combobox(master=selectionFrameTranslation, values = translationOptions)
    selectionFrameTranslationCombobox2.set("Code Options (Output)")
    selectionFrameTranslationCombobox2.pack(side="left")

    selectionFrameTranslationText4 = tk.Label(master = selectionFrameTranslation, text = "                                                  ")
    selectionFrameTranslationText4.pack(side="left")

    selectionFrameTranslationButton = tk.Button(master = selectionFrameTranslation, text = "Translate", width=10, command=translatebutton)
    selectionFrameTranslationButton.pack(side="left")

    titleInputTranslationPage2 = tk.Label(master=TranslationPage, text= "Output", font=("Arial", 20, "bold"))
    titleInputTranslationPage2.pack(anchor= tk.W)

    scrollentryInputTranslationPage2 = ScrolledText(master=TranslationPage, width=95,  height=21)
    scrollentryInputTranslationPage2.pack(anchor= tk.W)
    scrollentryInputTranslationPage2.config(state= 'disabled')

    titleInputTranslationPage2 = tk.Label(master=TranslationPage, text= "\nBinary Translation Program with Basic Learning System", font=("Arial", 10, "italic"))
    titleInputTranslationPage2.pack()

    # Game UI
    ## Main Frame
    gameactivityRoot = tk.Frame(mainNotebook)
    gameactivityRoot.rowconfigure(0, weight= 1)
    gameactivityRoot.rowconfigure(1, weight= 1)
    gameactivityRoot.rowconfigure(2, weight= 1)
    gameactivityRoot.columnconfigure(0, weight= 1)
    gameactivityRoot.columnconfigure(1, weight= 1)
    gameactivityRoot.pack(fill='both', expand=True)

    ### Listbox
    gameactivityLevelSelectionLabel = tk.Label(master=gameactivityRoot, text="Level:", font=("Arial", 20, "bold"))
    gameactivityLevelSelectionLabel.grid(row=0, column=0, sticky="W")
    gameactivityLevelSelection = tk.Listbox(master=gameactivityRoot, height=50)
    gameactivityLevelSelection.grid(row=1, column=0, rowspan=2)
    for i in range(len(dtColumnName)):
        gameactivityLevelSelection.insert(i, dtColumnName[i])

    ### Image Statistic
    gameactivityImageLabel = tk.Label(master=gameactivityRoot, text="Statistic:", font=("Arial", 20, "bold"))
    gameactivityImageLabel.grid(row=0, column=1, sticky="W")
    gameactivityImageFrame = tk.Frame(master=gameactivityRoot)
    gameactivityImageFrame.grid(row=1, column=1)
    gameActivityImageLabel = tk.Label(gameactivityImageFrame, text="Play at least 10 games to show statistic.")
    placeholderStatistic = tk.PhotoImage(file=imageFileName("PlaceholderStatistic.png"))
    gameActivityImageLabel.config(image=placeholderStatistic, compound= tk.BOTTOM)
    gameActivityImageLabel.pack(anchor='n')
    
    ### Mode Selection
    listModeOptions = ["DEC to ASCII", "ASCII to DEC", "Binary To ASCII",
                       "ASCII to Binary", "Binary to DEC", "DEC to Binary"]
    gameactivityModeSelectionFrame = tk.Frame(master=gameactivityRoot)
    gameactivityModeSelectionFrame.grid(row=2, column=1, sticky="NW")
    gameactivityModeSelectionFrame.columnconfigure(0, weight=1)
    gameactivityModeSelectionFrame.columnconfigure(1, weight=1)
    gameactivityModeSelectionFrame.columnconfigure(2, weight=1)
    gameactivityModeSelectionFrame.rowconfigure(0, weight=1)
    gameactivityModeSelectionFrame.rowconfigure(1, weight=1)
    for i in range(len(listModeOptions)):
        gameactivityModeSelectionFrame.rowconfigure(i+1, weight=1)

    gameactivityModeSelectionTitle = tk.Label(master=gameactivityModeSelectionFrame, text= "Mode:",
                                              font=("Arial", 20, "bold"))
    gameactivityModeSelectionTitle.grid(row=0, column=0, sticky='W')

    translationMode = tk.IntVar()
    for i in range(len(listModeOptions)):
        gameactivityModeSelection = tk.Radiobutton(master=gameactivityModeSelectionFrame,
                                               text= listModeOptions[i],
                                               variable=translationMode,
                                               value=i,
                                               pady=10,
                                               command=radioboxSelect)
        gameactivityModeSelection.grid(row=i+1, column=0, sticky='NW')
    
    gameactivityOptionFiller = tk.Frame(master=gameactivityModeSelectionFrame, width=260, height=260)
    gameactivityOptionFiller.grid(row=0, column=1, rowspan=7)
    gameactivityOptionSelectionTitle = tk.Label(master=gameactivityModeSelectionFrame, text= "Options:",
                                              font=("Arial", 20, "bold"))
    gameactivityOptionSelectionTitle.grid(row=0, column=2, sticky='W')

    gameactivityOptionSelectionEdit = tk.Button(master=gameactivityModeSelectionFrame, text="Edit (Unstable)", width=20, command=editingProgram) # placeholder for now as I have not made a function that selects the level to be edited.
    gameactivityOptionSelectionEdit.grid(column=2, row=1)
    gameactivityOptionSelectionPlay = tk.Button(master=gameactivityModeSelectionFrame, text="Play", width=20, command=Quiz)
    gameactivityOptionSelectionPlay.grid(column=2, row=2)
    gameactivityOptionSelectionPlayLevel = tk.Label(master=gameactivityModeSelectionFrame, text="Level: ")
    gameactivityOptionSelectionPlayLevel.grid(column=2, row=3, sticky="W")
    gameactivityOptionSelectionStatistic = tk.Button(master=gameactivityModeSelectionFrame, text="Statistic", width=20, command=statisticsButton)
    gameactivityOptionSelectionStatistic.grid(column=2, row=4)
    ## todo: fix options

    # mainNotebook Compiling
    mainNotebook.add(TranslationPage, text='Translation')
    mainNotebook.add(gameactivityRoot, text='Game Activity')
    mainWindow.mainloop()

## mainloop
strOption = ""
CorrectAnswers = []
IncorrectAnswers = []
BTPBLS()