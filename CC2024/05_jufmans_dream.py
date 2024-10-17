#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.transform import Rotation as R


def isJuf(num: int) -> int:

    def isPalindrome(num: int) -> bool:
        stringnum = str(num)
        return stringnum[::-1] == stringnum

    if num <= 0:
        return 0

    a = num % 7 == 0
    b = "7" in str(num)
    c = num > 10 and isPalindrome(num)

    if (a and b) or (a and c) or (b and c):
        return 2

    elif a or b or c:
        return 1

    return 0


def plotBeforeAfer(orig, rot) -> None:
    """Plots object's original and rotated coordinates for a visual comparison."""

    fig = plt.figure(figsize=(12, 6))

    ax1 = fig.add_subplot(121, projection="3d")
    ax1.scatter(orig[:-1, 0], orig[:-1, 1], orig[:-1, 2], c="r", marker="o")
    ax1.scatter(orig[-1:, 0], orig[-1:, 1], orig[-1:, 2], c="b", marker="o")
    ax1.set_title("Original")

    ax2 = fig.add_subplot(122, projection="3d")
    ax2.scatter(rot[:-1, 0], rot[:-1, 1], rot[:-1, 2], c="r", marker="o")
    ax2.scatter(rot[-1:, 0], rot[-1:, 1], rot[-1:, 2], c="b", marker="o")
    ax2.set_title("Rotated")

    for ax in [ax1, ax2]:
        ax.plot([-2, 2], [0, 0], [0, 0], "k--")  # X-axis
        ax.plot([0, 0], [-2, 2], [0, 0], "k--")  # Y-axis
        ax.plot([0, 0], [0, 0], [-2, 2], "k--")  # Z-axis
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")
        ax.set_xlim([-2, 2])
        ax.set_ylim([-2, 2])
        ax.set_zlim([-2, 2])

    plt.show()


def getDirection(coords):
    """Obtain the direction vector in which the rectangle's 'nose' is pointing."""
    nose = coords[-2]
    com = coords[-1]
    dir = nose - com
    dir /= np.linalg.norm(dir)
    return np.round(dir).astype(int)


if __name__ == "__main__":

    person = np.array(
        [
            [-0.5, -0.5, -1.0],
            [-0.5, 0.5, -1.0],
            [0.5, -0.5, -1.0],
            [0.5, 0.5, -1.0],
            [-0.5, -0.5, 1.0],
            [-0.5, 0.5, 1.0],
            [0.5, -0.5, 1.0],
            [0.5, 0.5, 1.0],
            [-0.1, 0.5, 0.5],  # eye point (for debug)
            [0.1, 0.5, 0.5],  # eye point (for debug)
            [0.0, 0.5, 0.0],  # nose point -> used in getting the direction
            [0.0, 0.0, 0.0],  # COM point -> represents position
        ]
    )

    # Initial conditions
    rotated = person
    orientation = R.from_euler("xyz", [0, 0, 0], degrees=True)  # Initial orientation.
    pos = np.array([0, 0, 0])  # Initial position (== person[-1]).

    # Main loop
    for step in range(1, 10000):

        pos += getDirection(rotated)

        jufVal = isJuf(step)

        if jufVal == 1:
            orientation *= R.from_euler("z", [np.pi / 2])
            rotated = orientation.apply(person)

        elif jufVal == 2:
            orientation *= R.from_euler("x", [np.pi / 2])
            rotated = orientation.apply(person)

        if abs(pos[0]) + abs(pos[1]) + abs(pos[2]) == 40:
            print(step, pos)
            break
