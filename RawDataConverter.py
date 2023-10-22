import json


fileToParse = "Players_Raw_Output_Date20231022-194741"
file = open(fileToParse,'r')
#Read first empty line
file.readline()

#TODO Embed full logic below on a a loop for all the players

#Read dict
readDict = {}
readDict = json.loads(file.readline())

#Get keys
readDictKeysList = list(readDict.keys())
playerKey = readDictKeysList[0]

#Transfer data to local Dicts
playerDict = readDict[playerKey]['Player']
awayDict = readDict[playerKey]['Away']
homeDict = readDict[playerKey]['Home']
nextMatchDict = readDict[playerKey]['Next_match']
plyerExtraDict = readDict[playerKey]['Player_extra']
#TODO Create basic data for events

#Iterate to get the Games data and create events
innerDictKeysList = list(readDict[playerKey].keys())
it = 5
while it < len(innerDictKeysList)-1:
    print(innerDictKeysList[it])
    it += 1
    #TODO: CREATE EVENTS HERE 
    #Order is J1 -> Jn

#TODO ADD Jn data and points (variable len list of dictionaries)

