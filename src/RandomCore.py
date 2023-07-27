from random import *
from sqlite3 import *
from tkinter import *
from tkinter import ttk
import glob
import webbrowser
import json

#Open source code with MIT License.
#By Akir_ 2023.6.10

def open_site(url):
    webbrowser.open(url)




def main():
    #Connect Database
    print("Loader started.")
    database_name = glob.glob("*.db")
    print("Collected the database file:",database_name)

    conn = connect(database_name[0])
    newcursor = conn.cursor()
    print("Connected database:",database_name)
    newcursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    table_names = newcursor.fetchall()
    num_tables = len(table_names)
    table_name = ','.join(table_names[0] for table_names in table_names)



    query = "SELECT COUNT(*) FROM {}".format(table_name)
    newcursor.execute(query)
    num_entries = newcursor.fetchone()[0]

    print("The number of the entires is",num_entries)



    def randompicker(num):
        a = 1
        b = int(num)
        Targetnum = randint(a, b)
        return Targetnum

    Picked =randompicker(num_entries)

    print(Picked)

    #Search

    query2 = "SELECT Name FROM {} WHERE ID = {}".format(table_name,Picked)
    newcursor.execute(query2)
    result = newcursor.fetchone()[0]

    print("Picked:",result)

    GUI = Tk()
    GUI.title("Result")
    GUI.iconbitmap("17-logo-v2.ico")


    screen_width = GUI.winfo_screenwidth()
    screen_height = GUI.winfo_screenheight()
    window_width = 270
    window_height = 160
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2

    GUI.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    result_var = StringVar(value=str(result))

    str_databasename = database_name[0]
    #if str_databasename == "17.db":
        
    #    print("Oh, You are in class17!")

 #        if Picked == 28:
 #            Table1 = ttk.Label(GUI, textvariable=result_var, font=("KaiTi",50))
 #            Table2 = ttk.Label(GUI, text="What a coincidence!", font=("Consolas",14,"italic"))# ??
    if Picked == 1:
        Table1 = ttk.Label(GUI, textvariable=result_var, font=("KaiTi",50))
        Table2 = ttk.Label(GUI, text="?", font=("Consolas",14,"italic"))
 #        elif Picked == 52:
 #            Table1 = ttk.Label(GUI, textvariable=result_var, font=("KaiTi",50))
 #            Table2 = ttk.Label(GUI, text="Nice to see you today!", font=("Consolas",14,"italic"))
 #        elif Picked == 20:
 #           Table1 = ttk.Label(GUI, textvariable=result_var, font=("KaiTi",50))
  #          Table2 = ttk.Label(GUI, text="阳光开朗大男孩~", font=("Consolas",14,"italic"))
   #     elif Picked == 55:
    #        Table1 = ttk.Label(GUI, textvariable=result_var, font=("KaiTi",50))
    #        Table2 = ttk.Label(GUI, text="达成成就：我抽我自己！", font=("Consolas",14,"italic"))
    else:
        Table1 = ttk.Label(GUI, textvariable=result_var, font=("Microsoft YaHei",50))
        Table2 = ttk.Label(GUI, text="You are quite lucky!", font=("Microsoft YaHei",14))#一般
    #else:
    #    Table1 = ttk.Label(GUI, textvariable=result_var, font=("SimSun",50))
    #    Table2 = ttk.Label(GUI, text="You are quite lucky!", font=("Microsoft YaHei",14))

    stylebar = ttk.Style()
    stylebar.configure("NoBorder.TButton" ,  borderwidth=0, highlightthickness=0)

    Table3 = ttk.Label(GUI, text="Powered by EFC Tech , ChatGPT as well.",font=("Consolas",10,"italic"),foreground="#ffffff",background="#f5b3b4")
    Table4 = ttk.Button(GUI, text="View:https://mcmjun.github.io/ !" , command=lambda:open_site("https://mcmjun.github.io/") ,style="NoBorder.TButton" , takefocus=False)

    Table1.pack()
    Table2.pack()
    Table3.pack()
    Table4.pack()
    GUI.resizable(False,False)

    GUI.mainloop()

#Debug GUI
#I hope you will never occur these problems!

try :
    main()
except IndexError:
    DebugGUI = Tk()
    DebugGUI.title("Debug-Traceback")
    window_width = 100
    window_height = 120
    Dlable = Label(DebugGUI, text="You might forget to put your database in the dir!")
    Dlable.pack()
    DebugGUI.mainloop()
except OperationalError:
    DebugGUI = Tk()
    DebugGUI.title("Debug-Traceback")
    window_width = 100
    window_height = 120
    Dlable = Label(DebugGUI, text="SQLite Operational ERROR!")
    Dlable.pack()
    DebugGUI.mainloop()
except ValueError:
    DebugGUI = Tk()
    DebugGUI.title("Debug-Traceback")
    window_width = 100
    window_height = 120
    Dlable = Label(DebugGUI, text="Database Construction ERROR!")
    Dlable.pack()
    DebugGUI.mainloop()