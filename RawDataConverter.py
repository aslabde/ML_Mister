import json
from collections import deque 
import time

fileToParse = "Players_Raw_Output_Date20231024-224436"
file = open(fileToParse,'r')

#Create output structure: allEventsDictionary{eventID:{K:V}}
allEventsDictionary={}

#TODO Embed full logic below on a a loop for all the players
for line in file:
    if line is not None or line is not "\n":
        readDict = {}
        readDict = json.loads(line)

        #Get keys
        readDictKeysList = list(readDict.keys())
        playerKey = readDictKeysList[0]

        #Transfer data to local Dicts
        playerDict = readDict[playerKey]['Player']
        awayDict = readDict[playerKey]['Away']
        homeDict = readDict[playerKey]['Home']
        nextMatchDict = readDict[playerKey]['Next_match']
        plyerExtraDict = readDict[playerKey]['Player_extra']
        #Create basic data for events
        basicEventData = {}
        basicEventData['player_id'] = playerKey
        basicEventData['team_id'] = playerDict['id_team']
        basicEventData['position'] = playerDict['position']
        basicEventData['player_value'] = playerDict['value']

        #Iterate to get the Games data and create events
        innerDictKeysList = list(readDict[playerKey].keys())
        it = 5
        it_J = 0
        #Queues are intended to gather data to calculate streaks
        q_points = deque()
        q_matchesPlayed = deque()
        while it < len(innerDictKeysList)-1:
            print(innerDictKeysList[it])
            it += 1
            it_J +=1
            eventKey = playerKey+'_J'+str(it_J)
            matchDict = readDict[playerKey][eventKey]

            #Order is J1 -> Jn; J1-J3 cummulative data; J4 first event
            if it_J > 3:
                #calculate
                totalStreakPoints = sum(list(q_points))
                averageStreakPoints = totalStreakPoints/3
                streakMatchesPlayed = sum(list(q_matchesPlayed))
                #create event
                #print(str(playerKey) + "_J:" + str(it_J) + " total points " + str(totalStreakPoints) + " avg " 
                #    + str(averageStreakPoints) + " matches played " + str(streakMatchesPlayed))
                eventDict = {}
                eventKey = playerKey+'_J'+str(it_J)
                eventDict['player_id'] = playerKey
                eventDict['team_id'] = playerDict['id_team']
                eventDict['position'] = playerDict['position']
                eventDict['player_value'] = playerDict['value']
                eventDict['total_streak_points'] = totalStreakPoints
                eventDict['average_streak_points'] = averageStreakPoints
                eventDict['streak_matches_played'] = streakMatchesPlayed
                #TODO Include goals, overall average, away/home, n-matches streak....into the model
                #TODO Also club id could be modified according to (last session postition??)
                #Insert outcome
                eventDict['points'] = matchDict['points']
                allEventsDictionary[eventKey]=eventDict

            #update Qs
            matchPoints = matchDict['points']
            if matchPoints is not None:
                q_points.append(int(matchPoints))
                q_matchesPlayed.append(1)
            else:
                q_points.append(0)
                q_matchesPlayed.append(0)

            #keep Qs with 3 elements
            if it_J > 3:
                q_points.popleft()
                q_matchesPlayed.popleft()

file.close()

#Create dataset output
version = 'v1_'
timestr = time.strftime("%Y%m%d-%H%M%S")
dataset_Output_Date = "Dataset_"+version+timestr
oFile = open(dataset_Output_Date,'w')
oFile.write(json.dumps(allEventsDictionary))
oFile.close()


