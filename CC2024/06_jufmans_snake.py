#!/usr/bin/env python3


def isJuf(num: int) -> bool:

    def isPalindrome(num: int) -> bool:

        stringnum = str(num)
        return stringnum[::-1] == stringnum

    a = num % 7 == 0
    b = "7" in str(num)
    c = num > 10 and isPalindrome(num)

    if a and b and c:
        return 3

    elif (a and b) or (a and c) or (b and c):
        return 2

    elif a or b or c:
        return 1

    return 0


step = 0
xpos, ypos = 0, 0
direction = 0
visited = []  # To keep track of visited positions
revisits = 0  # To keep track of visited positions

while True:

    if direction == 0:
        ypos += 1
    elif direction == 1:
        xpos -= 1
    elif direction == 2:
        ypos -= 1
    elif direction == 3:
        xpos += 1

    step += 1

    if (xpos, ypos) in visited:
        revisits += 1

        if revisits == 1210:
            print(step)
            break
    else:
        visited.append((xpos, ypos))

    # Check if it's single (1), double (2) or triple juf (3), or not at all (0).
    jufVal = isJuf(step)

    # Change direction depending on how many juf it is...
    if jufVal == 1:
        direction = (direction + 1) % 4  # go left...

    elif jufVal == 2:
        direction = (direction - 1) % 4  # go right...

    elif jufVal == 3:
        direction = (direction + 2) % 4  # reverse...
