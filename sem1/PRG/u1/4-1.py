import turtle

from math import sqrt
for i in range(4):
    turtle.backward(90)
    turtle.left(90)
turtle.right(45)
turtle.backward(45*sqrt(2))
turtle.right(270)
turtle.backward(45*sqrt(2))
turtle.setpos(0, 0)
turtle.settiltangle(90)
turtle.backward(90*sqrt(2))
turtle.setpos(-90, 0)
turtle.left(90)
turtle.backward(90*sqrt(2))
# turtle.reset()
turtle.exitonclick()

