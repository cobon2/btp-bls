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
placeholderTranslationPage = ttk.Frame(mainNotebook, width=1200, height = 1120) # Placeholder
placeholderTranslationPage.pack(fill='both', expand=True)

#####################################################################################################
# Page 2: Game Activity

#####################################################################################################
# Page 3: Chart
placeholderChartPage = ttk.Frame(mainNotebook, width=1200, height = 1120) # Placeholder
placeholderChartPage.pack(fill='both', expand=True)

#####################################################################################################
# mainNotebook Compiling
mainNotebook.add(placeholderTranslationPage, text='translation')
mainNotebook.add(placeholderChartPage, text='translation')

#####################################################################################################
# Mainloop
mainWindow.mainloop()