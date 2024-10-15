#!/usr/bin/env python3

count = 0

with open("data/klaverjas-handjes.txt") as file:

    hand = []  # Contains all lines of one hand.

    for line in file.read().splitlines():  # Loop through lines one by one

        if "---" in line:

            # Ignore situations where all four players pass
            while hand[0:4] == ["Pass", "Pass", "Pass", "Pass"]:
                hand = hand[4:]

            # Get the bid BEFORE we see three consecutive Pass
            for idx in range(0, len(hand) - 3):
                if (
                    hand[idx + 1] == "Pass"
                    and hand[idx + 2] == "Pass"
                    and hand[idx + 3] == "Pass"
                ):
                    thebid = hand[idx]
                    break

            if not "SANS" in thebid:  # Ignore SANS
                trump = thebid[-1]  # The trump suit is the last letter of this bid

                if trump in hand[-1]:  # If the trump letter
                    count += 1  # is in the last slag, we count.

            hand.clear()  # clear the hand list (if line contains ---).

        else:
            hand.append(line)

print(count)
