
import turtle


wn = turtle.Screen()
wn.title("Pong by Babacar")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)


# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)  # Sets animation speed to maximum speed
paddle_a.shape("square")  # By default, the square is 20 x 20 pixels
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)  # Makes padde 5 times taller
paddle_a.penup()  # This stops turtle from drawing a line
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)  # Sets animation speed to maximum speed
paddle_b.shape("square")  # By default, the square is 20 x 20 pixels
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)  # Makes padde 5 times taller
paddle_b.penup()  # This stops turtle from drawing a line
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)  # Sets animation speed to maximum speed
ball.shape("square")  # By default, the square is 20 x 20 pixels
ball.color("white")
ball.penup()  # This stops turtle from drawing a line
ball.goto(0, 0)

# Function


# Main game loop
while True:
    wn.update()  # This updates the screen whenever the loop runs
