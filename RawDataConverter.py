import json


fileToParse = "Players_Raw_Output_Date20231021-204843"
file = open(fileToParse,'r')
#Read first empty line
file.readline()

#TODO Iterate file thru keys in dict
readDict = {}
readDict = json.loads(file.readline())

print(list(readDict.keys()))

playerDict = {}
#TODO Calculate dict key based on id_pattern playerDictKey = 
#playerDict = readDict['444_Player']
awayDict = {}
homeDict = {}
nextMatchDict = {}
plyerExtraDict = {}

#TODO ADD Jn data and points (variable len list of dictionaries)

#print(playerDict['position'])
