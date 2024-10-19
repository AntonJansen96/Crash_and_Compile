#!/usr/bin/env python3

# Using the extra information at your disposal, find the amount of times that a team went wet because of the fame.

import json

tournament = json.load(open("data/tournament_simplified.json"))

count = 0

for boom in tournament:

    for slag in boom["rounds"]:

        if not slag['wet']:
            continue

        wieSpeeltId = slag["bid"]["highestBidBy"]
        hetbod = slag["bid"]["bid"]

        score0 = 0
        score1 = 0
        roem0 = 0
        roem1 = 0

        for idx in range(len(slag["playedTricks"])):

            hand = slag["playedTricks"][idx]

            if hand["winner"] in [0, 2]:
                roem0 += hand["honor"]
                score0 += hand["points"]
                if idx == 7:
                    score0 += 10  # laatste slag is 10 punten extra
            else:
                roem1 += hand["honor"]
                score1 += hand["points"]
                if idx == 7:
                    score1 += 10  # laatste slag is 10 punten extra

        score0 += 0.5 * roem0  # nu hebben we de totale scores herbouwd
        score1 += 0.5 * roem1

        # Roem gaat in de .json file in twintigtallen. Het verwarrende is dat
        # voor de score van de hele slag (voor het tournooi) roem in de volle
        # twintigtallen wordt geteld, maar tijdens de slag zelf, als je zegmaar
        # checkt of je nat bent, maar in tientallen. vandaar dat de daadwerkelijke
        # score = - 0.5 * eigen roem en dat hetbod += 0.5 * vijandige roem.

        if wieSpeeltId in [0, 2]:
            score = score0 - 0.5 * roem0  # daadwerkelijk score
            newbod = hetbod + 0.5 * roem1
        else:
            score = score1 - 0.5 * roem1  # daadwerkelijke score
            newbod = hetbod + 0.5 * roem0

        
        if (score >= hetbod) and (score < newbod):
            print(score, roem0, roem1, hetbod, newbod)
            count += 1

print(count)
