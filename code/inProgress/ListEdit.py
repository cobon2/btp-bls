import tkinter as tk
from tkinter import ttk as ttk
import pandas as pan


# Testing Variables here
testvariable = ["art", "two", "son", "pie", "law",
                "sir", "way", "map", "mom", "mud", 
                "tea", "dad", "hat", "lab", "ear",
                "fun", "cut", "fax", "pan", "owe"]

print(str(testvariable))

# functions here
def placeholder():
    print("placeholder() Called.")
    pass

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

for i in range(len(testvariable)):
    editListbox.insert(i, testvariable[i])

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

# tasks:
# Front-End: Done!
# Back-End (functionality): WIP