
from tkinter import *
from tkinter import filedialog
import tkinter as tk
import glob
import os
import shutil
import sqlite3


fileList = []
destination = []
files = []


def btn_source(): # ask for file source, print to corresponding entry
    source_path = filedialog.askdirectory()
    new_text = source_path
    source_text.set(new_text)
    for filename in os.listdir(source_path):
        if filename.endswith(".txt"):
            files.append(filename)
            updated_text = "{}/".format(new_text)
            fullPath = os.path.join(updated_text,filename)
            fileList.append(fullPath)
    
            

def btn_destination(): # ask file destination, print to corresponding entry
    destination_path = filedialog.askdirectory()
    new_text = destination_path
    destination_text.set(new_text)
    destination.append(new_text)
    

def btn_move():
    for file in fileList:
        
        for path in destination:
            moveSource = file
            moveDestination = path
            shutil.move(moveSource,moveDestination)

    dbNameTime()
        
        
def dbNameTime():
    conn = sqlite3.connect('dbMoveDir.db')

    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_Files(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_FileName TEXT, \
        col_FileTime TEXT \
        )")
        conn.commit()
    cur.close()
    conn.close()
        
    for file in files:
        fileName = file
        dstPath = destination[0]
        fullPath =  os.path.join(dstPath,fileName)
        fileTime = os.path.getmtime(fullPath)
        print("File Name: {} , File Time: {}".format(fileName,fileTime))
        conn = sqlite3.connect('dbMoveDir.db')
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_Files(col_FileName,col_FileTime) VALUES (?,?)", \
                        (fileName,fileTime,))
            conn.commit()
        cur.close()
        conn.close()       
           

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # define master frame config (H,W)
        self.master = master
        self.master.minsize(500,300)
        self.master.maxsize(500,300)

        # title and colors
        self.master.title("Move Files")
        self.master.configure(bg="#F0F0F0")

        # buttons
        self.btn_source = tk.Button(self.master,width=15,text='Browse Source',command=lambda: btn_source())
        self.btn_source.grid(row=0,column=0,padx=(5,10),pady=(10,10),sticky=W)

        self.btn_destination = tk.Button(self.master,width=15,text='Browse Destination',command=lambda: btn_destination())
        self.btn_destination.grid(row=1,column=0,padx=(5,10),pady=(10,10),sticky=W)

        self.btn_mover = tk.Button(self.master,width=15,text='Move Files',command=lambda: btn_move())
        self.btn_mover.grid(row=2,column=0,padx=(5,10),pady=(10,10),sticky=W)

        # text boxes
        self.txt_source = tk.Entry(self.master,width=60,textvariable=source_text)
        self.txt_source.grid(row=0,column=1,padx=(0,10),pady=(10,10))

        self.txt_destination = tk.Entry(self.master,width=60,textvariable=destination_text)
        self.txt_destination.grid(row=1,column=1,padx=(0,10),pady=(10,10))
        
        
if __name__ == "__main__":
    root = tk.Tk()
    source_text = StringVar()
    destination_text = StringVar()
    App = ParentWindow(root)
    root.mainloop()
