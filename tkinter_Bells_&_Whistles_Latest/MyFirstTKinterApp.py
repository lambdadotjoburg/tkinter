import tkinter as tk
from tkinter import *

my_w = tk.Tk() # My widget/window

# Define Geometry of Window Widget Tk() Class/Box
my_w.minsize(800, 500) # Width/Height
my_w.maxsize(1200, 1000) # Width/Height
my_w.geometry("900x800") # Width/Height

my_w.resizable(True, True) #Width/Height

from tkinter import ttk

my_sizegrip = ttk.Sizegrip(my_w)
my_sizegrip.pack(side="right", anchor=SE)

# Import Python Operating System Module/Library
import os

# Set Icon of App
imgicon = tk.PhotoImage(file=os.path.join('assets\images\header\logo\logo.ico.png'))
my_w.tk.call('wm', 'iconphoto', my_w._w, imgicon)

# Provide a Title to your Widget Window
title = my_w.title('Lambda Desktop Software')

# Implementing the title Widget as a Label
titleLabel= tk.Label(my_w, text=title)

# Pack Title Label
titleLabel.pack()

# Create New Label
my_label = tk.Label(my_w, text="Lambda Desktop Software", font=("Courier", 14))

# Pack Title Label
my_label.pack()

# Working with file path in operating system

# Get Current Working Directory
current_working_directory = os.getcwd()

# full_path_windows = "C:\Users\Frank\Desktop\Lambda\Applciation\Desktop\Python\\Code\latest_Version\assets\images\header\logo\logo.ico.png"
full_path_windows = current_working_directory+"\\assets\images\header\logo\logo.ico.png"

# full_path_linux = "C:\Users\Frank\Desktop\Lambda\Applciation\Desktop\Python\\Code\latest_Version\assets\images\header\logo\logo.ico.png"
# Convert fullPathWindows \ to fullPathPython /
full_path_linux = full_path_windows.replace("\\", "/")

# Create a Label Widget
my_label_1 = tk.Label(my_w, text=full_path_windows)
my_label_2 = tk.Label(my_w, text=full_path_linux)

# Define the "New Line" Widget
new_line = tk.Label(my_w, text="\n\r")

# Use New Line Widget
new_line.pack()

# Display the Label Widget on the root Window
my_label_1.pack()

# Use New Line Widget
new_line.pack()

# Display the Label Widget on the root Window
my_label_2.pack()

new_line.pack()

# Import functions which contain the commands for each menu item as well as all buttons functions etc.
from my_functions import *

# Instatiate menubar Wdiget/Class and wpecify parent frame/window/widget, in this case my_w which is a Tk() class/widget
menubar = tk.Menu(my_w)

menu_file = tk.Menu(menubar, tearoff=0, title="File")
menu_edit = tk.Menu(menubar, tearoff=0, title="Edit")
menu_radio = tk.Menu(menubar, tearoff=0, title="Radio")
menu_check = tk.Menu(menubar, tearoff=0, title="Check")

menubar.add_cascade(label="File", menu=menu_file)
menubar.add_cascade(label="Edit", menu=menu_edit)
menubar.add_cascade(label="Radio", menu=menu_radio)
menubar.add_cascade(label="Check", menu=menu_check)

# Cascade for File
menu_file.add_command(label="New", command=new_doc())
menu_file.add_command(label="Open ..", command=open_doc())

# Add a Separator in File Menu Tab
menu_file.add_separator()
# menu_file.insert_separator(3)

menu_file.add_command(label="Save", command=save_doc())
menu_file.add_command(label="Save As ..", command=save_doc_as())

# Add a Separator in File Menu Tab
menu_file.add_separator()
# menu_file.insert_separator(5)

menu_file.add_command(label="Exit", command=my_w.quit)

# Cascade for Edit
menu_edit.add_command(label="Undo", command=undo_last_step())
menu_edit.add_command(label="Redo", command=redo_last_step())

# Instantiate variable for radio buttons
optvar = tk.StringVar()

# Radio Menu Buttons
menu_radio.add_radiobutton(label="Radio 0", value=0)
menu_radio.add_radiobutton(label="Radio 1", value=1)
menu_radio.add_radiobutton(label="Radio 2", value=2)

# Instantiating variables for check buttons
chkopt0 = tk.StringVar()
chkopt1 = tk.StringVar()
chkopt2 = tk.StringVar()

# Check Menu Buttons
menu_check.add_checkbutton(label="Check 0", onvalue=1, offvalue=0, variable=chkopt0)
menu_check.add_checkbutton(label="Check 1", onvalue=1, offvalue=0, variable=chkopt1)
menu_check.add_checkbutton(label="Check 2", onvalue=1, offvalue=0, variable=chkopt2)

# New Code

# configure menu bar to be attached to my window widget
my_w.config(menu=menubar)

# Main Loop, keep my window active, unless quit ...
my_w.mainloop()