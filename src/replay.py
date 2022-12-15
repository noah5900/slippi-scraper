from slippi import Game
import glob
import os
from rating import fetch_rating, fetch_win_loss, get_file_rank, update_file_rank
from printer import get_rank_division, print_rating_to_next_rank
from colors import print_in_green, print_in_red

dir_path = os.path.expandvars("%HOMEPATH%") + "\\Documents\\Slippi"

def post_game_summary(player_name):
    # Find difference in rank
    newRating = float(fetch_rating(player_name))
    oldRating = float(get_file_rank(player_name))
    difference = newRating - oldRating
    difference = round(difference)

    # Print change in rank
    print("Rating Change: ", end="")
    if difference >= 0:
        print_in_green("+" + str(difference))
    elif difference < 0:
        print_in_red(str(difference))
    print()
    
    # Print distance to next rank
    print_rating_to_next_rank(newRating)

    # Print current rank
    print("Current rank: ", end="")
    print_in_green(str(round(newRating)))
    print(" " + get_rank_division(newRating) + " ", end="")
    
    # Print record
    print_win_loss(player_name)
    
    # Print opponent
    print_opponent(player_name)
    
    # Update the file
    update_file_rank(str(newRating))

def print_opponent(player_name):
    # Use glob to find all the files in the directory
    files = glob.glob(os.path.join(dir_path, "*"))

    # Sort the files by their modification time
    files.sort(key=os.path.getmtime)

    # Get the newest file
    newest_file = files[-1]
    
    game = Game(newest_file)
    
    players = game.metadata.players
    opponent = ""
    for player in players:
        if hasattr(player, "netplay") and hasattr(player.netplay, "code"):
           if player.netplay.code != player_name:
              opponent = player.netplay.code
    if opponent != "":
        opponent_rating = fetch_rating(opponent)
        print(opponent + " rank: ", end="")
        print_in_green(str(round(opponent_rating)))
        print(" " + get_rank_division(opponent_rating) + " ", end="")
        print_win_loss(opponent)
        print()
    else:
       print("Unable to parse opponent from replay")

def print_win_loss(user):
    # Print win/loss/games
    matchRecord = fetch_win_loss(user)
    
    if matchRecord[2] != 0:
      print_in_green(matchRecord[0])
      print("/", end="")
      print_in_red(matchRecord[1])
      print(" (" + str(matchRecord[2]) + ")")