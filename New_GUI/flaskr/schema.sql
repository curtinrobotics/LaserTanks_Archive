CREATE TABLE player (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    lives INTEGER,
    kills INTEGER,
    deaths INTEGER
);

CREATE TABLE game (
    
);