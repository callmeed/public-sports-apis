# Sports APIs

A list of publicly accessible sports APIs on the web. JSON whenever possible.

**Important**: I created gathered this information for my own educational purposes. I am not responsible for any trouble you 
may get yourself into by using this information.

## NBA 

### nba.com

`https://data.nba.net/prod/v2/[YYYYMMDD]/scoreboard.json`

Where [YYYYMMDD] is an 8-digit number representing the year, month, and day to query. For example:  
https://data.nba.net/prod/v2/20180224/scoreboard.json

### ESPN

`http://site.api.espn.com/apis/site/v2/sports/basketball/nba/scoreboard?dates=[YYYYMMDD]`

Where [YYYYMMDD] is an 8-digit number representing the year, month, and day to query. For example:  
http://site.api.espn.com/apis/site/v2/sports/basketball/nba/scoreboard?dates=20180224

### Bleacher Report

`https://scores2.bleacherreport.com/api/scores/league/NBA/Basketball?date=[YYYY-MM-DD]`

Where [YYYY-MM-DD] is a 10-character string representing the date you wish to query. For example:  
https://scores2.bleacherreport.com/api/scores/league/NBA/Basketball?date=2018-02-24

### Yahoo!

`https://api-secure.sports.yahoo.com/v1/editorial/s/scoreboard?leagues=nba&date=[YYYY-MM-DD]`

Where [YYYY-MM-DD] is a 10-character string representing the date you wish to query. For example:  
https://api-secure.sports.yahoo.com/v1/editorial/s/scoreboard?leagues=nba&date=2018-02-24

Note: low quality, may not contain complete information.

