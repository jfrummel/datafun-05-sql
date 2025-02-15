-- use GROUP BY clause (and optionally with aggregation)

-- Group players by position

SELECT COUNT(player_id), position
FROM players
GROUP BY position
ORDER BY COUNT(player_id) DESC;

