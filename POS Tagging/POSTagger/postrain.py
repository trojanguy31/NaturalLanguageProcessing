# Project 2
# - By Kedar Prabhu

# imports
import sys
import os

# initializations
ArgLen = sys.argv.__len__()
InputFile = sys.argv[1] 
BufferFile="trainPreProcessed.txt"
ModelFile= sys.argv[2]
if(ArgLen>=4):
    DevFile = sys.argv[4]

def main():
    readFile()
    if(ArgLen>=4):
        os.system("python3 ../perceplearn.py "+ BufferFile+" "+ModelFile+" -h "+DevFile)
    else:
        os.system("python3 ../perceplearn.py "+ BufferFile+" "+ModelFile)        
    os.remove(BufferFile)

def readFile():
    inf=open(InputFile,'r',encoding="ISO-8859-1")
    opf=open(BufferFile,'w')
    for Line in inf:
        for Word in Line.split():
            Class=Word.split('/')[1]
            Feature=Word.split('/')[0]
            OutputStr=Class+" "+Feature+"\n"
            opf.write(OutputStr)
    inf.close()
    opf.close()

if(ArgLen>=2):
    main()
else:
    print("Please provide necessary arguements!")
