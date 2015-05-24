import turtle

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow", "green")
    brad.speed(0)
    for i in range(1,37):
        draw_square(brad)
        brad.right(10)
    window.exitonclick()
    
def draw_square(some_turtle):
    i = 0
    while(i<4):
        some_turtle.forward(100)
        some_turtle.right(90)
        i+=1;

draw_art()
