--
-- File generated with SQLiteStudio v3.2.1 on Tue Jun 2 09:34:07 2020
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: match
CREATE TABLE [match] (
    playerID INTEGER REFERENCES stats (ID),
    scored   INTEGER,
    faced    INTEGER,
    fours    INTEGER,
    sixes    INTEGER,
    bowled   INTEGER,
    maiden   INTEGER,
    given    INTEGER,
    wkts     INTEGER,
    catches  INTEGER,
    stumping INTEGER,
    ro       INTEGER
);

INSERT INTO [match] (
                        playerID,
                        scored,
                        faced,
                        fours,
                        sixes,
                        bowled,
                        maiden,
                        given,
                        wkts,
                        catches,
                        stumping,
                        ro
                    )
                    VALUES (
                        1,
                        102,
                        98,
                        8,
                        2,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        1
                    );

INSERT INTO [match] (
                        playerID,
                        scored,
                        faced,
                        fours,
                        sixes,
                        bowled,
                        maiden,
                        given,
                        wkts,
                        catches,
                        stumping,
                        ro
                    )
                    VALUES (
                        2,
                        12,
                        20,
                        1,
                        0,
                        48,
                        0,
                        36,
                        1,
                        0,
                        0,
                        0
                    );

INSERT INTO [match] (
                        playerID,
                        scored,
                        faced,
                        fours,
                        sixes,
                        bowled,
                        maiden,
                        given,
                        wkts,
                        catches,
                        stumping,
                        ro
                    )
                    VALUES (
                        3,
                        49,
                        75,
                        3,
                        0,
                        0,
                        0,
                        0,
                        0,
                        1,
                        0,
                        0
                    );

INSERT INTO [match] (
                        playerID,
                        scored,
                        faced,
                        fours,
                        sixes,
                        bowled,
                        maiden,
                        given,
                        wkts,
                        catches,
                        stumping,
                        ro
                    )
                    VALUES (
                        4,
                        32,
                        35,
                        4,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0
                    );

INSERT INTO [match] (
                        playerID,
                        scored,
                        faced,
                        fours,
                        sixes,
                        bowled,
                        maiden,
                        given,
                        wkts,
                        catches,
                        stumping,
                        ro
                    )
                    VALUES (
                        5,
                        56,
                        45,
                        3,
                        1,
                        0,
                        0,
                        0,
                        0,
                        3,
                        2,
                        0
                    );

INSERT INTO [match] (
                        playerID,
                        scored,
                        faced,
                        fours,
                        sixes,
                        bowled,
                        maiden,
                        given,
                        wkts,
                        catches,
                        stumping,
                        ro
                    )
                    VALUES (
                        6,
                        8,
                        4,
                        2,
                        0,
                        48,
                        2,
                        35,
                        1,
                        0,
                        0,
                        0
                    );

INSERT INTO [match] (
                        playerID,
                        scored,
                        faced,
                        fours,
                        sixes,
                        bowled,
                        maiden,
                        given,
                        wkts,
                        catches,
                        stumping,
                        ro
                    )
                    VALUES (
                        7,
                        42,
                        36,
                        3,
                        3,
                        30,
                        0,
                        25,
                        0,
                        1,
                        0,
                        0
                    );

INSERT INTO [match] (
                        playerID,
                        scored,
                        faced,
                        fours,
                        sixes,
                        bowled,
                        maiden,
                        given,
                        wkts,
                        catches,
                        stumping,
                        ro
                    )
                    VALUES (
                        8,
                        18,
                        10,
                        1,
                        1,
                        60,
                        3,
                        50,
                        2,
                        1,
                        0,
                        1
                    );

INSERT INTO [match] (
                        playerID,
                        scored,
                        faced,
                        fours,
                        sixes,
                        bowled,
                        maiden,
                        given,
                        wkts,
                        catches,
                        stumping,
                        ro
                    )
                    VALUES (
                        9,
                        65,
                        60,
                        7,
                        0,
                        24,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0
                    );

