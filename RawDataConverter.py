import json


fileToParse = "Players_Raw_Output_Date20231021-204843"
file = open(fileToParse,'r')
#Read first empty line
file.readline()

#Read dict
readDict = {}
readDict = json.loads(file.readline())

#Get keys
readDictKeysList = list(readDict.keys())
playerKey = readDictKeysList[0]

#Transfer data to local Dicts
playerDict = readDict['Player']
awayDict = readDict['Away']
homeDict = readDict['Home']
nextMatchDict = readDict['Next_match']
plyerExtraDict = readDict['Player_extra']
#TODO Create basic data for events

#TODO Iterate to get the Games data and create events
it = 6
while 

#TODO ADD Jn data and points (variable len list of dictionaries)

#print(playerDict['position'])
