import os
from colors import print_in_green, print_in_red
import requests

clippiFileLocation = os.path.expandvars("%HOMEPATH%") + "\\Documents\\clippiFile.txt"
rankFileLocation = os.path.expandvars("%HOMEPATH%") + "\\Documents\\rank.txt"

def data(user):
  return {"operationName":"AccountManagementPageQuery","variables":{"cc":user,"uid":user},"query":"fragment userProfilePage on User {\n  fbUid\n  displayName\n  connectCode {\n    code\n    __typename\n  }\n  status\n  activeSubscription {\n    level\n    hasGiftSub\n    __typename\n  }\n  rankedNetplayProfile {\n    id\n    ratingOrdinal\n    ratingUpdateCount\n    wins\n    losses\n    dailyGlobalPlacement\n    dailyRegionalPlacement\n    continent\n    characters {\n      id\n      character\n      gameCount\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nquery AccountManagementPageQuery($cc: String!, $uid: String!) {\n  getUser(fbUid: $uid) {\n    ...userProfilePage\n    __typename\n  }\n  getConnectCode(code: $cc) {\n    user {\n      ...userProfilePage\n      __typename\n    }\n    __typename\n  }\n}\n"}

def fetch_user(user):
    # Make a request
    return requests.post(
        "https://gql-gateway-dot-slippi.uc.r.appspot.com/graphql",
        json=data(user)
    )

def fetch_rating(user):
    responseJson = fetch_user(user).json()
    return responseJson['data']['getConnectCode']['user']['rankedNetplayProfile']['ratingOrdinal']   

def get_file_rank():
    f = open(rankFileLocation, "r")
    rank = f.read()
    f.close()
    if rank == "":
      rank = fetch_rating()
    return rank

def update_file_rank(rank):
    f = open(rankFileLocation, "w")
    f.write(str(rank))
    f.close()

def find_difference(player_name):
    # Find difference in rank
    newRating = float(fetch_rating(player_name))
    oldRating = float(get_file_rank())
    difference = newRating - oldRating
    
    # Print change in rank
    print("Rating Change: ", end="")
    if difference >= 0:
        print_in_green(str(difference))
    elif difference < 0:
        print_in_red(str(difference))
        
    # Print current rank
    print()
    print("Current rank: ", end="")
    print_in_green(str(fetch_rating()))
    print()
    
    # Update the file
    update_file_rank(newRating)
