
from  turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)


l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()


# Keyboard controls
screen.listen()
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")




game_is_on = True
while game_is_on:
	time.sleep(0.1)
	screen.update()
	ball.move()

	# detect collision with wall
	ball.wall_bounce()

	# detect collision with paddles
	if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
		ball.bounce_x()

	# detect right paddle miss
	if ball.xcor() > 380:
		ball.reset_position()
	# detect left paddle miss
	if ball.xcor() < -380:
		ball.reset_position()



screen.exitonclick() # Close the window on click
