from turtle import *

def drawStar(starSize, starColour):
    color(starColour)
    pendown()
    for side in range(5):
        left(144)
        forward(starSize)
    end_fill()
    penup()

bgcolor("MidnightBlue")

penup()
setpos(200, 200)
pendown()

drawStar(50, "White")

hideturtle()
done()
