# Project 1
#  - By Kedar Prabhu

# Imports
import os
import sys
import pickle

# Initializations
LabelDict=dict()
FeatureDict=dict()
NumOfClass=0

ArgLen=sys.argv.__len__()
if ArgLen>=3:
    InputFile=sys.argv[1]
    OutputFile=sys.argv[2]

# Function definations
def main():
    print('\n<><><><><><><><><><><><><><><><><><><><><><><><>')
    print('CSCI544: Project 1')
    print('       - By Kedar Prabhu\n')
    getNumOfClass()
    readInputFile()
    writeModelFile()    
    print('Model file Created!')
    print('\nPlease press Enter to continue...')
    print('<><><><><><><><><><><><><><><><><><><><><><><><>\n')
    x=input()

def getNumOfClass():
    print('Counting number of classes...')
    inf=open(InputFile,'r',encoding = "ISO-8859-1")
    for Line in inf:
        for Word in Line.split():
            if Word in LabelDict:
                LabelDict[Word]=LabelDict[Word]+1
            else:
                LabelDict[Word]=1                
            break
    inf.close()
        
def readInputFile():
    print('Training...')
    # initialize dictionary for each classes
    global NumOfClass
    NumOfClass = LabelDict.__len__()
    for i in range(0,NumOfClass):
        FeatureDict[list(LabelDict.keys())[i]]=dict()

    #read the training file to get the features
    inf=open(InputFile,'r',encoding = "ISO-8859-1")
    for Line in inf:
        for p in string.punctuation:
            Line=Line.replace(p,"")
        flag=True
        for Word in Line.split():
            if(flag==True):
                flag=False
                Type=Word
            else:
                updateDictionary(FeatureDict[Type],Word)
    
    inf.close()
    
          
def updateDictionary(TheDict,Word):
    if Word in TheDict:
        TheDict[Word]=TheDict[Word]+1
    else:
        TheDict[Word]=1                 

    
def writeModelFile():
    print('Creating model file...')
    f=open(OutputFile,"wb")
    pickle.dump(LabelDict,f)
    pickle.dump(FeatureDict,f)
    f.close()


if ArgLen>=3:
    # main flow of the code starts here!
    main()
else:
    print("Please provide necesary arguements")




