CREATE TABLE player (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    totalLives INTEGER,
    totalKills INTEGER,
    highScore INTEGER,
    totalScore INTEGER,
    deaths INTEGER
);

/*A table containing entries of running games*/
CREATE TABLE game (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    playerIds TEXT NOTNULL,
    startTime INTEGER NOTNULL,
    endTime INTEGER,
    gameType TEXT,
    numPlayers INTEGER NOTNULL,
    players TEXT NOTNULL /*an array of layers serialised as a json*/
);