
CREATE TABLE players (
    player_id TEXT PRIMARY KEY, -- Prefixed sequential ID as the primary key (e.g., AUTHOR_001)
    name TEXT NOT NULL,         -- Player's name (mandatory field)
    age INTEGER,                -- Age 
    position TEXT               -- Position
);

-- Create the statistics table
CREATE TABLE statistics (
    stat_id TEXT PRIMARY KEY,       -- Prefixed sequential ID as the primary key (e.g., STAT_001)
    appearances INTEGER,            -- Appearances
    goals INTEGER,                  -- Goals scored
    assists INTEGER,                -- Year of publication
    player_id TEXT,                 -- Foreign key linking to players
    FOREIGN KEY (player_id) REFERENCES players (player_id) -- Relationship with players
);