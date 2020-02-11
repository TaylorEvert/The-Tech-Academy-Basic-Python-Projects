
from tkinter import *
import tkinter as tk


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # config master frame
        self.master = master
        self.master.minsize(550,200)
        self.master.maxsize(550,200)
        

        # title and colors
        self.master.title("Check Files")
        self.master.configure(bg="#F0F0F0")

        # buttons
        self.btn_browseTop = tk.Button(self.master,width=12,height=1,text='Browse...')
        self.btn_browseTop.grid(row=0,column=0,padx=(15,0),pady=(55,0),sticky=W)
        
        self.btn_browseBottom = tk.Button(self.master,width=12,height=1,text='Browse...')
        self.btn_browseBottom.grid(row=1,column=0,padx=(15,0),pady=(5,0),sticky=W)
        
        self.btn_checkFile = tk.Button(self.master,width=12,height=2,text='Check for files...')
        self.btn_checkFile.grid(row=2,column=0,padx=(15,0),pady=(15,0),sticky=W)

        self.btn_closeProg = tk.Button(self.master,width=12,height=2,text='Close Program')
        self.btn_closeProg.grid(row=2,column=4,padx=(0,0),pady=(15,0),sticky=E)

        # text boxes
        self.txt_browseTop = tk.Entry(self.master,width=67,text='')
        self.txt_browseTop.grid(row=0,column=1,columnspan=4,padx=(10,0),pady=(55,0))

        self.txt_browseBottom = tk.Entry(self.master,width=67,text='')
        self.txt_browseBottom.grid(row=1,column=1,columnspan=4,padx=(10,0),pady=(5,0))
        

        





        

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
