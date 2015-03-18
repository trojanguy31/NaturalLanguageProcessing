# Project 1
#  - By Kedar Prabhu

# imports
import sys
import pickle
import os
import math

# initializations
LabelDict = dict()
FeatureDict = dict()
ProbOfC=dict()
VocabSize=0

ArgLen=sys.argv.__len__()
if ArgLen>=2:
    ModelFile=sys.argv[1]
    OutputFile="sentiment.out"
    TestFile=sys.argv[2]
    
# function definations
def main():
    print('<><><><><><><><><><><><><><><><><><><><><><><><>\n')
    print('CSCI544: Project 1')
    print("Let me classify now!")
    readPickle()
    findVocabSize()
    readAndWrite()
    print("Classified!")
    print("Please press Enter to continue...")
    x=input()
    print('<><><><><><><><><><><><><><><><><><><><><><><><>\n')
    
def readPickle():
    print("Reading Model File")
    global LabelDict, FeatureDict
    f=open(ModelFile,"rb")
    LabelDict=pickle.load(f)
    FeatureDict=pickle.load(f)
    f.close()

def findVocabSize():
    global VocabSize, LabelDict, FeatureDict
    UnifiedDict=dict()
    for i in range(0,LabelDict.__len__()):
        UnifiedDict.update(list(FeatureDict.values())[i])
    VocabSize=UnifiedDict.__len__()
    
    
def readAndWrite():
    print("Classifying...")
    global LabelDict, FeatureDict
    TotalClassSum=sum(list(LabelDict.values()))
    inf=open(TestFile,'r')
    opf=open(OutputFile,'w')

    for Line in inf:
        for i in range(0,LabelDict.__len__()):
            # considering all classes find P
            ProbOfC[list(LabelDict.keys())[i]]=math.log(list(LabelDict.values())[i]) - math.log(TotalClassSum)
            for Word in Line.split():
                if(Word in list(FeatureDict.values())[i]):
                    ProbOfC[list(LabelDict.keys())[i]] = ProbOfC[list(LabelDict.keys())[i]] + math.log(list(FeatureDict.values())[i][Word]) - math.log(list(LabelDict.values())[i])
                else:
                    ProbOfC[list(LabelDict.keys())[i]] = ProbOfC[list(LabelDict.keys())[i]] + math.log(1) - math.log(list(LabelDict.values())[i]+VocabSize)
                    
                
        outputStr=max(ProbOfC,key=lambda i:ProbOfC[i])+"\n"
        opf.write(outputStr)

    inf.close()
    opf.close()
    


if ArgLen>=2:
    # main flow of the code starts here!
    main()
else:
    print("Please provide necesary arguements")
