from turtle import * #import the library of commands that you'd like to use

colormode(255)

# Create a panel to draw on. 
panel = Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = 'Bezos.gif'
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

Turtle()
up()
# mustache
goto(23,60) 
left(140)
width(6)
down() # begin drawing mustache left
begin_fill()
forward(25)
left(80)
forward(55)
right(205)
forward(67)
left(42) # begin drawing mustache right
forward(23)
right(97)
forward(40)
right(147)
forward(47)
end_fill()

# laser eyes
up()
color("red")
goto(40,122)
left(146)
width(3)
down() # begin drawing laser right
forward(750)
up()
goto(-16,111)
right(20) # being drawing mustache left
down()
forward(700)
up()

# LOL
LETTERS = int(3) # how many letters in LOLOL
width(8)
RUN = 1
goto(-325,80)
color("black")
left(150)
for iteration in range (LETTERS): # alternates between drawing L's and O's in a line
    if RUN == 1: # draws the L
        forward (50)
        down()
        left(180)
        forward(50)
        left(90)
        forward(25)
        up()
        forward(30)
        RUN = (RUN-1)
    else: # draws the O
        down()
        circle(25)
        up()
        forward(45)
        left(90)
        RUN = (RUN+1)
    
done()

# Since this is PC-02 the code is pretty limiting on what can be simplified. But I enjoyed the idea of the LOL next to Bezos's head, so I decided that automating that process would
# allow you to change the length of how long the LOL was which could be fun. I modified the original code to now include a for loop with an imbedded if else statement that will
# alternate drawing L's and O's for however many letters are put in. I think this addition does slightly simplify the code, and is a fun addition.
