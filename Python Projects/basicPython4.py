# How to open, edit, and read text documents from pythom

import os


def writeData():
    data = '\nHello World!'
    with open('pythonTEST.txt','a') as  f:
        f.write(data)
        f.close()

def openFile():
    with open('pythonTEST.txt','r') as f:
        data = f.read()
        print(data)
        f.close()

if __name__ == "__main__":
    writeData()
    openFile()
    
