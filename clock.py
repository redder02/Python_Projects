#Pranjal Aggarwal
#20/october/2023

import turtle
import time

# Create a Turtle object
t = turtle.Turtle()

# Set the background color to white
screen = turtle.Screen()
screen.bgcolor('white')

# Set the pen's properties for displaying the time
t.penup()
t.goto(0, 0)  # Center of the screen
t.pendown()
t.hideturtle()  # Hide the turtle cursor

# Customize the font size and style
font_style = ("Arial", 36, "bold")

while True:
    t.clear()  # Clear the previous time display
    curr_time = time.ctime().split()[3]  # Extract the time part of the date

    # Display the time in the center of the screen
    t.write(curr_time, align="center", font=font_style)

    # Wait for 1 second before updating the time
    time.sleep(1)

