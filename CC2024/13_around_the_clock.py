#!/usr/bin/env python3

large_prev = 0  # stores previous large-hand value
small_prev = 0  # stores previous small-hand value

count = 0

for second in range(0, 24 * 3600):  # 0:00:00 to 23:59:59

    large = second % 3600  # position in 10ths of degrees
    small = (1 / 12.0 * second) % 3600  # position in 10ths of degrees

    if (large_prev <= small_prev) and large > small:  # If hands cross
        count += 1

    large_prev = large
    small_prev = small

print(count)
