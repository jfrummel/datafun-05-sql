-- use INNER JOIN operation and optionally include LEFT JOIN, RIGHT JOIN, etc.

-- Inner join between players and statistics tables
SELECT players.name, players.position, statistics.goals, statistics.appearances, statistics.assists
FROM players
INNER JOIN statistics ON players.player_id = statistics.player_id;