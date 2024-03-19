def create_scoreboard(participants):
    scoreboard = []
    #Iterate over each participant in the participants list
    for participant in participants:
        name = participant["name"] # participant name
        chickenwings = participant["chickenwings"] * 5
        hamburgers = participant["hamburgers"] * 3
        hotdogs = participant["hotdogs"] * 2
        total_score = chickenwings + hamburgers + hotdogs  # Calculate total score for the participant
        
        #dictionary with the participant's name and total score
        scoreboard.append({"name": name, "score": total_score})
    
    #sort the scoreboard in descending order by score, if equal, sort alphabetically by name
    scoreboard.sort(key = lambda x: (-x["score"], x["name"]))
    return scoreboard 

#TEST DATA
participants = [
    {"name": "Habanero Hillary", "chickenwings": 5, "hamburgers": 17, "hotdogs": 11},
    {"name": "Big Bob", "chickenwings": 20, "hamburgers": 4, "hotdogs": 11},
    {"name": "Brian K", "chickenwings": 15, "hamburgers": 7, "hotdogs": 15}
]
#Call the create_scoreboard function
scoreboard = create_scoreboard(participants)
print(scoreboard)


#EXPECTED OUTPUT
'''
[{'name': 'Big Bob', 'score': 134}, {'name': 'Brian K', 'score': 126}, {'name': 'Habanero Hillary', 'score': 98}]
'''