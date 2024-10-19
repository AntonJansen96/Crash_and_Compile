#!/usr/bin/env python3

import json

tournament = json.load(open("data/tournament_simplified.json"))

lafcount = 0

for boom in tournament:

    for slag in boom["rounds"]:

        wieSpeeltId = slag["bid"]["highestBidBy"]
        hetbod = slag["bid"]["bid"]

        # Roem
        roem0 = 0
        roem1 = 0
        for hand in slag["playedTricks"]:
            if hand["winner"] in [0, 2]:
                roem0 += hand["honor"]
            else:
                roem1 += hand["honor"]

        roem0 *= 1  # 20 roem -> 20 punten voor spelende team
        roem1 *= 1

        if wieSpeeltId in [0, 2]:  # team 0 (players 0, 2)
            score = slag["wij"] - 0.5 * roem0
            hetbod = hetbod + 0.5 * roem1
        else:                      # team 1 (players 1, 3)
            score = slag["zij"] - 0.5 * roem1
            hetbod = hetbod + 0.5 * roem0

        if score >= hetbod + 10:
            lafcount += 1

print(lafcount)
