-- use aggregation functions including COUNT, AVG, SUM.

-- count all rows in the authors table
SELECT COUNT(*) as players_count from players;

-- get average retail price of books
SELECT AVG(appearances) FROM statistics;

-- get the total retail price of all books
SELECT SUM(goals) FROM statistics;