#!/usr/bin/env python3

import json

tournament = json.load(open("data/tournament_simplified.json"))

lafcount = 0

for boom in tournament:

    for slag in boom["rounds"]:

        score0 = slag["wij"]  # team 0 (players 0, 2)
        score1 = slag["zij"]  # team 1 (players 1, 3)

        wieSpeeltId = slag["bid"]["highestBidBy"]
        
        # Roem

        
        hetbod = slag["bid"]["bid"]

        if wieSpeeltId in [0, 2]:  # team 0
            score = score0
        else:                      # team 1
            score = score1

        if score >= hetbod + 10:
            lafcount += 1

print(lafcount)
