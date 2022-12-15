import os
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

def fetch_win_loss(user):
    responseJson = fetch_user(user).json()
    netplayProfile = responseJson['data']['getConnectCode']['user']['rankedNetplayProfile']

    # Extract the wins, losses, and ratingUpdateCount values
    wins = netplayProfile["wins"]
    losses = netplayProfile["losses"]
    rating_update_count = netplayProfile["ratingUpdateCount"]

    # Create a tuple containing the extracted values
    results = (wins, losses, rating_update_count)
    
    return results

def get_file_rank(player_name):
    f = open(rankFileLocation, "r")
    rank = f.read()
    f.close()
    if rank == "":
      rank = fetch_rating(player_name)
      update_file_rank(rank)
    return float(rank)

def update_file_rank(rank):
    f = open(rankFileLocation, "w")
    f.write(rank)
    f.close()

