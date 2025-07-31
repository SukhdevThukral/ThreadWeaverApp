import tkinter as tk
import os
import sys

def get_resource_path(relative_path):
    """ Get absolute path to resource (compatible with PyInstaller) """
    try:
        base_path = sys._MEIPASS 
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


root = tk.Tk()
root.title("ThreadWeaver - Smart Task Manager")
root.geometry("600x400")

icon_path = get_resource_path("assets/icon.png")
icon_img = tk.PhotoImage(file=icon_path)
root.iconphoto(False, icon_img)


root.mainloop()