INSERT INTO [match] (
                        playerID,
                        scored,
                        faced,
                        fours,
                        sixes,
                        bowled,
                        maiden,
                        given,
                        wkts,
                        catches,
                        stumping,
                        ro
                    )
                    VALUES (
                        10,
                        23,
                        42,
                        3,
                        0,
                        60,
                        2,
                        45,
                        6,
                        0,
                        0,
                        0
                    );

INSERT INTO [match] (
                        playerID,
                        scored,
                        faced,
                        fours,
                        sixes,
                        bowled,
                        maiden,
                        given,
                        wkts,
                        catches,
                        stumping,
                        ro
                    )
                    VALUES (
                        11,
                        0,
                        0,
                        0,
                        0,
                        54,
                        0,
                        50,
                        4,
                        1,
                        0,
                        0
                    );

INSERT INTO [match] (
                        playerID,
                        scored,
                        faced,
                        fours,
                        sixes,
                        bowled,
                        maiden,
                        given,
                        wkts,
                        catches,
                        stumping,
                        ro
                    )
                    VALUES (
                        12,
                        0,
                        0,
                        0,
                        0,
                        60,
                        2,
                        49,
                        1,
                        0,
                        0,
                        0
                    );

INSERT INTO [match] (
                        playerID,
                        scored,
                        faced,
                        fours,
                        sixes,
                        bowled,
                        maiden,
                        given,
                        wkts,
                        catches,
                        stumping,
                        ro
                    )
                    VALUES (
                        13,
                        15,
                        12,
                        2,
                        0,
                        60,
                        1,
                        46,
                        2,
                        0,
                        0,
                        0
                    );

INSERT INTO [match] (
                        playerID,
                        scored,
                        faced,
                        fours,
                        sixes,
                        bowled,
                        maiden,
                        given,
                        wkts,
                        catches,
                        stumping,
                        ro
                    )
                    VALUES (
                        14,
                        46,
                        65,
                        5,
                        1,
                        0,
                        0,
                        0,
                        0,
                        1,
                        0,
                        0
                    );

INSERT INTO [match] (
                        playerID,
                        scored,
                        faced,
                        fours,
                        sixes,
                        bowled,
                        maiden,
                        given,
                        wkts,
                        catches,
                        stumping,
                        ro
                    )
                    VALUES (
                        15,
                        29,
                        42,
                        3,
                        0,
                        0,
                        0,
                        0,
                        0,
                        2,
                        0,
                        1
                    );


-- Table: stats
CREATE TABLE stats (
    ID          INTEGER PRIMARY KEY AUTOINCREMENT,
    player_name STRING,
    matches     INTEGER,
    runs        INTEGER,
    no_of_100s  INTEGER,
    no_of_50s   INTEGER,
    value       INTEGER,
    ctg         TEXT
);

INSERT INTO stats (
                      ID,
                      player_name,
                      matches,
                      runs,
                      no_of_100s,
                      no_of_50s,
                      value,
                      ctg
                  )
                  VALUES (
                      1,
                      'Virat Kohli',
                      189,
                      8257,
                      28,
                      43,
                      120,
                      'BAT'
                  );

INSERT INTO stats (
                      ID,
                      player_name,
                      matches,
                      runs,
                      no_of_100s,
                      no_of_50s,
                      value,
                      ctg
                  )
                  VALUES (
                      2,
                      'Yuraj Singh',
                      86,
                      3589,
                      10,
                      21,
                      100,
                      'BAT'
                  );

INSERT INTO stats (
                      ID,
                      player_name,
                      matches,
                      runs,
                      no_of_100s,
                      no_of_50s,
                      value,
                      ctg
                  )
                  VALUES (
                      3,
                      'Ajinkya Rahane',
                      158,
                      5435,
                      11,
                      31,
                      100,
                      'BAT'
                  );

INSERT INTO stats (
                      ID,
                      player_name,
                      matches,
                      runs,
                      no_of_100s,
                      no_of_50s,
                      value,
                      ctg
                  )
                  VALUES (
                      4,
                      'Shikhar Dhawan',
                      25,
                      565,
                      2,
                      1,
                      85,
                      'AR'
                  );

