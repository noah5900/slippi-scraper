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

    print("Starting rank: ", end="")
    print_in_green(str(get_file_rank()))
    print(" " + get_rank_division(get_file_rank()), end="")
    print()

    print_opponent()

    print("Waiting for match to end...")
    while True:
        time.sleep(1)
        if os.path.exists(clippiFileLocation):
            print("-------------")
            find_difference(player_name)
            print_opponent()
            os.remove(clippiFileLocation)
        # else: 
        #     print("Waiting...")

if __name__ == "__main__":
    main()