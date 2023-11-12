from random import *
from sqlite3 import *
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import glob
import webbrowser
import configparser as cp
import datetime


# Open source code with GNU GPL-v3 License.
# By Akir_ 2023.10.29

def open_site(url):
    webbrowser.open(url)


# Construction Class
# class ClickableLable(Label,Button):
#    def __init__(self) -> None:
#        ttk.Label.register()
#        pass
#    def __main__(self):
#        ttk.Button.register()

class ClickableLabel(ttk.Label):
    def __init__(self, master, text, callback, *args, **kwargs):
        ttk.Label.__init__(self, master, text=text, *args, **kwargs)
        self.callback = callback
        self.bind("<Button-1>", self.on_click)

    def on_click(self):
        if self.callback:
            self.callback()


# By ChatGPT

cf = cp.ConfigParser()
cf.read("config.ini")
statu = str(cf.get("CoreMode", "mode"))
print("Current statu:", statu)


def main():
    def pick():
        # Connect Database
        print("Loader started.")
        database_name = glob.glob("*.db")
        print("Collected the database file:", database_name)

        conn = connect(database_name[0])
        newcursor = conn.cursor()
        print("Connected database:", database_name)
        newcursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        table_names = newcursor.fetchall()
        table_name = ','.join(table_names[0] for table_names in table_names)
        print("The table name is :", table_name)

        query = "SELECT COUNT(*) FROM {}".format(table_name)
        newcursor.execute(query)
        num_entries = newcursor.fetchone()[0]

        print("The number of the entires is", num_entries)

        def randompicker(num):
            a = 1
            b = int(num)
            targetnum = randint(a, b)
            return targetnum

        def randommethod2():
            time = datetime.datetime.now()
            time2 = str(time)
            time3 = time2[-9:-7]
            if time3.startswith("0"):
                result = time3[1]
            else:
                result = time3
            return int(result)

        def randommethod3():
            global state
            count = 0
            state = str()
            while count <= 30:

                if state[-1:] == "6":
                    state = state + "1"
                else:
                    state = state + str(randint(0, 6))
                count = count + 1

            print(state)

            sel_start = int(randint(1, 30))
            sel_end = sel_start + 2

            print(state[sel_start:sel_end])

            revalue = int(state[sel_start:sel_end])

            if state[sel_start:sel_end] == "00" or state[sel_start:sel_end] == "0":
                revalue = int("1")

            return revalue

        global Picked
        if statu == "buildin":
            Picked = randompicker(num_entries)
        elif statu == "time":
            Picked = randommethod2()
        elif statu == "glass":
            Picked = randommethod3()

        print(Picked)

        # Search

        query2 = "SELECT Name FROM {} WHERE ID = {}".format(table_name, Picked)
        newcursor.execute(query2)
        result = newcursor.fetchone()[0]

        print("Picked:", result)
        return result

    def update():
        global newlypicked
        newlypicked = StringVar(value=str(pick()))
        Table1.config(textvariable=newlypicked, font=("Microsoft YaHei", 50))
        Table1.pack()

    GUI = Tk()
    GUI.title("Result")
    GUI.iconbitmap("logo-v3.ico")

    screen_width = GUI.winfo_screenwidth()
    screen_height = GUI.winfo_screenheight()
    window_width = 270
    window_height = 180
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2

    GUI.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    result_var = StringVar(value=str(pick()))

    Table1 = ttk.Label(GUI, textvariable=result_var, font=("Microsoft YaHei", 50))
    Table2 = ttk.Label(GUI, text="You are quite lucky!", font=("Microsoft YaHei", 14))  # 一般

    Table3 = ClickableLabel(GUI, text="Powered by EFC Tech , ChatGPT as well.",
                            callback=lambda: open_site("https://akirtech.github.io/"), font=("Consolas", 10, "italic"),
                            foreground="#ffffff", background="#38b48b")
    # Table4 = ClickableLabel(GUI, text="View:https://akirtech.github.io/ !" ,callback=lambda:open_site("https://akirtech.github.io/"), takefocus=False)

    redostyle = ttk.Style()
    redostyle.configure("Transparent.TButton", padding=0, relief="flat", background="SystemTransparent")
    redobutton = ttk.Button(GUI, text="Try again", command=update)

    Table1.pack()
    Table2.pack()
    Table3.pack()
    # Table4.pack()
    redobutton.pack()
    GUI.resizable(False, False)

    GUI.mainloop()


# Debug GUI
# I hope you will never occur these problems!

try:
    main()
except IndexError:
    Dmsgbox = messagebox.showerror(title="DebugInfo", message="You might forget to put your database in the dir!")
except OperationalError:
    Dmsgbox = messagebox.showerror(title="DebugInfo", message="SQLite Operational ERROR!")
except ValueError:
    Dmsgbox = messagebox.showerror(title="DebugInfo", message="Database Construction ERROR!")
except TypeError:
    Dmsgbox = messagebox.showerror(title="DebugInfo", message="Object Not Found!")
