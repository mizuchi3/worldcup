insert into games (match_date,team_a,team_b) values('2014-06-12 17:00:00','Brazil','Croatia');
insert into games (match_date,team_a,team_b) values('2014-06-13 13:00:00','Mexico','Cameroon');
insert into games (match_date,team_a,team_b) values('2014-06-13 16:00:00','Spain','Netherlands');
insert into games (match_date,team_a,team_b) values('2014-06-13 19:00:00','Chile','Australia');
insert into games (match_date,team_a,team_b) values('2014-06-14 13:00:00','Colombia','Greece');
insert into games (match_date,team_a,team_b) values('2014-06-14 22:00:00','Ivory Coast','Japan');
insert into games (match_date,team_a,team_b) values('2014-06-14 16:00:00','Uruguay','Costa Rica');
insert into games (match_date,team_a,team_b) values('2014-06-14 19:00:00','England','Italy');
insert into games (match_date,team_a,team_b) values('2014-06-15 13:00:00','Switzerland','Ecuador');
insert into games (match_date,team_a,team_b) values('2014-06-15 16:00:00','France','Honduras');
insert into games (match_date,team_a,team_b) values('2014-06-15 19:00:00','Argentina','Bosnia-Herzegovina');
insert into games (match_date,team_a,team_b) values('2014-06-16 16:00:00','Iran','Nigeria');
insert into games (match_date,team_a,team_b) values('2014-06-16 13:00:00','Germany','Portugal');
insert into games (match_date,team_a,team_b) values('2014-06-16 19:00:00','Ghana','USA');
insert into games (match_date,team_a,team_b) values('2014-06-17 13:00:00','Belgium','Algeria');
insert into games (match_date,team_a,team_b) values('2014-06-17 19:00:00','Russia','South Korea');
insert into games (match_date,team_a,team_b) values('2014-06-17 16:00:00','Brazil','Mexico');
insert into games (match_date,team_a,team_b) values('2014-06-18 19:00:00','Cameroon','Croatia');
insert into games (match_date,team_a,team_b) values('2014-06-18 16:00:00','Spain','Chile');
insert into games (match_date,team_a,team_b) values('2014-06-18 13:00:00','Australia','Netherlands');
insert into games (match_date,team_a,team_b) values('2014-06-19 13:00:00','Colombia','Ivory Coast');
insert into games (match_date,team_a,team_b) values('2014-06-19 19:00:00','Japan','Greece');
insert into games (match_date,team_a,team_b) values('2014-06-19 16:00:00','Uruguay','England');
insert into games (match_date,team_a,team_b) values('2014-06-20 13:00:00','Italy','Costa Rica');
insert into games (match_date,team_a,team_b) values('2014-06-20 16:00:00','Switzerland','France');
insert into games (match_date,team_a,team_b) values('2014-06-20 19:00:00','Honduras','Ecuador');
insert into games (match_date,team_a,team_b) values('2014-06-21 13:00:00','Argentina','Iran');
insert into games (match_date,team_a,team_b) values('2014-06-21 19:00:00','Nigeria','Bosnia-Herzegovina');
insert into games (match_date,team_a,team_b) values('2014-06-21 16:00:00','Germany','Ghana');
insert into games (match_date,team_a,team_b) values('2014-06-22 19:00:00','USA','Portugal');
insert into games (match_date,team_a,team_b) values('2014-06-22 13:00:00','Belgium','Russia');
insert into games (match_date,team_a,team_b) values('2014-06-22 16:00:00','South Korea','Algeria');
insert into games (match_date,team_a,team_b) values('2014-06-23 17:00:00','Cameroon','Brazil');
insert into games (match_date,team_a,team_b) values('2014-06-23 17:00:00','Croatia','Mexico');
insert into games (match_date,team_a,team_b) values('2014-06-23 13:00:00','Australia','Spain');
insert into games (match_date,team_a,team_b) values('2014-06-23 13:00:00','Netherlands','Chile');
insert into games (match_date,team_a,team_b) values('2014-06-24 17:00:00','Japan','Colombia');
insert into games (match_date,team_a,team_b) values('2014-06-24 17:00:00','Greece','Ivory Coast');
insert into games (match_date,team_a,team_b) values('2014-06-24 13:00:00','Italy','Uruguay');
insert into games (match_date,team_a,team_b) values('2014-06-24 13:00:00','Costa Rica','England');
insert into games (match_date,team_a,team_b) values('2014-06-25 17:00:00','Honduras','Switzerland');
insert into games (match_date,team_a,team_b) values('2014-06-25 17:00:00','Ecuador','France');
insert into games (match_date,team_a,team_b) values('2014-06-25 13:00:00','Nigeria','Argentina');
insert into games (match_date,team_a,team_b) values('2014-06-25 13:00:00','Bosnia-Herzegovina','Iran');
insert into games (match_date,team_a,team_b) values('2014-06-26 13:00:00','USA','Germany');
insert into games (match_date,team_a,team_b) values('2014-06-26 13:00:00','Portugal','Ghana');
insert into games (match_date,team_a,team_b) values('2014-06-26 17:00:00','South Korea','Belgium');
insert into games (match_date,team_a,team_b) values('2014-06-26 17:00:00','Algeria','Russia');

UPDATE games SET match_date=DATETIME(match_date, '+300 minutes');