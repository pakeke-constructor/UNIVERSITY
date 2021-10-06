

-- Practice test answers:



-- question 5:
SELECT p.player_name, p.player_surname, COUNT(*) as TMS FROM
Player p JOIN Player_team team
ON p.player_id = team.player_id
GROUP BY p.player_name, p.player_surname
HAVING COUNT(*) > 1


-- question 7:
SELECT Stadium.stadium_name, MAX(ABS(Game.local_score - Game.visitor_score)) FROM
(Stadium JOIN Team_Stadium ON Stadium.stadium_id = Team_Stadium.stadium_id) 
JOIN Game ON (Team_Stadium.team_id = Game.local_team_id)
GROUP BY Stadium.stadium_name;


-- Question 9:
SELECT ROUND(AVG(Game.visitor_score), 2) AS VISITOR, ROUND(AVG(Game.local_score), 2) AS LOCAL
FROM  (Game JOIN Team_Stadium ON (Game.local_team_id = Team_Stadium.team_id))
JOIN Stadium ON (Stadium.stadium_id = Team_Stadium.stadium_id)
WHERE Stadium.turf = 'Natural';


-- Question 11:
SELECT COUNT(DISTINCT City.city_id) AS NO_TEAM_COUNT FROM
City
WHERE
City.city_id NOT IN (Select Team_City.city_id FROM Team_City);

-- ANSWER:  29




-- Question 13:
SELECT City.city_name AS CITY_NAME
FROM City JOIN Team_City ON City.city_id = Team_City.city_id
GROUP BY City.city_name
HAVING COUNT(*) > 1
ORDER BY City.city_name ASC;





-- QUESTION 15:
SELECT Coach.coach_name, Coach.coach_surname FROM
(Team JOIN Team_Coach ON Team.team_id = Team_Coach.team_id)
JOIN Coach ON Coach.coach_id = Team_Coach.coach_id
WHERE
(SELECT COUNT(*)
FROM Game WHERE
(Game.local_score > Game.visitor_score) AND Game.local_team_id = Team.team_id
OR (Game.visitor_score > Game.local_score) AND Game.visitor_team_id = Team.team_id)
=
(SELECT COUNT(*)
FROM Game WHERE
((Game.local_score < Game.visitor_score) AND Game.local_team_id = Team.team_id)
OR ((Game.visitor_score < Game.local_score) AND Game.visitor_team_id = Team.team_id));
-- This is a bad solution- find a better way to do this thru answers.





-- queston 17:
-- THIS IS INCORRECT!
-- FIXME.
SELECT MAX(Offensive_Line.pancakes)
FROM
(Team JOIN Player_Team ON Team.team_id = Player_Team.team_id)
JOIN Player ON Player.player_id = Player_Team.player_id
WHERE Player.player_id IN (SELECT Offensive_Line.player_id FROM Offensive_Line)
GROUP BY
Team.division, Team.conference;



