team1 = {"Jones": 24, "Jameson": 18, "Smith": 58, "Burns": 7}
team2 = {"White": 12, "Macke": 88, "Perce": 4}
Merged_Teams = {Key:Value for team in (team1,team2) for Key,Value in team.items()}
print(Merged_Teams)
