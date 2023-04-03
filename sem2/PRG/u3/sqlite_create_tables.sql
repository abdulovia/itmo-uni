CREATE TABLE tMusician (
    musicianId INTEGER PRIMARY KEY,
    stageName TEXT NOT NULL,
    age INTEGER NOT NULL,
    gender TEXT NOT NULL
);

CREATE TABLE tSongs (
    songId INTEGER PRIMARY KEY,
    songName TEXT NOT NULL,
    description TEXT NOT NULL,
    musicianId INTEGER,
    FOREIGN KEY (musicianId) REFERENCES tMusician (musicianId)
);

CREATE TABLE tComments (
    commentId INTEGER PRIMARY KEY,
    comment TEXT NOT NULL,
    songId INTEGER,
    musicianId INTEGER,
    FOREIGN KEY (songId) REFERENCES tSongs(songId),
    FOREIGN KEY (musicianId) REFERENCES tMusician(musicianId)
);