import math
def star(k):
    import turtle
    turtle.shape("turtle")
    turtle.color("Blue")
    turtle.begin_fill()
    for i in range(9):
        turtle.forward(k)
        turtle.right(100)
        turtle.forward(k)
        turtle.left(140)
    turtle.exitonclick()
print(star(30))
