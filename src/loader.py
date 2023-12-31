import pygame as pg
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import time
import subprocess
import configparser

cf = configparser.ConfigParser()
cf.read("config.ini")
secname = cf.sections()[1]

cond = str(cf.get(secname,"condition"))
print(cond)
if cond == "OOBE" or cond == "oobe":
    
    # Play Sound Function
    def play_sound():
        pg.mixer.init()
        pg.mixer.music.load(R"res\title.mp3")
        pg.mixer.music.set_volume(0.3)
        pg.mixer.music.play(-1)

    # Progress Bar Function
    def start_progress():
        title_progressbar.start(1)  # Start the progress bar

        for i in range(10):
            time.sleep(1)
            title_progressbar.step(9)
            UI.update()

        title_progressbar.stop()
        title_progressbar.destroy()
        UI.title("NamePicker-V2.3-Ready")

        play_sound()  # Call the play_sound() function after the progress bar completes



    # Function to start the main application
    def start_main():
        # Call the main.py using subprocess
        pg.mixer.music.stop()
        UI.destroy()
        subprocess.run("main.exe")
    
    cf.read("config.ini")
    cf.set("Boot","condition","old")
    cf.write(open("config.ini","w+"))

    # GUI Construction
    UI = Tk()
    UI.title("NamePicker-V2.3-Loading...")
    UI.iconbitmap("17-logo-v2.ico")
    UI.resizable(False,False)

    # Set the position of the window
    screen_width = UI.winfo_screenwidth()
    screen_height = UI.winfo_screenheight()

    window_width = 520
    window_height = 330
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2

    UI.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    image_path = "res/NamePicker_2.3_Stable_icon.jpg"
    image = Image.open(image_path)
    image = image.resize((520, int(520 * 1100 / image.width)))
    photo_image = ImageTk.PhotoImage(image)
    title_ico = ttk.Label(UI, image=photo_image)
    title_ico.grid(column=0, row=1)

    style = ttk.Style()
    style.theme_use('clam')  # Use the default theme for the style

    # Set the color for the progress bar
    style.configure("Custom.Horizontal.TProgressbar", troughcolor='#ffffff', background='#4e5b64', thickness=10)


    title_progressbar = ttk.Progressbar(UI, style="Custom.Horizontal.TProgressbar",mode="determinate", orient="horizontal", length=520)
    title_progressbar.grid(column=0, row=5)

    start_progress()

    # Create a button to start the main application
    start_button = ttk.Button(UI, text="Start",command=start_main)
    start_button.grid(column=0, row=6)
    pg.init()
    pg.mouse.set_system_cursor(pg.SYSTEM_CURSOR_CROSSHAIR)

    UI.mainloop()
elif cond == "old" or cond == "OLD":
    subprocess.run("RandomCore.exe")