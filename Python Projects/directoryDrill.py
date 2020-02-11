
from tkinter import *
from tkinter import filedialog
import tkinter as tk


def btn_browse():
    global file_path
    file_name = filedialog.askdirectory()
    file_path.set(file_name)


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        
        # define master frame config (H,W)
        self.master = master
        self.master.minsize(500,300)
        self.master.maxsize(500,300)

        # title and colors
        self.master.title("Directory Drill")
        self.master.configure(bg="#F0F0F0")

        # buttons - open browser directory after click 
        self.btn_browse = tk.Button(self.master,width=20,text='Browse...',command=lambda: btn_browse()) 
        self.btn_browse.grid(row=0,column=0,padx=(10,10),pady=(20,10),sticky=W)

        # text boxes - after 'select folder' print file path to entry
        self.txt_browse = tk.Entry(self.master,width=80,textvariable=file_path) 
        self.txt_browse.grid(row=1,column=0,padx=(5,10),pady=(10,10),sticky=W)
    

if __name__ == "__main__":
    root = tk.Tk()
    file_path = StringVar()
    App = ParentWindow(root)
    root.mainloop()
