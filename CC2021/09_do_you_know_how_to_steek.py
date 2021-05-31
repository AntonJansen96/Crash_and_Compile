#!/bin/python3

# While everybody is monopolizing the streets, you have been busy practicing you
# klaverjas cheating skills. You have a deck of 32 cards for a game of klaverjas
# and managed to place the four aces on top. You've perfected the art of perfect
# cuts and shuffles, and set out to construct a system that allows you to deal all
# aces back to your own team. Starting and ending with a perfect cut in the middle
# of the deck you execute 1 to 11 of the following shuffles:
# riffle shuffle - 1 2 3 4 5 6 -> 1 4 2 5 3 6, 
# monge shuffle - 1 2 3 4 5 6 -> 6 4 2 1 3 5, 
# sake shuffle - 1 2 3 4 5 6 -> 3 2 1 6 5 4,
# peel shuffle - 1 2 3 4 5 6 -> 3 4 2 5 1 6. 
# What fraction of these shuffles will result in all aces being dealt to your
# team? Note that the cards are dealt as 3,3,3,3,2,2,2,2,3,3,3,3, you start with
# the player left of you, and your team mate is opposite of you.

# Perfect cut in the middle of the deck.
def cut(deck):
    return deck[16:] + deck[0:16]

# riffle shuffle - 1 2 3 4 5 6 -> 1 4 2 5 3 6
def riffle(deck):
    newdeck = []
    for idx in range(0, 16):
        newdeck += [deck[idx], deck[idx + 16]]
    return newdeck

# monge shuffle - 1 2 3 4 5 6 -> 6 4 2 1 3 5
def mongle(deck):
    return [deck[idx] for idx in range(0, 32) if idx % 2 == 1][::-1] + \
           [deck[idx] for idx in range(0, 32) if idx % 2 == 0]

# sake shuffle - 1 2 3 4 5 6 -> 3 2 1 6 5 4
def sake(deck):
    return deck[0:16][::-1] + deck[16:][::-1]

# peel shuffle - 1 2 3 4 5 6 -> 3 4 2 5 1 6
def peel(deck):
    a = 15
    b = 16
    newdeck = []
    while (b != len(deck)):
        newdeck += [deck[a], deck[b]]
        a -= 1
        b += 1
    return newdeck

# Deal cards (3,3,3,3, 2,2,2,2, 3,3,3,3)
# These are the cards that we get (other team gets deck[0:3] + deck[6:9] +
# deck[12:14] + deck[16:18] + deck[20:23] + deck[26:29]).
def deal(deck):
    return deck[3:6] + deck[9:12] + deck[14:16] + deck[18:20] + deck[23:26] + deck[29:32]

# Perform shuffles and check whether this leads to us having the four aces.
def checkTheShuffle(startdeck, shuffleList):
    deck = startdeck

    for idx in shuffleList:
        deck = {0 : riffle, 1 : mongle, 2 : sake, 3: peel}[idx](deck)

    deck = cut(deck)                # End with a cut.

    if (sum(deal(deck)) == 4):      # Deal and check.
        return True
    
    return False

################################################################################

# We start with four aces (1) on top. order of other (0) cards does not matter.
startdeck = 4 * [1] + 28 * [0]

# We always start with a cut (in the same starting deck) so take outside of loop.
startdeck = cut(startdeck)

total = 0
count = 0

for a in range(0, 4):
    if (checkTheShuffle(startdeck, [a])):
        count += 1
    total += 1

    for b in range(0, 4):
        if (checkTheShuffle(startdeck, [a, b])):
            count += 1
        total += 1

        for c in range(0, 4):
            if (checkTheShuffle(startdeck, [a, b, c])):
                count += 1
            total += 1

            for d in range(0, 4):
                if (checkTheShuffle(startdeck, [a, b, c, d])):
                    count += 1
                total += 1

                for e in range(0, 4):
                    if (checkTheShuffle(startdeck, [a, b, c, d, e])):
                        count += 1
                    total += 1

                    for f in range(0, 4):
                        if (checkTheShuffle(startdeck, [a, b, c, d, e, f])):
                            count += 1
                        total += 1

                        for g in range(0, 4):
                            if (checkTheShuffle(startdeck, [a, b, c, d, e, f, g])):
                                count += 1
                            total += 1

                            for h in range(0, 4):
                                if (checkTheShuffle(startdeck, [a, b, c, d, e, f, g, h])):
                                    count += 1
                                total += 1

                                for i in range(0, 4):
                                    if (checkTheShuffle(startdeck, [a, b, c, d, e, f, g, h, i])):
                                        count += 1
                                    total += 1

                                    for j in range(0, 4):
                                        if (checkTheShuffle(startdeck, [a, b, c, d, e, f, g, h, i, j])):
                                            count += 1
                                        total += 1

                                        for k in range(0, 4):
                                            if (checkTheShuffle(startdeck, [a, b, c, d, e, f, g, h, i, j, k])):
                                                count += 1
                                            total += 1

print(count, total, count / float(total))

# 86222 5592404 0.015417698721337013
# ~2m
