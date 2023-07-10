#importing the necessary modules
import random


class Player:
    def __init__(self, name, bowling_skill, batting_skill, fielding_skill, running_skill, experience):
        """
        Initialize a Player.
        
        Args:
            name (str): Name of the player.
            bowling_skill (float): Bowling skill range(0-1)
            batting_skill (float): Batting skill range(0-1)
            fielding_skill (float): Fielding skill range(0-1)
            running_skill (float): Running skill range(0-1)
            experience (float): Experience skill range(0-1)
        """
        self.name = name
        self.bowling_skill = bowling_skill
        self.batting_skill = batting_skill
        self.fielding_skill = fielding_skill
        self.running_skill = running_skill
        self.experience = experience


class Team:
    def __init__(self, name, players):
        """
        Initialize the team.
        
        Args:
            name (str): Name of the team
            players (list): List of players
        """
        self.name = name
        self.players = players
        self.captain = None #captain of the team
        self.batting_order = players.copy() #list of batting team
        self.bowlers = [] #list of bowlers

    def set_captain(self, captain):
        self.captain = captain #captain of the team

    def get_next_batsman(self):
        if len(self.batting_order) > 0:
            return self.batting_order.pop(0)
        return None

    def get_next_bowler(self):
        return random.choice(self.bowlers)


class Field:
    def __init__(self, size, fan_ratio, pitch_conditions, home_advantage):
        """
        Initialize the field.
        Args:
            size (float): Size of the field range(0-1)
            fan_ratio (float): Fan ration
            pitch_conditions (float): Pitch conditions
            home_advantage (float): Home advantage
        """
        self.size = size
        self.fan_ratio = fan_ratio
        self.pitch_conditions = pitch_conditions
        self.home_advantage = home_advantage


class Umpire:
    """
    Initialize a umpire
    """
    def __init__(self, field):
        self.field = field
        self.scores = 0
        self.wickets = 0
        self.overs = 0

    def update_scores(self, runs):
        """
        Update the scores based on random (0-6) integer.
        """
        self.scores += runs

    def update_wickets(self):
        """
        Update the wicket by 1 in case of OUT.
        """
        self.wickets += 1

    def update_overs(self):
        """
        Update the total number of overs after every over.
        """
        self.overs += 1

    def predict_outcome(self, batsman, bowler):
        """
        Predit the chances of batsman hitting the ball or getting out.
        Args:
            batsman (player): batsman object
            bowler (player): bowler object

        Returns:
            str: OUT or NOT OUT
        """
        batting_winning = (
            batsman.batting_skill
            * batsman.experience
            * pow(bowler.fielding_skill, -1)
            * batsman.running_skill
            * self.field.home_advantage
            * pow(self.field.size, -1)
            * random.random()
        )
        bowling_winning = (
            bowler.bowling_skill
            * bowler.experience 
            * self.field.pitch_conditions 
            * random.random()
        )
        if batting_winning >= bowling_winning:
            return "NOT OUT"
        return "OUT"


class Commentator:
    def __init__(self, umpire):
        """
        Initialize the umpire.
        """
        self.umpire = umpire

    def describe_ball(self, batsman, bowler):
        """
        Prints the outcome of the ball.

        Args:
            batsman (player): batsman object
            bowler (player): bowler object

        Returns:
            str: outcome of the ball OUT vs Strikes.
        """
        
        outcome = self.umpire.predict_outcome(batsman, bowler)
        print(bowler.name, "balls")
        if outcome == "OUT":
            description = f"{batsman.name} strikes and is OUT!"
        else:
            description = f"{batsman.name} strikes."
        return description

    def describe_match(self, captain1, captain2, team1, team2, total_overs):
        """
        Describes the match.
        Args:
            captain1 (str): Captain of team 1
            captain2 (str): Captain of team 2
            team1 (str): Name of team1
            team2 (str): Name of team 2
            total_overs (int): Total number of overs
        """
        print("\n<Match Information>")
        print(f"{team1.name} (Captain - {captain1.name}) Vs {team2.name} (Captain - {captain2.name}) ")
        print(f"Total Overs: {total_overs}")

    def describe_match_start(self, team):
        """
        Informs about the match start.

        Args:
            team (str): Name of the team batting.
        """
        print("\n<Match STARTED>")
        print(f"Team {team.name} playing:")

    def describe_current_info(self, ball_count):
        """
            Gives information after each ball.
        Args:
            ball_count (int): balls played in this over.
        """
        print(f"Overs: {self.umpire.overs}.{ball_count}, Score: {self.umpire.scores}/{self.umpire.wickets}")

    def describe_match_end(self):
        """
            Gives informaton at the end of the match.
        """
        print(f"\n\nFinal Score: {self.umpire.scores}/{self.umpire.wickets+1}, Overs: {self.umpire.overs}.\n")

    def describe_final_result(self, winning_team, winning_score):
        """
            Gives the final result.
        Args:
            winning_team (str): Winning team name.
            winning_score (int): Score difference.
        """
        print("<Winner>")
        print(f"{winning_team.name} Won by - {winning_score} Runs\n")


