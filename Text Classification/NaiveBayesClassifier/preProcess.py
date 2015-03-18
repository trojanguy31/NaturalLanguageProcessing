# Project 1
#  - By Kedar Prabhu

# Imports
import sys
import os

# Initialization


ArgLen=sys.argv.__len__()
if ArgLen>=3:
    Directory=sys.argv[1]+'/'
    OutputFile=sys.argv[2]
    if(sys.argv[3]=="Train"):
        Train=True
    else:
        Train=False

def main():
    print('\n<><><><><><><><><><><><><><><><><><><><><><><><>')
    print('CSCI544: Project 1')
    print('       - By Kedar Prabhu\n')

    
    FileNames=countFiles()
    createOutputFile()
    readInputFiles(FileNames)
    
    if(Train):
    	print('Training file Created!')
    else:
    	print('Testing file Created!')
    print('\nPlease press Enter to continue...')
    x=input()
    print('<><><><><><><><><><><><><><><><><><><><><><><><>\n')


def countFiles():
    print("Counting files from the directory...")
    return next(os.walk(Directory))[2]

def createOutputFile():
    f=open(OutputFile,'w')
    f.close()
        
def readInputFiles(FileNames):
    if(Train):
    	print("Creating the Training file...")
    else:
    	print("Creating the Testing file...")
    for Fname in FileNames:
        if(Train):
            Class=Fname.split(".")[0]+' ';
        else:
            Class=""
        appendToOutput(Class,Fname)

def appendToOutput(Class,Fname):
    InputFile=Directory+Fname
    ipf=open(InputFile,'r',encoding = "ISO-8859-1")
    opf=open(OutputFile,'a')
    outputStr=Class
    for Line in ipf:
        for Word in Line.split():
            outputStr=outputStr+Word+" "
    outputStr=outputStr+'\n'
    opf.write(outputStr)
    ipf.close()
    opf.close()
    
ArgLen=sys.argv.__len__()
if ArgLen>=3:
    main()
else:
    print("Please provide necessary arguments")
