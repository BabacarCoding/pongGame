
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
ball.dx = 0.3
ball.dy = 0.3


# Function


def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Keyboard binding
wn.listen()  # This line tells program to listen to keyboard input
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


# Main game loop
while True:
    wn.update()  # This updates the screen whenever the loop runs

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
