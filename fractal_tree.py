#Pranjal Aggarwal
#20/october/2023
import turtle
# Create a Turtle object
t = turtle.Turtle()

# Set the background color to white
screen = turtle.Screen()
screen.bgcolor("white")

# Set the starting position and angle
t.left(90)  # Start by pointing upward
t.penup()
t.goto(0, -200)  # Move to the base of the tree
t.pendown()

# Define a function to draw a fractal tree
def fractal_tree(branch_len, t):
    if branch_len > 5:
        t.forward(branch_len)
        t.right(20)
        fractal_tree(branch_len - 15, t)
        t.left(40)
        fractal_tree(branch_len - 15, t)
        t.right(20)
        t.backward(branch_len)

# Draw the fractal tree
fractal_tree(100, t)

# Close the Turtle graphics window when clicked
screen.exitonclick()
