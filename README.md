# OOP Problem - SCOREBOARD
A scoreboard for a competitive eating competition.

Includes:<br />
A list of dictionaries representing participants. Each dictionary has the following keys:
- `name` - Name of the participant
- `chickenwings` - number of chickenwings eaten.
- `hamburgers` - number of hamburgers eaten.
- `hotdogs` - number of hotdogs eaten.

Returns<br />
A list of dictionaries representing the scoreboard. Each dictionary has the following keys:
- `name`: The name of the participant.
- `score`: The total score of the participant.

The list is sorted in descending order by score, and if scores are equal, it is sorted alphabetically by name.