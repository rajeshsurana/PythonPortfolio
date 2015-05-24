import turtle

def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("red")
    draw_square()
    draw_circle()
    draw_triangle()
    window.exitonclick()
    
def draw_square():
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow", "green")
    brad.speed(2)
    i = 0
    while(i<4):
        brad.forward(100)
        brad.right(90)
        i+=1;
def draw_circle():    
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)

def draw_triangle():
    jenni = turtle.Turtle()
    jenni.shape("arrow")
    jenni.color("black")
    i = 0
    while(i<3):
        jenni.forward(100)
        jenni.right(120)
        i += 1
    

draw_shapes()
