# Project 2
# - By Kedar Prabhu

# imports
import sys
import os

# initializations
ArgLen=sys.argv.__len__()
ModelFile = sys.argv[1]
BufferFile="BufferFile.txt"

def main():
    makeBufferFile()
    callPecepClassify()

def makeBufferFile():
    opf=open(BufferFile,'w')
    for Line in sys.stdin:
        NewLine=""
        for Word in Line.split():
            if('/' in Word):
                NewLine=NewLine+Word.split('/')[0]+'*SLASH*'+Word.split('/')[1]+" "
            else:
                NewLine=NewLine+Word+" "
        opf.write(NewLine+'\n')
    opf.close()

def callPecepClassify():
    os.system("python3 ../percepclassify.py "+ModelFile+" < "+BufferFile);
    os.remove(BufferFile)

if(ArgLen>=2):
    main()
else:
    print("Please provide necessary arguments!")
