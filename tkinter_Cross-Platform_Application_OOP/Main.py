############################################################################################
########################### Import Classes/Modules/Frameworks ##############################
############################################################################################

from pkg.window import *
from pkg.modules import *

############################################################################################
########################### Define all Classes/Properties/Methods ##########################
############################################################################################

# Main() Class/Widget/Window
class Main(tk.Tk): # The Main() class/window/widget inherits properties and methods from the tk.Tk() class/widget by extending to it Main(tk.Tk)
    
    def __init__(self):

        # Define root for Main class/window/widget
        self.root = tk.Tk()

        # Other Main() widget/class/window specifications here
        self.root.title("Main Window")
        self.root.geometry("700x600")
        self.root.minsize(800, 500) # Width/Height
        # my_w.maxsize(1200, 1000) # Width/Height
        self.root.resizable(True, True) #Width/Height

        # Sizegrip
        my_sizegrip = ttk.Sizegrip(self.root)
        my_sizegrip.pack(side="right", anchor="se")

        # Make widget/window resizable
        self.root.resizable(True, True) #Width/Height
        
        # Create New Label
        tk.Label(self.root, text="Lambda Desktop Software", font=("Courier", 14)).pack(pady=30)

        # set icon of main/all window(s)/widget(s)
        icon_path = tk.PhotoImage(file = "assets\images\header\logo\logo.ico.png") # set the icon path by joining the current directoy to the subfolder containing the icon
        self.root.iconphoto(True, icon_path) # "True" specifies that all top-level windows/widgets should have the same icon as the tk.Tk() root/main window/wigdet

        # Working with file path in operating system
        # Get Current Working Directory
        current_working_directory = os.getcwd()

        # full_path_windows = "C:\Users\Frank\Desktop\Lambda\Applciation\Desktop\Python\\Code\latest_Version\assets\images\header\logo\logo.ico.png"
        full_path_windows = current_working_directory+"\\assets\images\header\logo\logo.ico.png"

        # full_path_linux = "C:\Users\Frank\Desktop\Lambda\Applciation\Desktop\Python\\Code\latest_Version\assets\images\header\logo\logo.ico.png"
        full_path_linux = full_path_windows.replace("\\", "/") # Convert fullPathWindows \ to fullPathPython /

        # Create & Pack/Place/Grid a Label Widget
        tk.Label(self.root, text=full_path_windows).pack(pady=10)
       
        # Create & Pack/Place/Grid a Label Widget
        tk.Label(self.root, text=full_path_linux).pack(pady=10)

        # Define the "New Line" Widget
        new_line = tk.Label(self.root, text="\n\r")

        # Use New Line Widget
        new_line.pack()

        # Instatiate menubar Widget/Class and specify parent widget/class/frame/window, in this case self.root

        # Menu stuff for this particular class/widget
        menubar = tk.Menu(self.root)

        menu_file = tk.Menu(menubar, tearoff=0)
        menu_edit = tk.Menu(menubar, tearoff=0)

        menubar.add_cascade(label="File", menu=menu_file)
        menubar.add_cascade(label="Edit", menu=menu_edit)    

        menu_file.add_command(label="New", command=new_doc) # referring to my_function inside of the my_functions.py file/module
        menu_file.add_command(label="Open ..", command=open_doc) # referring to my_function inside of the my_functions.py file/module
        menu_file.add_command(label="Save", command=save_doc_as) # referring to my_function inside of the my_functions.py file/module
        menu_file.add_command(label="Save As ..", command=save_doc_as) # referring to my_function inside of the my_functions.py file/module
        
        menu_edit.add_command(label="Undo", command=undo_last_step) # referring to my_function inside of the my_functions.py file/module
        menu_edit.add_command(label="Redo", command=redo_last_step) # referring to my_function inside of the my_functions.py file/module

        self.root.config(menu=menubar)

        ############################################################################################
        ########################### Working with Classes/Properties/Methods ########################
        ############################################################################################

        # Run new window defined by method inside this class on start-up
        # This illustrates how to call a method of a class inside of another method within the same class
        # We can also see here that the main window and the toplevel window has the same icon
        # self.new_window()

        # Open a new window defined by a class
        # This illustrates how to call a method of a class inside of another method within a different class
        # window = Window()

        # We can manipulate widget/window instantiated by the Window() class
        # window.root.geometry("600x500") # This line overwrites the geometry of instance window = Window()

        # Call the mainloop() method from the tk.Tk class on the Main() class
        self.root.mainloop()

############################################################################################
################ Instantiate the Main() class and call mainloop() method ###################
############################################################################################

# Run the program whenever super-global variable __name__ matches __main__
if __name__ == '__main__':
    # instantiate the Main() class to run the program
    main = Main()

############################################################################################
###################################### End of App ##########################################
############################################################################################

############################################################################################
###################################### Discussion ##########################################
############################################################################################

# "self" is a class-level identifier.

# Whenever you type self.root = tk.Tk()
# it means that in this/self-referential
# class will create a class-level variable
# called root and initialize it with tk.Tk() object.

# Whenever you want to access this variable in the class
# you will call it with self.root

# For example self.root.title()

# Example 1

# Example 2

# Example 3

# Example 4

# .
# .
# .