#!/usr/bin/env python3

def formattime(seconds: int) -> str:
    hour = int(seconds / 3600)
    minute = int((seconds - 3600 * hour) / 60)
    second = int(seconds % 60)
    return f"{hour:02d}:{minute:02d}:{second:02d}"

clockArray = []  # Global storing all the clock objects.

class clock:

    def __init__(self, creationtime, speed, number):
        self.number = number       # Clock number.
        self.creationtime = creationtime  # The real time at which this clock was created.
        self.localtime = 0         # The time of this specific clock.
        self.speed = speed         # The relative speed of this clock.
        self.large_prev = 1        # Initial conditions. We set large_prev to 
        self.small_prev = 0        # 1 to prevent infinite clocks at the start.
        self.count = 0             # How often have the hands crossed for this clock?

    def tick(self, realtime):
        """Increment the clock. If hands pass each other, a new clock is spawned at 1/2 speed and added to the clockArray."""

        self.localtime += self.speed                       # increment the local time
        self.large = self.localtime % 3600                 # convert localtime to large-hand position
        self.small = ((1 / 12.0) * self.localtime) % 3600  # convert localtime to small-hand position

        if self.large_prev < self.small_prev and self.large >= self.small:

            # User update
            print(f"{formattime(realtime)} : Clock {self.number} (speed {self.speed}) has hand-crossing localtime {formattime(self.localtime)} -> spawning clock #{len(clockArray)+1} (speed {self.speed * 0.5})")

            # Count the crossing, create a new clock, and append to the clockArray
            self.count += 1
            clockArray.append(clock(creationtime=realtime, speed=0.5*self.speed, number=len(clockArray)+1))

        # Update previous values to current
        self.large_prev = self.large
        self.small_prev = self.small

if __name__ == "__main__":

    # Initialize clockArray with the original Francken clock, running at speed 1.
    clockArray = [clock(creationtime=0, speed=1.0, number=1)]

    for realtime in range(0, 24 * 3600 - 1):  # 0:00:00 to 23:59:59

        for clockobj in clockArray:
            clockobj.tick(realtime)

    # Get the total time
    totalCount = 0
    for clockobj in clockArray:
        totalCount += clockobj.count

    print(totalCount)
    print(len(clockArray) - 1) # -1 because original Francken clock already existed before any crossings.
