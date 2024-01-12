# created by ymirwani
# This program makes three turtles race, all the turtles have different laziness; the program outputs the winner

from turtle import *
from random import *
import sys

def setup_race(n_turtles, race_length, obstacle_positions):
    ''' Setups a race of length 320 pixels with the given number of racers '''

    # Checks function input
    if n_turtles < 2 or n_turtles > 4:
        print('setup_race: invalid n_turtles, must be 2 <= n_turtles <= 4', file=sys.stderr)
        return None
    
    # Initializes function values
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

    for pos in obstacle_positions:
        draw_obstacle(pos)
    return turtles, race_length

def draw_obstacle(position):
    ''' Draws an obstacle at the given position '''
    penup()
    goto(position)
    pendown()
    color("black")
    begin_fill()
    for _ in range(4):
        forward(20)
        right(90)
    end_fill()
    penup()

def race_round(turtles, laziness_probability, power_ups, obstacle_positions):
    ''' Modified race round to include obstacle encounters '''
    for i in range(len(turtles)):
        turtle = turtles[i]

        # Improved obstacle check
        near_obstacle = False
        for pos in obstacle_positions:
            if abs(turtle.xcor() - pos[0]) < 20 and abs(turtle.ycor() - pos[1]) < 20:
                near_obstacle = True
                break

        if near_obstacle:
            # Turtle slows down but still moves a bit
            turtle.forward(randrange(1, 5))
            continue

        # Existing movement logic
        choice = random()
        if laziness_probability[i] > choice:
            nod(turtle)
        elif power_ups[i] > 0:
            turtle.forward(randrange(16, 31))
            power_ups[i] -= 1
        else:
            turtle.forward(randrange(1, 16))


def nod(t):
    ''' Makes the given turtle instance nod '''
    t.left(45)
    t.right(90)
    t.left(45)

def print_distance(turtles):
    '''writes down the total distance that the turtles have traveled'''
    for turtle in turtles:
        dist = turtle.xcor() + 140
        turtle.write(dist, align="right", font =(15))

def lazy_race(laziness_probability, race_length, obstacle_positions):
    # Draw the racetrack with obstacles
    turtle_names = ['O', 'L', 'E']
    turtles, race_length = setup_race(3, race_length, obstacle_positions)
    finish_line = race_length - 140
    power_ups = [1, 2, 1] # Each turtle has a certain number of power-ups

    # Start the race
    while all(turtle.xcor() < finish_line for turtle in turtles):
        race_round(turtles, laziness_probability, power_ups, obstacle_positions)

    # Find the winner
    for turtle in turtles:
        if turtle.xcor() >= finish_line:
            winner = turtle

    winner_name = turtle_names[turtles.index(winner)]
    print("The winner is:", winner_name)

    done()

    return winner_name


def main():
    #define laziness
    laziness_probability = [0.4, 0.2, 0.3]

    # Randomize race length
    race_length = randint(300, 500)

    # Define obstacle positions
    obstacle_positions = [(randint(-100, 100), y) for y in [100, 70, 40]]

    # Start the race with obstacles
    lazy_race(laziness_probability, race_length, obstacle_positions)

if __name__ == "__main__":
    main()