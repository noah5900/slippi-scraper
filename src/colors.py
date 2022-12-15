def print_in_green(s):
  s = str(s)
  print("\033[92m" + s + "\033[0m", end="")

def print_in_red(s):
  s = str(s)
  print("\033[91m" + s + "\033[0m", end="")