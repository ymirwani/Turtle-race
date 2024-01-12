#simulator.py

#This program makes three turtles race, all the turtles have different laziness, the program outputs the winner

from turtle import *
from random import *
import sys
from turtle_GUI import setup_race, swirl, nod, race_round, print_distance

def main():
    laziness_probability = [0.4, 0.2, 0.3]
    turtle_wins = [0, 0, 0]  # initialize list of wins
    turtles, race_length = setup_race(3)

    tracer(0, 0)
    # loop through deez turtles using lazy_race function
    for _ in range(10):
        w_index = simulator(laziness_probability, turtles, race_length) # call modified lazy_race function
        turtle_wins[w_index] += 1 # increment the index
        update()

    turtle_names = ['Sara', 'Luuk', 'Lisa'] # We are now calling this in main in case we want to modify stuff
    for i in range(3):
        print(f"{turtle_names[i]} won {turtle_wins[i]} times")

def simulator(laziness_probability, turtles, race_length):
        # reverse the way we now get the finish_line from the race length
    finish_line = race_length - 140

    while all(turtle.xcor() < finish_line for turtle in turtles):
        race_round(turtles, laziness_probability)

    winner = max(turtles, key=lambda t: t.xcor())
    winner_index = turtles.index(winner)
    
    # Reset turtle back to initial position so we have to subtract 
    for turtle in turtles:
        turtle.penup()
        turtle.goto(-140, turtle.ycor())
        turtle.pendown()

    return winner_index

if __name__ == "__main__":
    main()