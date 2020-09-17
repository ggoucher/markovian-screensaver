"""
M3, A project by Gerard Goucher using turtle to create a piece of visual art via Markov Chains.
"""

# The following are the python modules I will utilize to create my piece of art
from turtle import *
import random

# General parameters
travelingPoints = []  # these are the points that the turtle can travel to, we'll generate values for this
m_states = 200  # this variable stores the number of possible states for our markov chain.
shape_count = 49
initPoints = []

colors = [(55, 63, 81), (139, 139, 174), (83, 122, 90), (156, 129, 217)]  # generate from coolors.co,
# (charcoal, cool grey, amazon, medium purple
bg_color = (250, 242, 219)  # cornsilk, from coolors.co

# Markov Matrices
movementMarkovs = []  # storage variable that will allow us to store the markov matrix for moving the turtle
colorMarkovs = []  # storage variable that will allow us to store the markov matrix for our colors utilized


def get_points(ptnum):
    """(int)-> null. This function intakes the number of travelingPoints that we desire, and then utilizes the random
    module in order to determine the points we will use for the turtle to travel to."""

    low_lim = -300
    up_lim = 300

    for x in range(ptnum):
        travelingPoints.append([random.randint(low_lim, up_lim), random.randint(low_lim, up_lim)])


def init_states():
    """()-> null. This function merely takes our M possible states, and creates an initial state array where
    every state is equally probable."""

    equal_pr = 1/m_states
    for i in range(m_states):
        initPoints.append(equal_pr)


def get_movement_markovs():
    """()-> null. This function takes our travelingPoints matrix, and then uses its length in order to determine
    the size of the mxm Markov matrix. From here, we use the random module to create random terms 1 -> 100, sum and
    divide them, then add to the resultant array to our movementMarkov matrix."""

    pts_len = len(travelingPoints)  # lets us know how many rows we have to generate

    for x in range(pts_len):  # creates our MxM markov matrix
        row_vals = []  # used as a temporary placeholder array for randomly generated values 1 -> 100.
        row_probs = []  # contains all of the state transition probability values for the mi term
        upper_lim = 100

        for y in range(pts_len):  # for loop creating our randomly generated values
            stored_val = random.uniform(1, upper_lim)
            row_vals.append(stored_val)

        sum_vals = sum(row_vals)  # used for dividing each term  in the row_vals array
        for z in row_vals:  # for loop adding values to the row_probs array, which will sum to 1.
            row_probs.append(z / sum_vals)
        movementMarkovs.append(row_probs)


def initial_turtle_movement():
    """()-> null. This function initiates our turtle, setting its first state and travelling there"""

    colormode(255)
    bgcolor(bg_color)
    hideturtle()  # for visual purposes
    color(bg_color)  # initializing the color we want
    width(5)


def create_rect(loc1, loc2):
    """(arr, arr)->null. This function makes a square between two different rectangles. It first travels on the x plane,
    and then travels on the y plane to the new point. it closes this by traveling back on the x plane, and then the y
    plane, closing the rectangle and filling it."""

    color(random.choices(colors, [.25, .25, .25, .25], k=1)[0])

    pendown()
    goto(loc2[0], loc1[1])
    goto(loc2[0], loc2[1])
    goto(loc1[0], loc2[1])
    goto(loc1[0], loc1[1])
    penup()


def creation_loop(s_start):
    """(arr)->none. This function serves as a looper to create rectangles and assign new positions to goto using
    the random python module. """

    count = 0

    while count <= shape_count:
        if count % 10 == 0:  # so that the screen doesn't get too busy
            clear()
        s_next = random.choices(travelingPoints, initPoints, k=1)  # the next point we will use to illustrate
        create_rect(s_start, s_next[0])

        s_start = random.choices(travelingPoints, initPoints, k=1)[0]  # giving us a new point to create a shape from
        goto(s_start[0], s_start[1])
        count += 1


def main_turtle():
    """null->null. Combines all of our turtle movement functions to create a final output. Additionally,
    specifies our starting state using random choices, then starts our creation loop."""

    initial_turtle_movement()

    s_o = random.choices(travelingPoints, initPoints, k=1)  # finding the S_o point we're going to start from
    penup()
    goto(s_o[0][0], s_o[0][1])

    s_start = [s_o[0][0], s_o[0][1]]  # the inital point to draw a rectangle from, reassigned in the creation loop
    creation_loop(s_start)

    done()


get_points(m_states)
get_movement_markovs()
init_states()
main_turtle()
