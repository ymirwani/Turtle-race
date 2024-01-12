# created by ymirwani
# This program makes three turtles race, all the turtles have different laziness; the program outputs the winner

from turtle import *
from random import *
import sys

def setup_race(n_turtles):
    ''' Setups a race of length 320 pixels with the given number of racers '''

    # Checks function input
    if n_turtles < 2 or n_turtles > 4:
        print('setup_race: invalid n_turtles, must be 2 <= n_turtles <= 4', file=sys.stderr)
        return None
    
    # Initializes function values
    race_length = 320
    n_gaps = 8
    gap_dist = race_length/n_gaps
    speed(10)
    
    # Go to starting location
    penup()
    x_loc_start = -140
    goto(x_loc_start, 140)

    # Draw race lines
    for step in range(n_gaps+1):
        write(step, align='center')
        right(90)
        for num in range(8):
            penup()
            forward(10)
            pendown()
            forward(10)
        penup()
        backward(160)
        left(90)
        forward(gap_dist)
    hideturtle()

    # Create and place turtles
    colors = ['red', 'blue', 'orange', 'green']
    y_loc = [100, 70, 40, 10]
    turtles = []
    for i in range(n_turtles):
        turtles.append(Turtle())
        turtles[i].color(colors[i])
        turtles[i].shape('turtle')

        turtles[i].penup()
        turtles[i].goto(x_loc_start, y_loc[i])
        turtles[i].pendown()
        swirl(turtles[i])
    
    return turtles, race_length