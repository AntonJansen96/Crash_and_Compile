#!/usr/bin/env python3

import json

tournament = json.load(open("data/tournament_simplified.json"))

lafcount = 0

for boom in tournament:

    for slag in boom["rounds"]:

        if slag["wet"]:
            continue

        score0 = slag["wij"]
        score1 = slag["zij"]
        wieSpeeltId = slag["bid"]["highestBidBy"]
        hetbod = slag["bid"]["bid"]

        roem0 = 0  # Rekening houden met het effect van roem.
        roem1 = 0
        for hand in slag["playedTricks"]:
            if hand["winner"] in [0, 2]:
                roem0 += hand["honor"]
            else:
                roem1 += hand["honor"]

        # Roem gaat in de .json file in twintigtallen. Het verwarrende is dat
        # voor de score van de hele slag (voor het tournooi) roem in de volle
        # twintigtallen wordt geteld, maar tijdens de slag zelf, als je zegmaar
        # checkt of je nat bent, maar in tientallen. vandaar dat de daadwerkelijke
        # score = - 0.5 * eigen roem en dat hetbod += 0.5 * vijandige roem.

        if wieSpeeltId in [0, 2]:
            score = score0 - 0.5 * roem0
            hetbod += 0.5 * roem1
        else:
            score = score1 - 0.5 * roem1
            hetbod += 0.5 * roem0

        if score >= hetbod + 10:
            lafcount += 1

print(lafcount)
