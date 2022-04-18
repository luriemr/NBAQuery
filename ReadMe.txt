- This all works for me on PC but some commands in the terminal might be different on Mac
- Make sure you have python installed
- Download and install Postgres 12.3 --> https://www.enterprisedb.com/downloads/postgres-postgresql-downloads
- Make password 123 if it asks during install
- Open command prompt and navigate to the postgresql/12/bin directory and type
- > psql -U postgres
- Enter password, should be 123, then type
- > CREATE DATABASE NBASTATS;
- ; is important in postgres, hitting enter without a ; will think you're still adding to your command
- > \c NBASTATS
- That last command connects to the database after you made it
- You can type \d to view contents in whatever DB you're in to know what you can connect to



- The last two commands are below, they're big command blocks so paste them entirely into the terminal and just hit enter
- The first command CREATE TABLE creates the table and sets the input types for each of the stats.
- The second command below it COPY just populates each of those stats with the data from allstats.csv
- You will have to change the FROM'' part of the copy to where you put the allstats.csv on your computer, cause it's setup for my drive right now.
- Just copy the create table command block first, and the terminal should return CREATE DATABASE if it works.
- Then copy the copy command and it should return COPY 26421 to indicate it copied 26421 rows of data.



CREATE TABLE players_players
(
  id serial NOT NULL,
  year int,
  player text,
  pos text,
  age int,
  tm text,
  g int,
  mpg real,
  tspercent real,
  fg int,
  fga int,
  fgpercent real,
  threep int,
  threepa int,
  threeppercent real,
  twop int, 
  twopa int, 
  twoppercent real,
  efgpercent real,
  ft int,
  fta int,
  ftpercent real,
  rpg real,
  reb int,
  apg real,
  ast int,
  spg real,
  stl int,
  bpg real,
  blk int,
  topg real,
  tov int, 
  ppg real,
  pts int
);



COPY players_players
(
  id,
  year, 
  player, 
  pos, 
  age, 
  tm,
  g, 
  mpg, 
  tspercent, 
  fg, 
  fga, 
  fgpercent, 
  threep, 
  threepa, 
  threeppercent, 
  twop, 
  twopa, 
  twoppercent, 
  efgpercent, 
  ft, 
  fta, 
  ftpercent, 
  rpg, 
  reb, 
  apg, 
  ast, 
  spg, 
  stl, 
  bpg, 
  blk, 
  topg, 
  tov, 
  ppg, 
  pts 
)
FROM 'C:\Users\Jake\Projects\NBAQuery\allstats.csv' DELIMITER ',' CSV HEADER;


- At this point you can type select * from players_players;  or any other SQL query


Starting The App
- in terminal, in the NBAQUERY base folder, navigate to env/scripts and then type activate.
- This part may be different on Mac, so just googled how to activate an ENV on mac
- Once you're in the env, it should say (env) in your terminal
- That just activates all the packages I installed to make this project run. 
- I think this includes Django but if it doesnt you'll just have to type pip install django in your terminal
- Now navigate back to the nbaquery folder, go inside the next nbaquery folder where the manage.py file is, and type
> manage.py runserver

The server should start, then type 127.0.0.1:8000 in your browser to connect