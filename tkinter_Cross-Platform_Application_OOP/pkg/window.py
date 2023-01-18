# Import Python tkinter Library/Module/Framework
import tkinter as tk

# Window() Widget/Class/Window
class Window():
    
    def __init__(self):
        # Create top level window
        self.root = tk.Toplevel()

        # Other new_window widget specifications here
        self.root.title("Toplevel Window")
        self.root.geometry("400x300")