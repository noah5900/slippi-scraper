from time import time
import requests
import time
import os
from pathlib import Path
from colors import print_in_green, print_in_red
import sys
from rating import *
from replay import print_opponent

os.system("")
os.system("cls")

player_name = input("Please enter your slippi connect code (e.g. NANO#493): ")

def main():
    if not os.path.exists(rankFileLocation):
        print("Initiating rank file")
        f = open(rankFileLocation, "w")
        currentRating = fetch_rating(player_name)
        f.write(str(currentRating))
        f.close()

    print("Current rank: ", end="")
    print_in_green(str(round(get_file_rank(player_name))))
    print(" " + get_rank_division(get_file_rank(player_name)), end="")
    print()

    print_opponent(player_name)

    print("Waiting for match to end...")
    while True:
        time.sleep(1)
        if os.path.exists(clippiFileLocation):
            print("-------------")
            find_difference(player_name)
            print_opponent(player_name)
            if os.path.exists(clippiFileLocation):
                os.remove(clippiFileLocation)
        # else: 
        #     print("Waiting...")

if __name__ == "__main__":
    main()