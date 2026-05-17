import tkinter as tk
from tkinter import ttk

def quizInstanceUI():
    """Draws an decoding game instance"""
    def placeholder():
        pass

    window = tk.Tk()
    window.title("Game Activity")
    window.geometry("600x200")

    # Grid Geometry
    window.rowconfigure(0, weight=1)
    window.rowconfigure(1, weight=1)
    window.rowconfigure(2, weight=1)
    window.columnconfigure(0, weight=1)
    window.columnconfigure(1, weight=1)
    
    # Question
    questionInput = "01000110 00111001 10010010"
    question = tk.Label(text=questionInput, master=window, font=("Arial", 12, "bold"))
    question.grid(row=0, column=0, columnspan=2, sticky=tk.W)
    
    # Entrybox
    questionBox = tk.Entry(width=20, master=window)
    questionBox.grid(row=1, column=0, columnspan=2, sticky=tk.NSEW)

    # Buttons 
    verifyButton = tk.Button(width=20, text="Verify", master=window)
    verifyButton.grid(row=2, column=0, sticky=tk.E)
    exitButton = tk.Button(width=20, text="Exit", master=window)
    exitButton.grid(row=2, column=1, sticky=tk.W)

    window.mainloop()

def replaceUI():
    """Draws an decoding game instance"""
    def placeholder():
        pass

    window = tk.Tk()
    window.title("Game Activity")
    window.geometry("600x200")

    # Grid Geometry
    window.rowconfigure(0, weight=1)
    window.rowconfigure(1, weight=1)
    window.rowconfigure(2, weight=1)
    window.rowconfigure(3, weight=1)
    window.columnconfigure(0, weight=1)
    window.columnconfigure(1, weight=1)
    window.columnconfigure(2, weight=1)
    window.columnconfigure(3, weight=1)

    # Queries
    replace = tk.Label(text="Replace", master= window)
    current = tk.Label(text="Current:", master= window)
    new =  tk.Label(text="New:", master= window)
    replace.grid(column=0, row=0)
    current.grid(column=0, row=1)
    new.grid(column=0, row=2)

    currentEntry = tk.Entry(master=window)
    newEntry = tk.Entry(master=window)
    currentEntry.grid(column=1, row=1, columnspan=3, sticky=tk.W)
    newEntry.grid(column=1, row=2, columnspan=3, sticky=tk.W)

    # Buttons 
    cancelButton = tk.Button(width=20, text="Cancel", master=window)
    cancelButton.grid(row=3, column=0, columnspan=2, sticky=tk.E)
    replaceButton = tk.Button(width=20, text="Replace", master=window)
    replaceButton.grid(row=3, column=2, columnspan=2, sticky=tk.W)

    window.mainloop()

