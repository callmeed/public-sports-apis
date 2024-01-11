import requests 


url = "https://site.api.espn.com/apis/site/v2/sports/basketball/nba/scoreboard"

print("API URL: ", url)

r = requests.get(url)
data = r.json()
r.close()

print("Events today: ", len(data['events']))

for event in data['events']:
  short_name = event['shortName']
  game_time = event['status']['type']['shortDetail'].split(" - ")
  game_msg = game_time[1] if len(game_time) > 1 else game_time[0]
  team1 = event['competitions'][0]['competitors'][0]['team']['abbreviation']
  team2 = event['competitions'][0]['competitors'][1]['team']['abbreviation']
  score1 = event['competitions'][0]['competitors'][0]['score']
  score2 = event['competitions'][0]['competitors'][1]['score']

  status = event['competitions'][0]['status']
  info = ''
  if status['type']['name'] == 'STATUS_FINAL':
    info = 'F'
  elif status['type']['name'] == 'STATUS_SCHEDULED':
    info = 'PRE'
  else:
    info = f"Q#{status['period']}"

  print(short_name)
  print(team1.ljust(4), " ", score1.rjust(4))
  print(team2.ljust(4), " ", score2.rjust(4))
  print(info)
  print(game_msg)
  print('-----')
