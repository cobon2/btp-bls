import tkinter as tk        # we cant use `*` as it is not recomended due to the posiblity of library conflicts.
from tkinter import ttk     # Extra Features of tkinter
import os                   # file handling


# functions here

#####################################################################################################
# file handling
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

def buttonPlaceholder():
    pass

#####################################################################################################
# window(root) settings
mainWindow = tk.Tk()
mainWindow.title("BTP-BLS")
mainWindow.geometry("600x400")
logo = tk.PhotoImage(file = logoFileNameConstant())
mainWindow.iconphoto(True, logo)

## notebook declaration
mainNotebook = ttk.Notebook(mainWindow)
mainNotebook.pack(expand=True)

#####################################################################################################
# Page 1: Translation Page
placeholderTranslationPage = ttk.Frame(mainNotebook) # Placeholder
placeholderTranslationPage['padding'] = 10
placeholderTranslationPage.pack(fill='both', expand=True)

#####################################################################################################
# Page 2: Game Activity
gameactivityRoot = ttk.Frame(mainNotebook)
## (...) Note to self: main - pertains to the main 'main' and;
##                     root - pertains to the mode's parent or
##                            main.

## cell config
# todo: move this on another file
# todo: config this
qtyRow = 9
qtyColumn = 3
for i in range(qtyRow):        # setting the cell rows
    gameactivityRoot.rowconfigure(i, weight=1)

for i in range(qtyColumn):     # setting the cell colums
    gameactivityRoot.columnconfigure(i, weight=1)

# cell filling

## Level title
gameactivityLevelTitle = tk.Label(gameactivityRoot, text='Levels:', font=('Arial', 20, 'bold'))
gameactivityLevelTitle.grid(column=0, row=0, sticky=tk.SW)

## Level Selection
placeholderLevels = ["Level 1","Level 2","Level 3",
                     "Level 4","Level 5","Level 6",
                     "Level 7","Level 8","Level 9"]
gameactivityLevelSelection = tk.Listbox(gameactivityRoot,listvariable= tk.Variable(value = placeholderLevels), height=20, width= 1)
gameactivityLevelSelection.grid(column=0, row=1, rowspan=6, sticky="nsew")

## Win/lose Stat
gameactivityWinLoseTitle = tk.Label(gameactivityRoot, text='Win/Lose', font=("Arial", 20, "bold"))
gameactivityWinLoseTitle.grid(column=1, row=0, sticky= tk.SW)

## Win/lose Image
gameactivityWinLosePlaceholderPhotoImage = tk.PhotoImage(file = imageFileNameConstant("PlaceholderStatistic.png"))
gameactivityWinLosePlaceholderImage = tk.Label(gameactivityRoot, image= gameactivityWinLosePlaceholderPhotoImage)
gameactivityWinLosePlaceholderImage.grid(column=1, row = 1, columnspan= 2, sticky=tk.NW)

## Mode
gameactivityModeSelectionTitle = tk.Label(gameactivityRoot, text = "Mode: ", font=('Arial', 20, 'bold'))
gameactivityModeSelectionTitle.grid(column=1, row = 2, sticky=tk.NW)
listModeOptions = ["OCT to ASCII", "ASCII to OCT", "Binary To ASCII", "ASCII to Binary", "Binary to OCT", "OCT to Binary"]
for i in range(len(listModeOptions)):
    gameactivityModeOptions = tk.Radiobutton(gameactivityRoot, text=listModeOptions[i], value=listModeOptions[i]) #todo: add variable argument here
    gameactivityModeOptions.grid(column=1, row = i+3,sticky= tk.NW)

## Buttons
gameactivityPlayButton = tk.Button(text= 'Play', master= gameactivityRoot, width= 10, command= buttonPlaceholder)
gameactivityPlayButton.grid(column=2, row=3, sticky= tk.NW)
gameactivityEditButton = tk.Button(text= 'Edit', master= gameactivityRoot, width= 10, command= buttonPlaceholder)
gameactivityEditButton.grid(column=2, row=4, sticky= tk.NW)

## Minor Player Milestones
gameactivityMilestoneWins = tk.Label(text="Wins:", font = ("Arial", 12), master= gameactivityRoot)
gameactivityMilestonePlays = tk.Label(text="Plays:", font = ("Arial", 12), master= gameactivityRoot)
gameactivityMilestoneWins.grid(column=2, row=5, sticky= tk.NW)
gameactivityMilestonePlays.grid(column=2, row=6, sticky= tk.NW)

#####################################################################################################
# Page 3: Chart
placeholderChartPage = ttk.Frame(mainNotebook, width=1200, height = 1120) # Placeholder
placeholderChartPage['padding'] = (10, 10, 10, 10)
placeholderChartPage.pack(fill='both', expand=True)

#####################################################################################################
# mainNotebook Compiling
mainNotebook.add(placeholderTranslationPage, text='translation')
mainNotebook.add(gameactivityRoot, text='Game Activity')
mainNotebook.add(placeholderChartPage, text='chart')

#####################################################################################################
# Mainloop
mainWindow.mainloop()