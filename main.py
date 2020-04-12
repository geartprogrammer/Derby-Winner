
def decide_champion(matches):
  team1wins = 0
  team2wins = 0

  for match in matches:
    if match[0] > match[1]:
      team1wins += 1
    elif match[0] < match[1]:
      team2wins += 1


  if team1wins > team2wins:
    return 1
    print(1)

  if team1wins == team2wins:
    return 0
    print(0)

    

  elif team1wins < team2wins:
    return 2
    print(2)

matches = [[2,0], [0,5], [3,0], [6,8], [0,7]]

print(decide_champion(matches))
