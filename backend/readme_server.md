# server my-nba

## Method Reference

- `search`

  - Endpoint:
    [`localhost:8000/search?teamName=warriors&year=2018&isActive=true`]
  - Parameters:
    - `teamName`
    - `year`
    - `isActive`
  - Response:
    {
    "team": [
    {
    "firstName": "Jordan",
    "lastName": "Bell",
    "personId": "1628395",
    "teamId": "1610612744",
    "jersey": "2",
    "pos": "F",
    "isActive": true,
    "img": "https://nba-players.herokuapp.com/players/Bell/Jordan"
    }, ... ]}

- `stats`

  - Endpoint:
    [`localhost:8000/stats?lastName=james&firstName=lebron`]
  - Parameters:
    - `lastName`
    - `firstName`
  - Response:
    {
    "stats": {
    "games_played": "46",
    "minutes_per_game": "36:54",
    "free_throw_percentage": "74.5",
    "player_efficiency_rating": "1.7"
    }
    }
