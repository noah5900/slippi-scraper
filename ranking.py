from colorama import Fore, Style

def get_rank_division(rating):
  rating = float(rating)
  if rating >= 2350:
    return Fore.MAGENTA + "Master 3" + Style.RESET_ALL
  elif rating >= 2275:
    return Fore.MAGENTA + "Master 2" + Style.RESET_ALL
  elif rating >= 2191.75:
    return Fore.MAGENTA + "Master 1" + Style.RESET_ALL
  elif rating >= 2136.28:
    return Fore.BLUE + "Diamond 3" + Style.RESET_ALL
  elif rating >= 2073.67:
    return Fore.BLUE + "Diamond 2" + Style.RESET_ALL
  elif rating >= 2003.92:
    return Fore.BLUE + "Diamond 1" + Style.RESET_ALL
  elif rating >= 1927.03:
    return Fore.CYAN + "Platinum 3" + Style.RESET_ALL
  elif rating >= 1843.00:
    return Fore.CYAN + "Platinum 2" + Style.RESET_ALL
  elif rating >= 1751.83:
    return Fore.CYAN + "Platinum 1" + Style.RESET_ALL
  elif rating >= 1653.52:
    return Fore.YELLOW + "Gold 3" + Style.RESET_ALL
  elif rating >= 1548.07:
    return Fore.YELLOW + "Gold 2" + Style.RESET_ALL
  elif rating >= 1435.48:
    return Fore.YELLOW + "Gold 1" + Style.RESET_ALL
  elif rating >= 1315.75:
    return Fore.LIGHTBLACK_EX + "Silver 3" + Style.RESET_ALL
  elif rating >= 1188.88:
    return Fore.LIGHTBLACK_EX + "Silver 2" + Style.RESET_ALL
  elif rating >= 1054.87:
    return Fore.LIGHTBLACK_EX + "Silver 1" + Style.RESET_ALL
  elif rating >= 913.72:
    return Fore.BROWN + "Bronze 3" + Style.RESET_ALL
  elif rating >= 765.43:
    return Fore.BROWN + "Bronze 2" + Style.RESET_ALL
  else:
    return Fore.BROWN + "Bronze 1" + Style.RESET_ALL