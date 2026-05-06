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

#####################################################################################################
# Page 1: Translation Page

#####################################################################################################
# Page 2: Game Activity

#####################################################################################################
# Page 3: Chart

#####################################################################################################
# mainNotebook Compiling

#####################################################################################################
# Mainloop
mainWindow.mainloop()