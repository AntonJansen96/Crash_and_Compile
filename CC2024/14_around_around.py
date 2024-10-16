#!/usr/bin/env python3


def formattime(seconds: int) -> str:
    hour = int(seconds / 3600)
    minute = int((seconds - 3600 * hour) / 60)
    second = int(seconds % 60)
    return f"{hour:02d}:{minute:02d}:{second:02d}"


clockArray = []  # Global storing all the clock objects.


class clock:

    def __init__(self, number, time, speed):
        self.number = number  # Clock number (for debugging/update purposes).
        self.creationtime = time  # The real time at which this clock was created.
        self.speed = speed  # The relative speed of this clock.
        self.large_prev = 1  # Initial conditions. We set large_prev to
        self.small_prev = 0  # 1 to prevent infinite clocks at the start.

    def tick(self, realtime):
        """Increment the clock. If hands pass each other, a new clock is spawned at 1/2 speed and added to the clockArray."""

        # The local time on this clock is the real time - the clock's (real),
        # creation time, multiplied by the speed factor.
        localtime = (realtime - self.creationtime) * self.speed

        self.large = localtime % 3600  # Convert time to large-hand pos.
        self.small = 1 / 12.0 * localtime % 3600  # Convert time to small-hand pos.

        if self.large_prev < self.small_prev and self.large >= self.small:

            # User update
            print(
                f"{formattime(realtime)} : Clock #{self.number} (speed {self.speed}) has a hand-crossing at localtime {formattime(localtime)} -> spawning clock #{len(clockArray)+1} (speed {self.speed * 0.5})"
            )

            # Append new clock (running at 1/2 this clock's speed) to the clockArray.
            clockArray.append(clock(len(clockArray) + 1, realtime, 0.5 * self.speed))

        # Update previous hand-position values to current.
        self.large_prev, self.small_prev = self.large, self.small


# Initialize clockArray with the original Francken clock, running at speed 1.
clockArray = [clock(number=1, time=0, speed=1)]

for realtime in range(0, 24 * 3600):  # 0:00:00 to 23:59:59
    for clockobj in clockArray:
        clockobj.tick(realtime)

# Every time we have a crossing a new clock gets created. So the solution
# is simply len(clockArray) - 1, to account for original Francken clock.
print(len(clockArray) - 1)
