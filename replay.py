from slippi import Game
import glob
import os
from rating import *

dir_path = os.path.expandvars("%HOMEPATH%") + "\\Documents\\Slippi"

def print_opponent():
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
    if hasattr(player, "netplay"):
      if player.netplay.code != "NANO#493":
        opponent = player.netplay.code
  
  opponent_rating = fetch_rating(opponent)
  print("Last Opponent " + opponent + " rating: ", end="")
  print_in_green(str(opponent_rating))
  print()
  
  
  