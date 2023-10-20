#Pranjal Aggarwal
#20/october/2023
import turtle

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor('white')

t.right(90)

# Define a list of colors for a rainbow effect
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
t.speed(10)
def spiral(length, times, t):
    if times < 360:
        # Change the pen color based on the current step in the spiral
        color_index = times % len(colors)
        t.color(colors[color_index])

        t.forward(length)
        t.right(40)
        times += 1
        spiral(length - 1, times, t)

spiral(150, 0, t)

screen.exitonclick()
