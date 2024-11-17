import turtle
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(300,400)
square=turtle.Turtle()
side=4
side_length=70
angle=360.0/side
for i in range(side):
    square.forward(side_length)
    square.right(angle)
turtle.done()