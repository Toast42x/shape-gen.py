import random
import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("black")
turtle.speed("normal")

# Define colors
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# Function to draw a random shape
def draw_shape():
    sides = random.randint(3, 8)  # Random number of sides (3 to 6)
    length = random.randint(50, 200)  # Random side length
    color = random.choice(colors)  # Random color

    turtle.color(color)
    for _ in range(sides):
        turtle.forward(length)
        turtle.right(360 / sides)

# Generate art
for _ in range(50):  # Draw 50 random shapes
    x = random.randint(-300, 300)  # Random x-coordinate
    y = random.randint(-300, 300)  # Random y-coordinate
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    draw_shape()

# Hide the turtle cursor
turtle.hideturtle()

# Keep the window open until manually closed
turtle.done()
