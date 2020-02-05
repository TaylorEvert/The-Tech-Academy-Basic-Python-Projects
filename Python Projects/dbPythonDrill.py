

import os
import sqlite3
import glob

fileList = ['information.docx','Hello.txt','myImages.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg']

conn = sqlite3.connect('pythonDrillDB.db')

with conn: # CREATE DB
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_Files(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_FileName TEXT \
        )")
    conn.commit()
cur.close()
conn.close()

for fileName in fileList: # VERIFY .TXT AND INSERT INTO TABLE
    if fileName.endswith(".txt"):
        x = fileName
        conn = sqlite3.connect('pythonDrillDB.db')
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_Files(col_FileName) VALUES (?)", \
                        (x,))
            conn.commit()
        conn.close()
        

conn = sqlite3.connect('pythonDrillDB.db')

with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_FileName FROM tbl_Files")
    varFiles = cur.fetchall()
    for item in varFiles:
        msg = "File Names: {}".format(item)
        print(msg)