INSERT INTO stats (
                      ID,
                      player_name,
                      matches,
                      runs,
                      no_of_100s,
                      no_of_50s,
                      value,
                      ctg
                  )
                  VALUES (
                      5,
                      'M.S.Dhoni',
                      78,
                      2573,
                      3,
                      19,
                      75,
                      'BAT'
                  );

INSERT INTO stats (
                      ID,
                      player_name,
                      matches,
                      runs,
                      no_of_100s,
                      no_of_50s,
                      value,
                      ctg
                  )
                  VALUES (
                      6,
                      'Axar Patel',
                      67,
                      208,
                      0,
                      0,
                      100,
                      'BOW'
                  );

INSERT INTO stats (
                      ID,
                      player_name,
                      matches,
                      runs,
                      no_of_100s,
                      no_of_50s,
                      value,
                      ctg
                  )
                  VALUES (
                      7,
                      'Hardik Pandya',
                      70,
                      77,
                      0,
                      0,
                      75,
                      'BOW'
                  );

INSERT INTO stats (
                      ID,
                      player_name,
                      matches,
                      runs,
                      no_of_100s,
                      no_of_50s,
                      value,
                      ctg
                  )
                  VALUES (
                      8,
                      'Ravindra Jadeja',
                      16,
                      1,
                      0,
                      0,
                      85,
                      'BOW'
                  );

INSERT INTO stats (
                      ID,
                      player_name,
                      matches,
                      runs,
                      no_of_100s,
                      no_of_50s,
                      value,
                      ctg
                  )
                  VALUES (
                      9,
                      'Kedar Jadhav',
                      111,
                      675,
                      0,
                      1,
                      90,
                      'BOW'
                  );

INSERT INTO stats (
                      ID,
                      player_name,
                      matches,
                      runs,
                      no_of_100s,
                      no_of_50s,
                      value,
                      ctg
                  )
                  VALUES (
                      10,
                      'Ravichandran Ashwin',
                      136,
                      1914,
                      0,
                      10,
                      100,
                      'AR'
                  );

INSERT INTO stats (
                      ID,
                      player_name,
                      matches,
                      runs,
                      no_of_100s,
                      no_of_50s,
                      value,
                      ctg
                  )
                  VALUES (
                      11,
                      'Umesh Yadav',
                      296,
                      9496,
                      10,
                      64,
                      110,
                      'WK'
                  );

INSERT INTO stats (
                      ID,
                      player_name,
                      matches,
                      runs,
                      no_of_100s,
                      no_of_50s,
                      value,
                      ctg
                  )
                  VALUES (
                      12,
                      'Jasprit Bumrah',
                      73,
                      1365,
                      0,
                      8,
                      60,
                      'WK'
                  );

INSERT INTO stats (
                      ID,
                      player_name,
                      matches,
                      runs,
                      no_of_100s,
                      no_of_50s,
                      value,
                      ctg
                  )
                  VALUES (
                      13,
                      'Bhuvaneshwar Kumar',
                      17,
                      289,
                      0,
                      2,
                      75,
                      'AR'
                  );

INSERT INTO stats (
                      ID,
                      player_name,
                      matches,
                      runs,
                      no_of_100s,
                      no_of_50s,
                      value,
                      ctg
                  )
                  VALUES (
                      14,
                      'Rohit Sharma',
                      304,
                      8701,
                      14,
                      52,
                      85,
                      'BAT'
                  );

INSERT INTO stats (
                      ID,
                      player_name,
                      matches,
                      runs,
                      no_of_100s,
                      no_of_50s,
                      value,
                      ctg
                  )
                  VALUES (
                      15,
                      'Kartick Bose',
                      11,
                      111,
                      0,
                      0,
                      75,
                      'AR'
                  );


-- Table: teams
CREATE TABLE teams (
    ID        INTEGER PRIMARY KEY AUTOINCREMENT,
    team_name STRING,
    players   VARCHAR,
    value     INTEGER
);


COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
