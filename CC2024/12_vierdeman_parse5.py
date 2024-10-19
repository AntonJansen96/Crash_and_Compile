#!/usr/bin/env python3

import json

tournament = json.load(open("data/tournament_simplified.json"))

count = 0

for boom in tournament:

    for slag in boom["rounds"]:

        if not slag["wet"]:
            continue

        wieSpeeltId = slag["bid"]["highestBidBy"]
        bod_origineel = slag["bid"]["bid"]

        score0, score1 = 0, 0
        roem0, roem1 = 0, 0

        # Herbouw de score en vind de roem door door de handen heen te loopen.
        for idx in range(len(slag["playedTricks"])):

            hand = slag["playedTricks"][idx]

            if hand["winner"] in [0, 2]:
                roem0 += hand["honor"]
                score0 += hand["points"]
                if idx == 7:
                    score0 += 10  # Laatste slag is 10 punten extra.
            else:
                roem1 += hand["honor"]
                score1 += hand["points"]
                if idx == 7:
                    score1 += 10  # Laatste slag is 10 punten extra.

        if wieSpeeltId in [0, 2]:
            score = score0
            bod_nieuw = bod_origineel + 0.5 * roem1
        else:
            score = score1
            bod_nieuw = bod_origineel + 0.5 * roem0

        if (score >= bod_origineel) and (score < bod_nieuw):
            count += 1

print(count)
