from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
import tkinter
from tkinter import filedialog

import re
import json
import os

# ask for directory to list
Tk().withdraw() 
rootdir = filedialog.askdirectory(title="Select Parent Folder") 

lst = []

# rootdir = 'I:\_Customers'
for file in os.listdir(rootdir):
    lst.append(file)
    print(file)

# where to stor the txt file
Tk().withdraw() 
saveDir = filedialog.askdirectory(title="Choose Location for Directories.txt") 

print(saveDir)

newFile = saveDir + '/Directories.txt'
print(newFile)

with open(newFile, "w") as txt_file:
    for loc in lst:
        txt_file.write(loc + '\n')
