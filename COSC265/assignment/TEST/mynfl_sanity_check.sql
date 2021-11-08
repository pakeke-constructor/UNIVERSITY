-- Sanity Check that all tables in the test have correct size
-- If you get an error raise a concern with the Teaching Team

CREATE OR REPLACE FUNCTION is_valid(table_name varchar ,student int, expected int) RETURN int IS
BEGIN
    IF student != expected THEN
        raise_application_error(-20001, CONCAT(table_name, ': Error EXPECTED ' || to_char(expected) ||', GOT ' || to_char(student))) ;
    END IF;
    return 0;
END;
/


SELECT is_valid('CITY', (select count(*) from CITY), 60) as PASS from DUAL;
SELECT is_valid('COACH', (select count(*) from COACH), 60) as PASS from DUAL;
SELECT is_valid('DEFENSE', (select count(*) from DEFENSE), 932) as PASS from DUAL;
SELECT is_valid('GAME', (select count(*) from GAME), 4005) as PASS from DUAL;
SELECT is_valid('KICKER', (select count(*) from KICKER), 37) as PASS from DUAL;
SELECT is_valid('OFFENSIVE_LINE', (select count(*) from OFFENSIVE_LINE), 338) as PASS from DUAL;
SELECT is_valid('PLAYER', (select count(*) from PLAYER), 1954) as PASS from DUAL;
SELECT is_valid('PLAYER_TEAM', (select count(*) from PLAYER_TEAM), 2001) as PASS from DUAL;
SELECT is_valid('PUNTER', (select count(*) from PUNTER), 39) as PASS from DUAL;
SELECT is_valid('QUARTERBACK', (select count(*) from QUARTERBACK), 100) as PASS from DUAL;
SELECT is_valid('RECEIVER', (select count(*) from RECEIVER), 332) as PASS from DUAL;
SELECT is_valid('RUNNER', (select count(*) from RUNNER), 176) as PASS from DUAL;
SELECT is_valid('STADIUM', (select count(*) from STADIUM), 60) as PASS from DUAL;
SELECT is_valid('TEAM', (select count(*) from TEAM), 32) as PASS from DUAL;
SELECT is_valid('TEAM_CITY', (select count(*) from TEAM_CITY), 32) as PASS from DUAL;
SELECT is_valid('TEAM_COACH', (select count(*) from TEAM_COACH), 32) as PASS from DUAL;
SELECT is_valid('TEAM_STADIUM', (select count(*) from TEAM_STADIUM), 32) as PASS from DUAL;

DROP FUNCTION is_valid;