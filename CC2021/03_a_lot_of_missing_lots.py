#!/bin/python3

# There is nothing like having to wait for the other players during a game of 
# monopoly, to find ways of passing time. One way is to play out all possible 
# games of tic-tac-toe on graph paper, but after having contemplated this, we 
# will save you the trouble. Graph paper can be used for other things than playing 
# tic-tac-toe. One can also use the graph paper to draw squares. The obvious squares
# follow the lines on the paper, and will end up having areas of 1, 4, 9, 16 graph 
# paper blocks. One can also obtain a square with an area of 5 blocks, by drawing it
# under an angle. To do this, start at any block's corner and move 2 blocks to the
# right and 1 up, connect this corner with the initial one and finish the square. 
# If you do the calculation you will see this square has an area of 5 (blocks).
# After playing around a bit, you might notice that it is impossible to obtain a 
# square with an area of 6 blocks, that also fits nicely on the graph paper. What
# is the sum of all impossible areas under 10000?

impossibles = 10000 * [1]

for a in range(1, 100):
    for b in range(0, 100):
        area = a**2 + b**2
            
        if (area >= 10000):
            break
        
        impossibles[area] = 0

total = 0
for num in range(1, 10000):
    if impossibles[num] == 1:
        total += num

print(total)
