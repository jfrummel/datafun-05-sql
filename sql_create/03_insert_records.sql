
-- Insert records into the players table first
INSERT INTO players (player_id, name, age, position) VALUES
    ('PLAYER_001', 'Cole Palmer', 22, 'Midfielder'),
    ('PLAYER_002', 'Moises Caicedo', 23, 'Midfielder'),
    ('PLAYER_003', 'Robert Sanchez', 27, 'Goalkeeper'),
    ('PLAYER_004', 'Marc Cucurella', 26, 'Defender'),
    ('PLAYER_005', 'Trevoh Chalobah', 25, 'Defender'),
    ('PLAYER_006', 'Pedro Neto', 25, 'Forward');

-- Insert records into the statistics table
-- And include foreign key references to the players table
-- IMPORTANT: No tic marks inside a string, use two single quotes to escape a single quote
INSERT INTO statistics(stat_id, appearances, goals, assists, player_id) VALUES
    ('STAT_001', 77, 36, 18, 'PLAYER_001'),
    ('STAT_002', 105, 4, 7, 'PLAYER_002'),
    ('STAT_003', 124, 0, 0, 'PLAYER_003'),
    ('STAT_004', 103, 3, 6, 'PLAYER_004'),
    ('STAT_005', 74, 7, 2, 'PLAYER_005'),
    ('STAT_006', 133, 13, 21, 'PLAYER_006');
