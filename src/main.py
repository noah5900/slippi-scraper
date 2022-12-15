from time import time
import time
import os
from rating import *
from replay import post_game_summary

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

    post_game_summary(player_name)
    
    print("Waiting for match to end...")
    while True:
        time.sleep(1)
        if os.path.exists(clippiFileLocation):
            print("-------------")
            post_game_summary(player_name)
            if os.path.exists(clippiFileLocation):
                os.remove(clippiFileLocation)
        # else: 
        #     print("Waiting...")

if __name__ == "__main__":
    main()