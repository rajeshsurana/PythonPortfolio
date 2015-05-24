import turtle

def draw_rhombus(some_turtle):
    for i in range(1,3):
        some_turtle.forward(50)
        some_turtle.right(30)
        some_turtle.forward(50)
        some_turtle.right(150)


def draw_flower():
    window = turtle.Screen()
    window.bgcolor("white")
    brad = turtle.Turtle()
    brad.shape("classic")
    brad.color("blue")
    brad.speed(0)
    for i in range(1,73):
        draw_rhombus(brad)
        brad.right(5)
    brad.right(90)
    brad.forward(200)
    window.exitonclick()

draw_flower()
