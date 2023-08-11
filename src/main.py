from tkinter import *
from time import *
from tkinter import ttk
import threading
from random import *
from sqlite3 import *
import subprocess

#


def adopt():
        subprocess.run("RandomCore.exe")

def newado():
      subthr = threading.Thread(target=adopt)
      subthr.start()

#Get time (From ChatGPT)
def update_time(time_label):
    current_time = strftime("%H:%M:%S")
    time_label.config(text=current_time)
    # Schedule the next update after 1 second (1000 milliseconds)
    time_label.after(1000, update_time)



def GUIMain():
      #GUI Started
    UI = Tk()
    UI.title("NamePicker_V2")
    UI.iconbitmap("17-logo-v2.ico")
    UI.resizable(False,False)

    #Set the position of the window
    screen_width = UI.winfo_screenwidth()
    screen_height = UI.winfo_screenheight()

    window_width = 520
    window_height = 320
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2

    UI.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    #Creat frame
    frame = Frame(UI)
    frame.pack()

    Lable0 = Label(frame, text="NamePicker_V2",font=("consolas",25)).grid(column=0,row=0)

    time_label = Label(frame, text="", font=("Arial", 20))
    time_label.grid(column=0,row=1)
    update_time(time_label)

    Button1 = Button(frame ,text="TOUCH TO START",height=2,width=17,command=adopt).grid(column=0,row=2)

    UI.mainloop()

try:
      mianthr = threading.Thread(target=GUIMain)
      mianthr.start()
except ValueError as e:
      print(e)