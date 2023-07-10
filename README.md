# Advanced Cricket Tournament Simulation Program using Python
The goal is to develop a Python program that simulates a cricket tournament involving various teams with an advanced level of detail. 
It is designed to mimic real-world cricket matches and statistics.

## The program consists of the following key classes: 

- Player: This class contains information on player stats, such as name (e.g., "MS Dhoni") bowling: 0.2 batting: 0.8 fielding: 0.99 running: 0.8 experience: 0.9, etc. These player stats when running the simulation affects the probabilities of various events occurring like a boundary, getting out, etc. 

- Teams: A team consists of players. It has methods like selecting the captain, sending the next player to the field, choosing a bowler for an over, deciding batting order, etc. 

- Field: This class contains factors like field size, fan ratio, pitch conditions, home advantage, etc., which can impact the probabilities of the simulation. 

- Umpire: This class is responsible for chunking the probabilities of all the players on the field and predicting the outcome of a ball. The Umpire class will also keep track of scores, wickets, and overs.

- Commentator: This class provides commentary for each ball and over. It gives a description of the ongoing game events.

- Match: This class simulates an individual cricket match. It will use objects of the Teams, Field, and Umpire classes and have methods to start the match and end the match.



## Demo

Video link - https://youtu.be/04hJU1o16pE

## Run Locally

1. Clone the project

```bash
  git clone https://github.com/gulshan-kumar-123/Advanced_cricket_tournament.git
```

2. Go to the project directory

```bash
  cd Advanced_Cricket_Tournament
```

3. Run main.py

```bash
  python main.py
```



## Run Online

1. To run the project online visit the below website.

```bash
  https://www.programiz.com/python-programming/online-compiler/
```

2. Copy all the code from the below website.

```bash
  https://github.com/gulshan-kumar-123/Advanced_Cricket_Tournament/blob/main/main.py
```

3. Paste the code and run.


