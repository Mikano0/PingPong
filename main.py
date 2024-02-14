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


right_paddle = Paddle((450, 0))
left_paddle = Paddle((-450, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(right_paddle.up , "Up")
screen.onkey(right_paddle.down , "Down")

screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")


while game_is_on:
    time.sleep(ball.move_speed())
    screen.update()
    ball.move()


    # Detect collision with wall
    if ball.ycor() > 480 or ball.ycor() < - 480 :
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 420 or ball.distance(left_paddle) < 50 and ball.xcor() < -420 :
        ball.bounce_x()

    # Detect when right_paddle misses
        if ball.xcor() > 480:
            ball.reset_position()
            scoreboard.left_point()

    # Detect when left_paddle misses
        if ball.xcor() > -480:
            ball.reset_position()
            scoreboard.right_point()
    



screen.exitonclick()

