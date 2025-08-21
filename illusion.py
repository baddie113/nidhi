import turtle

my_wn = turtle.Screen()
my_wn.bgcolor("lavender")
my_wn.title("Turtle Circles")

my_pen = turtle.Turtle()
size = 0

while True:
    my_pen.circle(size + 1)
    size = size - 5
    size = size + 1 
    

turtle.done()