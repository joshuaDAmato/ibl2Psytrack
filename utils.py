import tkinter as tk
from tkinter import filedialog

def selectFile():
    root = tk.Tk() # create a root window
    root.withdraw() # hide the root window
    filepath = filedialog.askopenfilename(title = "Select File") # get the filepath of the selected file
    return filepath # return the filepath

def selectFolder():
    root = tk.Tk() # create a root window
    root.withdraw() # hide the root window
    folderpath = filedialog.askdirectory(title = "Select Folder") # get the filepath of the selected file
    return folderpath # return the filepath

def dictprint(d):
    """
    will print the keys and paired value's type as it unpacks them.
    """
    for k in d.keys():
        print(k, type(d[k]))

def writtenInput(prompt):
    """
    will prompt the user for input via a gui window and save the input as a string.
    """
    root = tk.Tk() # create a root window
    root.withdraw() # hide the root window
    return input(prompt)