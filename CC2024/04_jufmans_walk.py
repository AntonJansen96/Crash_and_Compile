#!/usr/bin/env python3

from euler import isJuf

# import matplotlib.pyplot as plt
# import os

state = 0
step = 0
xpos, ypos = 0, 0

# xlist = [0]  # only for creating the .gif.
# ylist = [0]

while True:

    if state == 0:
        ypos += 1
    elif state == 1:
        xpos -= 1
    elif state == 2:
        ypos -= 1
    elif state == 3:
        xpos += 1

    step += 1

    if isJuf(step):
        state = (state + 1) % 4

    if abs(xpos) + abs(ypos) == 40:
        print(step)
        break

    # xlist.append(xpos)
    # ylist.append(ypos)
    # plt.plot(xlist, ylist)
    # plt.text(17, 8, f"step = {step:03d}")
    # plt.scatter([0], [0], color="#1f77b4")
    # plt.scatter(xpos, ypos, color="#1f77b4")
    # plt.axis([-10, 25, -25, 10])
    # plt.grid()
    # plt.gca().set_aspect('equal', adjustable='box')
    # plt.savefig(f"{step:03d}_step.png")
    # plt.clf()
    # os.system("convert {0} -trim {0}".format(f"{step:03d}_step.png"))
