"""
Notes. You don't have to finish statements  with ';' like you do in javascript.
As long as you have indetation. You are good.
There are few ways I would write your problem
"""
roles = [
    "team captain",
    "opening batsman",
    "role3",
    "role4"
]

names = [
]

# The quick way
for role in roles:
    names.append(input("Name of role {}:".format(role)))

# Get in the habit of using format on your stings
# You will save yourself heaps of time.
# https://pyformat.info/

# print out names
print(names)

# to print name and roles
for n, r in zip(roles, names):
    print("Cricketer {} has role {}".format(r, n))

# If you want to use an index use enumerate it itereates over your list
# You use list[index] assignment to set values in a list same applies for keys in a dict

# Do this
for index, role in enumerate(roles):
    names[index] = input("Name your " + role + " :")

# Not this
for index in len(roles):
    names[index] = input("Name your " + role[index] + " :")

# A dictionary of role: cricketer name might be even better for printing and setting values
cricketers = {}  # create dict
for role in roles:
    cricketers[role] = input("Name of role {}:".format(role))

# Iterate through all the items in your dictionary role=key, cricketer=value
for role, cricketer in cricketers.items():
    print("{role}: {cricketer}".format(role=role, cricketer=cricketer))

# **dict unpacks all values in your dict
# You can then use to format
# Don't worry about understanding it its mostly magic
print("""
Team Captain is :{team captain}
Opening Batsman is: {opening batsman}
""".format(**cricketers))


# This is the advanced way using Object orientated Programming
# But you can start using checks to make sure values are set and define how to print out values
# See https://docs.python.org/3/tutorial/classes.html for a bit of an intro

class Cricketer(object):
    """
    A standard cricket player
    """
    player_types = ["Batter", "Bowler", " All Rounder"]

    def __init__(self, role="", name="", player_type=""):
        self.role = role
        self.name = name
        self.player_type = player_type
        # Do extra set up level
        self.set_up_player()

    def ask_role(self):
        self.role = input("What is this cricketers role ?")

    def ask_name(self):
        self.name = input("What is this cricketers name ?")

    def ask_player_type(self):
        ptype = input("What type of player are they {} ?".format(",".join(Cricketer.player_types)))
        if not ptype in Cricketer.player_types:
            print("Couldn't set player type pick {}".format(",".join(Cricketer.player_types)))
        self.player_type = ptype

    def set_up_player(self):
        if not self.role:
            self.ask_role()
        else:
            overwrite = input("Would you like to overwrite role {} [Y/N]?".format(self.role))
            if overwrite.lower() == "y":
                self.ask_role()
        if not self.name:
            self.ask_name()
        else:
            overwrite = input("Would you like to overwrite name {} [Y/N]?".format(self.name))
            if overwrite.lower() == "y":
                self.ask_name()
        if not self.player_type:
            self.ask_player_type()
        else:
            overwrite = input("Would you like to overwrite player_type {} [Y/N]?".format(self.player_type))
            if overwrite.lower() == "y":
                self.ask_player_type()

    def __str__(self):
        return "{} - {} - {}".format(self.role, self.name, self.player_type)


cricketers = []
for i in range(3):
    cricketers.append(Cricketer())

# This is how normally ou might add a player, the set_up_player function would check for extra values
glen_mcgrath = Cricketer("Final Player", "Glen Mcgrath", "Bowler")
cricketers.append(glen_mcgrath)

# Will print out using string function
print(glen_mcgrath)

# Add new player types
Cricketer.player_types.append("Wicket Keeper")


# You should probably have a Team Object to
# You can have a think of some other functions you might like to add
# Print players, Change Team name.
# Is a player in a team.
class Team(object):
    """
    Team of cricketers
    """

    def __init__(self, team_name):
        self.team_name = team_name
        self.players = []

    def add_new_player(self):
        if len(self.players) < 12:
            self.players.append(Cricketer())
        else:
            print("Too many players remove a player first")


# I'll let you create the rest of the match objects function
class CricketMatch(object):
    """
    Cricket Match class
    """

    def __init__(self):
        self.teams = []
        self.scores = []
        self.ground = None