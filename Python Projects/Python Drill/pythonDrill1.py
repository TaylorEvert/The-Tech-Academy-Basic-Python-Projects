
import os
import glob

dirPath = 'C:\\Users\\taylo\\Desktop\\TechAcademy\\Python Projects\\Python Drill\\'
dirList = os.listdir(dirPath)

for txtFile in glob.glob(os.path.join(dirPath, '*.txt')):
    print('File Path: \n{}'.format(txtFile))
    fileTime = os.path.getmtime(txtFile)
    print('File Time: \n{}\n'.format(fileTime))
    
        
        
