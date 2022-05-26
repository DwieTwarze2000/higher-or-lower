import os
from random import randint


logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""
vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

def main():
    streamers = getStreamers()
    points = 0
    streamerA = ""
    while True:
        os.system("cls")
        print(logo)

        print("You have {} points".format(points))

        if streamerA == "":
            streamerA = streamers[randint(0, len(streamers)-1)]

        print("Compare A: {}, {} streamer, mostly streaming {}".format(streamerA["name"], streamerA["language"], streamerA["category"]))

        print(vs)

        streamerB = streamers[randint(0, len(streamers)-1)]
        print("Against B: {}, {} streamer, mostly streaming {}".format(streamerB["name"], streamerB["language"], streamerB["category"]))

        compare = input("Who has more followers? type 'A' or 'B': ")

        Userchoice = streamerA if compare == "A" else streamerB

        if streamerA["followers"] > streamerB["followers"]:
            winner = streamerA
        elif streamerA["followers"] < streamerB["followers"]:
            winner = streamerB
        else:
            winner = "both"

        if winner == "both" or winner == Userchoice:
            points +=1
            streamerA = Userchoice
        else:
            os.system("cls")
            print(logo)
            print("YOU LOST! Your points: {}".format(points))
            break



def getStreamers():
    dir = os.path.join( os.path.dirname( __file__ ), '..' )

    streamersData = []
    with open(f"{dir}/TwitchDataSet.csv", encoding="UTF-8") as file:
        
        for line in file:
            streamer = {}
            words = line.split(",")
            streamer["name"] = words[2]
            streamer["followers"] = words[7]
            streamer["language"] = words[12]
            streamer["category"] = words[14]        
            streamersData.append(streamer)
        streamersData.pop(0)
    return streamersData

main()
