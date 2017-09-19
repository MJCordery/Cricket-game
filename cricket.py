"""
Main Cricket File for our game

Authors: Michael Cordery, Cameron Poole
"""

# Set up our teams
teams = []

team_bangladesh = "Cricket stars  - Bangladesh Banditos.tsv"
# team_scorchers = "Cricket stars  - Perth Splorchers.tsv"

# open files for reading
file1 = open(team_bangladesh, "r")
# file2 = open(team_scorchers, "r")

#
bangladesh_players = []
heading = None
# enumerate returns index and a text line readlines is an iterable and will make a list of lines in a file
for lno, line in enumerate(file1.readlines()):
    # skip first line
    if not lno:
        # remove the end of line carry and split the string into a list using the '\t' tab delimiter
        heading = line.rstrip("\n").split("\t")
        continue
    if not heading:
        exit("No heading on File")
    player = line.rstrip("\n").split("\t")
    # combine the two lists so to create a lists with the heading a value from line
    # [ ('Player Name', player[0]), ('Role','Batter') ... ]
    # https://docs.python.org/3/library/functions.html#zip
    # convert this list of tuples into a dictionary
    # {'Player Name':player[0], 'Role':'Batter',...}

    bangladesh_players.append(dict(zip(heading, player)))

teams.append(bangladesh_players)
print(bangladesh_players)

# see if you can sort the player list according to the batting order.
# some of the values in the dictionary contains floats and ints but we have them as strings how do we convert them


# how might me streamline this code instead of copying + pasting and
# changing the values to be for the perth scorchers team
# maybe we can use the csv module on the csv files instead of splitting the line
# https://docs.python.org/3/library/csv.html
