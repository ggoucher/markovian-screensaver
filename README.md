<h1>A Markovian Screensaver</h1>
<h3>A project by Gerard Goucher 🧚</h3>

This project uses turtle to create a "screen saver" style form of visual art, drawing on 
my favorite colors and geometric inspiration from Piet Mondrian. Markov Chains are used throughout
to probabilistically determine the next created rectangle on the screen. 

<h4>Setting up the code</h4>

My project relies on the Turtle and Random modules, which both come pre-packaged
with Python distributions, so just make sure that you have Python version 3.7
or later installed. 

Then, simply run the m3.py script using whatever method you prefer, though I used the 
PyCharm IDE. If you wish to run this using the command line, navigate to the markovian-screensaver
folder in your directory after downloading from GitHub and run the following command:

    $ python3 m3.py

<h2>Personal Meaning</h2>

I've always enjoyed being in and around art museums, and am particularly familiar with 
the Philadelphia Museum of Art. In it, I've found that I really appreciate 
geometrically satisfying pieces, particularly the work of Piet Mondrian, a storied Dutch artist.

When I started approaching this project, I considered one of the highlights of my Intro to CS class,
where we were able to play with the Turtle Graphics module. Combining these two interests,
I considered using turtle as a vehicle to create satisfying geometry with dimensions determined
by Markov Chains. Turtle lends itself very well to creating rectangles, so it 
was a great match. 

As I progressed through the project, I began to choose colors with equal probability for my program to color the 
rectangles. The colors I chose are my comfort colors, they make me feel cozy and happy. 
I initially intended to just output final pictures, however I noticed how enjoyable it 
was to watch my output as it was drawn in by turtle. 

Ultimately, I saw potential for a Mondrian inspired, comfort color, screen saver created using
Markov Chains. I find the results soothing and aesthetically pleasing, and I hope you do, too! 

<h2>Personal Challenge</h2>

The most challenging aspect of this project was determining how to create the markov probabilities
in Python, and the best way to implement state transitions. This is where I decided to use
the random module, a tool that I'm pretty unfamiliar with. By randomly generating Markov matrix row 
probabilities, I was able to create a transition matrix that ensured most transitions would create great
new shapes, and that the final product would fill the screen before being cleared. This way,
each "screen saver" outputted is unique, and visually coherent. Beyond this, I used the random module to generate 
the points on the coordinate plane that we could travel to, as well.

Once all my probabilities and points were generated, I worked on figuring out the best
way to probabilitiscally choose the next points to transition to. This is where I toyed with the Random
 module again, using the ```random.choices()``` method to apply my generated probabilities to my possible transition
 points. By doing a bit of conceptual work up front, the rest of the code was pretty simple
to put together in terms of graphical work. 

<h2>Creativity</h2>

I believe that the system is creative because it well synthesizes a variety of my interests artistically
and is designed with creative intention to create an original product. It is more of a combinatorial 
form of creativity - I am considering my favorite colors, one of my favorite artsts, and screen savers, combining
them into an original idea. 

<h2>Sources</h2>

Conversed with Kayla Snyder and Tenzin Choezin about project parameters and ideas. 

[Python Random Module Documentation](https://docs.python.org/3/library/random.html)

[Python Turtle Module Documentation](https://docs.python.org/3/library/turtle.html)

[Coolors Color Generator](https://coolors.co/)

[Coding Probabilitiy Summation Resource](https://stackoverflow.com/questions/18659858/generating-a-list-of-random-numbers-summing-to-1),
used to determine how to ensure that randomly generated probabilities have a row sum of 1. 