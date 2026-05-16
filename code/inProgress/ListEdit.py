import tkinter as tk
from tkinter import ttk as ttk
import pandas as pan

# Testing Variables here
testvariable = ["art", "two", "son", "pie", "law",
                "sir", "way", "map", "mom", "mud", 
                "tea", "dad", "hat", "lab", "ear",
                "fun", "cut", "fax", "pan", "owe"]

# functions here
def placeholder():
    print("placeholder() Called.")
    pass

# window
window = tk.Tk()
window.title = "Edit"

# Three frames:
## listbox
wordFrame = ttk.Frame(master=window)
wordFrame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

## query
queryFrame = ttk.Frame(master=window)
queryFrame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

buttonAccess = ttk.Frame()
buttonAccess.rowconfigure(0, weight=1)
buttonAccess.columnconfigure(0, weight=1)
buttonAccess.columnconfigure(1, weight=1)
buttonAccess.columnconfigure(2, weight=1)
buttonAccess.columnconfigure(3, weight=1)
buttonAccess.pack()

# scrollbar
wordFrameScrollbar = ttk.Scrollbar(wordFrame)
wordFrameScrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# listbox
editListbox = tk.Listbox(width = 12, selectmode=tk.MULTIPLE, master= wordFrame,
                         font=("Arial", 20))
editListbox.pack()

for i in range(len(testvariable)):
    editListbox.insert(i, testvariable[i])

editListbox.config(height= editListbox.size())

# Entrybox
entryboxLabel = tk.Label(master=queryFrame, text="Add Entry:", font=("Arial", 10))
entryboxLabel.pack(side = tk.LEFT)
editEntrybox = tk.Entry(master=queryFrame)
editEntrybox.pack(side = tk.RIGHT)

# buttonAccess
addButton = tk.Button(text="Add", command=placeholder, master= buttonAccess)
addButton.grid(row=0, column=0)

deleteButton = tk.Button(text="Delete", command=placeholder, master= buttonAccess)
deleteButton.grid(row=0, column=1)

saveButton = tk.Button(text="Save", command=placeholder, master= buttonAccess)
saveButton.grid(row=0, column=2)

# wordFrame Scrollbar Access
editListbox['yscrollcommand']=wordFrameScrollbar.set
wordFrameScrollbar.config(command=editListbox.yview)

# mainloop()
window.mainloop()