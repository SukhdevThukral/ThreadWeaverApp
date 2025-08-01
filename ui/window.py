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

def update_stats():
    while True:
        cpu = psutil.cpu_percent(interval=1)
        ram = psutil.virtual_memory().percent
        cpu_progress["value"] = cpu        
        ram_progress["value"] = ram
        cpu_label_var.set(f"CPU Usage: {cpu}%")
        ram_label_var.set(f"RAM Usage: {ram}%")
        battery = psutil.sensors_battery()
        if battery is not None:
            battery_perc = battery.percent
            charging = "Charging" if battery.power_plugged else "Not Charging"
            battery_label_var.set(f"Battery: {battery_perc}% ({charging})")
        else:
            battery_label_var.set("Battery Not Present")

root = tk.Tk()
root.title("ThreadWeaver - Smart Task Manager")
root.geometry("600x400")
root.configure(bg="#f4f4f5")
root.attributes("-alpha", 0.94)

# cpu_usage = tk.Label(root, text="CPU Usage",bg="#e0d8d7",fg="#0f172a",font=("Segoe UI",40,"bold")) #bg dekhlio kya krna hai lallu
# cpu_usage.pack()

#heading
appTitle = tk.Label(root, text="ThreadWeaver", font=("Segoe UI",28,"bold"), bg="#f4f4f5", fg="#1e293b")
appSubtitle = tk.Label(root, text="Smart Background Task Manager", font=("Segoe UI", 14), bg="#f4f4f5", fg="#64748b")
appTitle.pack(pady=(20,0))
appSubtitle.pack(pady=(20,0))

#cpu stats
cpu_label_var = tk.StringVar()
cpu_label_var.set("CPU Usage: 0%")
cpu_label = tk.Label(root, textvariable=cpu_label_var, font=("Segoe UI", 12), bg="#f4f4f5", fg="#0f172a")
cpu_label.pack(pady=(10,0))

cpu_progress = ttk.Progressbar(root, orient="horizontal", length=400, mode="determinate")
cpu_progress.pack(pady=(5,15))

#ram stats
ram_label_var = tk.StringVar()
ram_label_var.set("RAM Usage: 0%")
ram_label = tk.Label(root, textvariable=ram_label_var, font=("Segoe UI", 12), bg="#f4f4f5", fg="#0f172a")
ram_label.pack(pady=(10,0))

ram_progress = ttk.Progressbar(root, orient="horizontal", length=400, mode="determinate")
ram_progress.pack(pady=(5,15))

#battery stats
battery_label_var = tk.StringVar()
battery_label_var.set("Battery: ...")
battery_label = tk.Label(root, textvariable=battery_label_var, font=("Segoe UI", 12), bg="#f4f4f5", fg="#0f172a")
battery_label.pack(pady=(10,0))


#bars styling
style = ttk.Style()
style.theme_use("clam")
style.configure("TProgressBar", thickness=20, troughcolor="#e2e8f0", background="#0f766e", bordercolor="#cbd5e1")

#setting icon
icon_path = get_resource_path("assets/icon.png")
icon_img = tk.PhotoImage(file=icon_path)
root.iconphoto(False, icon_img)

#bg thread for live updates
threading.Thread(target=update_stats, daemon=True).start()

root.mainloop()