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
    logoPath = os.path.join(mainDirectory, "..", "testLevel", fileName)
    filenameConstant = os.path.normpath(logoPath)
    return filenameConstant

def readExcel(filename):
    """reads the Excel file into a DataFrame (modified)"""
    print("[readExcel] - Argument Recieved.")
    output = pan.read_excel(io=excelFileNameConstant("Levels.xlsx"), sheet_name = filename, index_col=[0])
    print("[readExcel] - Output returned")
    return output

def omniEncoder(listLevelinput, output):
    "Converts the string (ASCII) elements into the desired code."
    # must encode sting to binary, ascii, and hex
    # codes in respective order:
    # hexadecimal = hex
    # binary = bin
    # decimal = ord
    originalList = listLevelinput
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
    elif output == "original":
        return originalList 
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
    # local Functions:
    def funcDelete():
        """Deletes the entry"""
        quizEntrybox.delete(0, tk.END)

    def gugugaga():
        """placeholder"""
        pass
    
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
        ## scrubbing
        userAnswers[page] = quizEntrybox.get()
        quizWindow.destroy()
        def check(userAnswers, answerSheet):
            """checks the user's questions"""
            output = []
            for i in range(len(userAnswers)):
                if userAnswers[i] == answerSheet[i]:
                    output.append("Correct")
                else:
                    output.append("Incorrect")
            return output
        
        def qtyCorrect(iterable):
            """Counts the correct user answers"""
            count = 0
            for i in iterable:
                if i == "Correct":
                    count =+ 1
                else:
                    continue
        
        functionEvaluation = check(userAnswers, quizAnswerList)
        CorrectAnswers = qtyCorrect(functionEvaluation)                                   # comment

        # UI
        submitWindow = tk.Tk()
        submitWindow.title("Results")
        submitWindow.geometry("480x600")
        #logo = tk.PhotoImage(file = logoFileNameConstant())
        #submitWindow.iconphoto(True, logo)
        submitWindowFrame = tk.Frame()
        submitWindowFrame.pack()
        
        submitWindowFrame.columnconfigure(0, weight=1)
        submitWindowFrame.columnconfigure(1, weight=1)
        submitWindowFrame.columnconfigure(2, weight=1)
        submitWindowFrame.columnconfigure(3, weight=1)
        submitWindowFrame.rowconfigure(0, weight=1)
        for i in range(len(userAnswers)):
            submitWindowFrame.rowconfigure(i+1, weight=1)

        
        
        submitWindowTitle1 = tk.Label(master=submitWindowFrame, text="Questions",
                                     font=("Arial", 12, "bold"))
        submitWindowTitle1.grid(row=0, column=0, sticky="W")
        submitWindowTitle2 = tk.Label(master=submitWindowFrame, text="Your Answer",
                                     font=("Arial", 12, "bold"))
        submitWindowTitle2.grid(row=0, column=1, sticky="W")
        submitWindowTitle3 = tk.Label(master=submitWindowFrame, text="Answer",
                                     font=("Arial", 12, "bold"))
        submitWindowTitle3.grid(row=0, column=2, sticky="W")
        submitWindowTitle3 = tk.Label(master=submitWindowFrame, text="Remarks",
                                     font=("Arial", 12, "bold"))
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
    baseList = randomSelection(extractDataFrames(readExcel("Levels.xlsx"), strLevel), quizItems)
    inputBaseList1 = baseList.copy()
    inputBaseList2 = baseList.copy()
    quizQuestionList = omniEncoder(inputBaseList1, strQuestionMode)
    quizAnswerList = omniEncoder(inputBaseList2, strAnswerMode)
    
    page = 0

    # UI
    quizWindow = tk.Tk()
    quizWindow.title("Game Activity")
    quizWindow.geometry("600x120")
    #logo = tk.PhotoImage(file = logoFileNameConstant())
    #quizWindow.iconphoto(True, logo)
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

Quiz("Level 1", "Binary To ASCII")


    

# ...