from colorama import Fore, Style

ranks = {
  "Master 3": 2350,
  "Master 2": 2275,
  "Master 1": 2191.75,
  "Diamond 3": 2136.28,
  "Diamond 2": 2073.67,
  "Diamond 1": 2003.92,
  "Platinum 3": 1927.03,
  "Platinum 2": 1843.00,
  "Platinum 1": 1751.83,
  "Gold 3": 1653.52,
  "Gold 2": 1548.07,
  "Gold 1": 1435.48,
  "Silver 3": 1315.75,
  "Silver 2": 1188.88,
  "Silver 1": 1054.87,
  "Bronze 3": 913.72,
  "Bronze 2": 765.43,
  "Bronze 1": 0
}

ranksWithColour = {
  Fore.MAGENTA + "Master 3" + Style.RESET_ALL: 2350,
  Fore.MAGENTA + "Master 2" + Style.RESET_ALL: 2275,
  Fore.MAGENTA + "Master 1" + Style.RESET_ALL: 2191.75,
  Fore.BLUE + "Diamond 3" + Style.RESET_ALL: 2136.28,
  Fore.BLUE + "Diamond 2" + Style.RESET_ALL: 2073.67,
  Fore.BLUE + "Diamond 1" + Style.RESET_ALL: 2003.92,
  Fore.CYAN + "Platinum 3" + Style.RESET_ALL: 1927.03,
  Fore.CYAN + "Platinum 2" + Style.RESET_ALL: 1843.00,
  Fore.CYAN + "Platinum 1" + Style.RESET_ALL: 1751.83,
  Fore.YELLOW + "Gold 3" + Style.RESET_ALL: 1653.52,
  Fore.YELLOW + "Gold 2" + Style.RESET_ALL: 1548.07,
  Fore.YELLOW + "Gold 1" + Style.RESET_ALL: 1435.48,
  Fore.LIGHTBLACK_EX + "Silver 3" + Style.RESET_ALL: 1315.75,
  Fore.LIGHTBLACK_EX + "Silver 2" + Style.RESET_ALL: 1188.88,
  Fore.LIGHTBLACK_EX + "Silver 1" + Style.RESET_ALL: 1054.87,
  "\033[31mBronze 3\033[0m": 913.72,
  "\033[31mBronze 2\033[0m": 765.43,
  "\033[31mBronze 1\033[0m": 0
}

def get_rank_division(rating):
  for rank, value in ranksWithColour.items():
    if rating >= value:
      return rank

def print_rating_to_next_rank(rating):
  next_rank = None
  rating_difference = None
  for rank, value in ranks.items():
    if value >= rating:
      next_rank = rank
      rating_difference = value - rating
      
  print("Rating required to reach " + next_rank + ": " + str(round(rating_difference)))
