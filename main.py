from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time



paddle = Turtle()
screen = Screen()
screen.setup(width = 1000, height = 1000)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)
game_is_on = True


r_paddle = Paddle((450, 0))
l_paddle = Paddle((-450, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(r_paddle.up , "Up")
screen.onkey(r_paddle.down , "Down")


screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")




while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball.move()


    # Detect collision with wall
    if ball.ycor() > 480 or ball.ycor() < - 480 :
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 420 or ball.distance(l_paddle) < 50 and ball.xcor() < -420 :
        ball.bounce_x()

    # Detect when r_paddle misses
        if ball.xcor() > 480:
            ball.reset_position()

    # Detect when l_paddle misses
        if ball.xcor() > -480:
            ball.reset_position()
    



screen.exitonclick()
