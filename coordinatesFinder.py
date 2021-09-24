import re
import time
import sys
import os

''' 
running command from terminal -
python coordinatesFinder.py filename filepath
    filename : required : name of html/text file that contains the source code
    filepath : optional : path to the file, if not then it will look for the file in existing directory
'''

'''
For entire planet - 
    Latitude can have maximum of 2 digits before decimal
    Longitude can have maximum of 3 digits before decimal
'''


latlng_regex = "\"latitude\":-{0,1}\d{1,2}\.\d\d+,\"longitude\":-{0,1}\d{1,3}\.\d\d+"
latlng_regex = re.compile("(?i)"+latlng_regex)


def readFile(fileName):
    htmlFile = open(os.path.join(fileName),'r',encoding="utf-8")

    sourceCode = ""
    line = htmlFile.readline()
    while(line != ""):
        sourceCode += line
        line = htmlFile.readline()
    
    return sourceCode


def getCoordinates(htmlFile):
    coordinates = latlng_regex.findall(htmlFile)
    return coordinates

    
if __name__ == "__main__":

    file_name = ""

    systemArgs = len(sys.argv)

    if(systemArgs == 1):
        print("Missing at least 1 parameter")
        quit()
     
    elif(systemArgs == 2):
        file_name = sys.argv[1]

    elif(systemArgs == 3):
        file_name = sys.argv[1]
        file_path = sys.argv[2]
        file_name = os.path.join(file_path,file_name)
    
    else:
        print("More than required parameters given")
        quit()
    
    
   
    a = time.time()
    htmlFile = readFile(file_name)
    coordinates = getCoordinates(htmlFile)
    print("Total of {} Coordinates found in {} seconds".format(len(coordinates),time.time()-a))    

    for i in coordinates:
        print(i)