class Match:
    def __init__(self, team1, team2, field, total_overs):
        """
        Describes the match between two teams.

        Args:
            team1 (Team): Team object of team 1
            team2 (Team): Team Object of team 2
            field (Field): Field
            total_overs (int): Total overs
        """
        self.team1 = team1
        self.team2 = team2
        self.field = field
        self.umpire = Umpire(field)
        self.commentator = Commentator(self.umpire)
        self.total_overs = total_overs
        self.batting_team = None
        self.bowling_team = None

    def toss(self):
        """
        Randomly determine the batting team
        """
    
        toss_winner = random.choice([self.team1, self.team2])
        self.batting_team = toss_winner
        self.bowling_team = self.team2 if toss_winner == self.team1 else self.team1

    def start_match(self):
        self.team1.set_captain(random.choice(self.team1.players))
        self.team2.set_captain(random.choice(self.team2.players))
        self.team1.batting_order = self.team1.players.copy()
        self.team2.batting_order = self.team2.players.copy()
        self.team1.bowlers = self.team1.players.copy()
        self.team2.bowlers = self.team2.players.copy()

        self.commentator.describe_match(
            self.team1.captain,
            self.team2.captain,
            self.team1,
            self.team2,
            self.total_overs,
        )

        # Team 1 batting
        self.commentator.describe_match_start(self.batting_team)
        self.play_innings(self.batting_team, self.bowling_team)
        self.commentator.describe_match_end()
        team1_score = self.commentator.umpire.scores

        # Team 2 batting
        self.commentator.umpire.scores = 0
        self.commentator.umpire.wickets = 0
        self.commentator.umpire.overs = 0
        self.commentator.describe_match_start(self.team2)
        self.play_innings(self.team2, self.team1)
        self.commentator.describe_match_end()
        team2_score = self.commentator.umpire.scores

        # Final outcome
        if team1_score > team2_score:
            self.commentator.describe_final_result(self.team1, team1_score - team2_score)
        else:
            self.commentator.describe_final_result(self.team2, team2_score - team1_score)


    def play_innings(self, batting_team, bowling_team):
        ball_count = 1
        over = 0
        bowler = bowling_team.get_next_bowler()
        batsman = batting_team.get_next_batsman()

        while over < self.total_overs:
            print("\n")
            if batsman is None:
                break

            ball_description = self.commentator.describe_ball(batsman, bowler)

            print(ball_description)
            if ball_description.endswith("OUT!"):
                batsman = batting_team.get_next_batsman()
                if batsman is None:
                    break
                self.umpire.update_wickets()
            else:
                runs = self.calculate_runs(batsman, bowler)
                self.umpire.update_scores(runs)

            if ball_count > 5:
                over += 1
                self.umpire.update_overs()
                bowler = bowling_team.get_next_bowler()
                ball_count = 0

            self.commentator.describe_current_info(ball_count)
            ball_count += 1

    def calculate_runs(self, batsman, bowler):
        """
        Calculate the runs scored based on batting and bowling skills.

        Args:
            batsman (Player): Batsman object
            bowler (Player): Bowler object

        Returns:
            int: Runs scored on the ball
        """
        batting_skill = batsman.batting_skill
        bowling_skill = bowler.bowling_skill

        # Adjust the batting and bowling skills to a range of 0-10
        batting_skill *= 10
        bowling_skill *= 10

        # Calculate the average of batting and bowling skills
        average_skill = abs(batting_skill - bowling_skill) / 2

        # Calculate the runs based on the average skill
        runs = random.randint(0, int(average_skill)+1)

        return runs



# Creating players for Team 1
player1 = [
    Player("Rohit Sharma", 0.8, 0.7, 0.6, 0.9, 0.8),
    Player("Shubham Gill", 0.7, 0.6, 0.5, 0.8, 0.7),
    Player("Virat Kohli", 0.6, 0.7, 0.8, 0.6, 0.9),
    Player("Ajinkya Rahane", 0.7, 0.8, 0.6, 0.7, 0.8),
    Player("Ravindra Jadeja", 0.6, 0.6, 0.7, 0.7, 0.7),
    Player("Mohammed Shami", 0.8, 0.9, 0.7, 0.8, 0.9),
    Player("Mohammed Siraj", 0.7, 0.8, 0.9, 0.7, 0.8),
    Player("Umesh Yadav", 0.6, 0.7, 0.8, 0.9, 0.7),
    Player("Ishan Kishan", 0.8, 0.9, 0.7, 0.8, 0.9),
    Player("Shardul Thakur", 0.9, 0.8, 0.7, 0.9, 0.8)
]

# Creating players for Team 2
player2 = [
    Player("Pat Cummins", 0.7, 0.8, 0.9, 0.8, 0.7),
    Player("Scott Boland", 0.6, 0.7, 0.8, 0.7, 0.6),
    Player("Cameron Green", 0.7, 0.6, 0.5, 0.6, 0.7),
    Player("Marcus Harris", 0.6, 0.7, 0.8, 0.7, 0.6),
    Player("Travis Head", 0.8, 0.6, 0.7, 0.6, 0.8),
    Player("Nathan Lyon", 0.9, 0.7, 0.8, 0.7, 0.9),
    Player("Todd Murphy", 0.8, 0.9, 0.7, 0.9, 0.7),
    Player("Steven Smith", 0.7, 0.8, 0.9, 0.8, 0.7),
    Player("Mitchell Starc", 0.8, 0.9, 0.8, 0.9, 0.8),
    Player("David Warner", 0.7, 0.8, 0.9, 0.7, 0.8)
]

# Creating teams
team1 = Team("India", player1)
team2 = Team("Australia", player2)

# Creating the field
field = Field(0.5, 0.8, 0.6, 0.7)

# Setting the total overs for the match
total_overs = 5

# Creating the match instance
match = Match(team1, team2, field, total_overs)

# Toss to determine the batting team
match.toss()

# Starting the match
match.start_match()

