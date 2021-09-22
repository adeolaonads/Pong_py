import turtle
import winsound

screen = turtle.Screen()
screen.title("Pong by @StrokeOfGeniusX")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)


# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1, outline=None)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1, outline=None)
paddle_b.penup()
paddle_b.goto(350, 0)


# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)

# Ball movement
ball.dx = 0.2
ball.dy = -0.2



# Pen (scoreboard)

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("PlayerA: 0 PlayerB: 0", align="center", font=("Verdana", 24, "normal"))

def paddle_a_up():
    y = paddle_a.ycor()
    if y < 240:
        y += 20
        paddle_a.sety(y)
    

def paddle_a_down():
    y = paddle_a.ycor()
    if y > -240:
        y -= 20
        paddle_a.sety(y)
    

def paddle_b_up():
    y = paddle_b.ycor()
    if y < 240:
        y += 20
        paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    if y > -240:
        y -= 20
        paddle_b.sety(y)


# Keybaora binding
screen.listen()
screen.onkeypress(paddle_a_up, key="w")
screen.onkeypress(paddle_a_down, key="s")
screen.onkeypress(paddle_b_up, key="Up")
screen.onkeypress(paddle_b_down, key="Down")





# Main game loop
while True:
    screen.update()
    
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    
    
    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("ball-bounce.wav", winsound.SND_ASYNC)
        
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("ball-bounce.wav", winsound.SND_ASYNC)
        
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("PlayerA: {} PlayerB: {}".format(score_a, score_b), align="center", font=("Verdana", 24, "normal"))
        
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("PlayerA: {} PlayerB: {}".format(score_a, score_b), align="center", font=("Verdana", 24, "normal"))
        
        
    # Paddle and ball collisions
    if ball.xcor() > 340  and ball.xcor() < 350 and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("ball-bounce.wav", winsound.SND_ASYNC)
        
    if ball.xcor() < -340  and ball.xcor() > -350 and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("ball-bounce.wav", winsound.SND_ASYNC)
