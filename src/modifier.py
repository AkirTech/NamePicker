from tkinter import *
import sqlite3 as sql
import glob
import os
from tkinter import ttk
import time

#Data operation
def main_DEL():
    #Connect Database
    print("Loader started.")
    database_name = glob.glob("*.db")
    print("Collected the database file:",database_name)

    conn = sql.connect(database_name[0])
    newcursor = conn.cursor()
    print("Connected database:",database_name)
    newcursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    table_names = newcursor.fetchall()
    num_tables = len(table_names)
    table_name = ','.join(table_names[0] for table_names in table_names)
    if num_tables > 1 :
        print("You may have more than one table in your database!")
        quit()
    elif num_tables == 0:
        print("There's no table in the database.\nPlease check!")
    else :
        print("Finished to load the table.",table_name)



    query = "SELECT COUNT(*) FROM {}".format(table_name)
    newcursor.execute(query)
    num_entries = newcursor.fetchone()[0]

    print("The number of the entires is",num_entries)

    try:
        innum = int(inbox_init.get())
        # Verify row existence using the ID column
        find = "SELECT CODE FROM {} WHERE ID = {}".format(table_name,innum)
        newcursor.execute(find)
        row = newcursor.fetchone()

        if not row:
            print(f"No row found in table '{table_name}' with ID = {innum}.")
            err2 = Label(Window , text=f"No such object!" , font=("SimSun", 10),width=40).grid(row=4,column=1)
            return None

        Code = row[0]
        print(Code)
        inpass = str(password_init.get())
        print(inpass)
        #Nameselect
        namesel = "SELECT NAME FROM {} WHERE ID = {}".format(table_name,innum)
        newcursor.execute(namesel)
        namegot = newcursor.fetchone()[0]
        print("Name picked",namegot)

        if inpass == Code:
            query2 = "DELETE FROM {} WHERE ID = {}".format(table_name,innum)
            newcursor.execute(query2)
            conn.commit()
            success = Label(Window , text="Successfully deleted {}".format(namegot) , font=("SimSun", 10),width=40).grid(row=4,column=1)
        else:
            err = Label(Window , text="Wrong Password" , font=("SimSun", 10),width=40).grid(row=4,column=1)

    except Exception as e:
        print(f"Error occurred: {e}")
        return None
    


    #query2 = "DELETE FROM {} WHERE ID = {}".format(table_name,inbox_init)
    #newcursor.execute(query2)




#GUI_Construction
Window = Tk()
Window.title("Modifier")
Window.iconbitmap("17-logo-v2.ico")
mainframe = Frame(Window)
Window.resizable(False,False)

screen_width = Window.winfo_screenwidth()
screen_height = Window.winfo_screenheight()
window_width = 400
window_height = 150
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2
X_MOVE = screen_width // 6
Y_MOVE = screen_height // 10

Window.geometry(f"{window_width}x{window_height}+{x_position - X_MOVE}+{y_position - Y_MOVE}")

tip = Label(Window , text="NamePicker-Modifier." , font=("SimSun", 17),width=25).grid(row=0,column=1)


in_tip = Label(Window,text="Number",font=("SimSun", 10)).grid(row=1,column=0)
inbox_init = StringVar()
inbox_init.set("")
inbox = Entry(Window , textvariable=inbox_init, width=20).grid(column=1 , row=1)
pass_tip = Label(Window,text="Password",font=("SimSun", 10)).grid(row=2,column=0)
password_init = StringVar()
password_init.set("")
password = Entry(Window ,textvariable=password_init , width = 20).grid(column=1 , row=2)
btn = Button(Window , text="Delete" , command=main_DEL).grid(row=3,column=1)


Window.mainloop()