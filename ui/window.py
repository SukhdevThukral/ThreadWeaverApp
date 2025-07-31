import tkinter as tk
from tkinter import ttk
import os
import sys
import psutil
import threading
import time

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
root.configure(bg="#e0d8d7")
root.attributes("-alpha", 0.86)

cpu_usage = tk.Label(root, text="CPU Usage",bg="#e0d8d7",fg="#0f172a",font=("Segoe UI",40,"bold")) #bg dekhlio kya krna hai lallu
cpu_usage.pack()
icon_path = get_resource_path("assets/icon.png")
icon_img = tk.PhotoImage(file=icon_path)
root.iconphoto(False, icon_img)
root.mainloop()