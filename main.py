
from  turtle import Screen
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

ball = Ball()
ball.reset_position()


l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))

# Keyboard controls
screen.listen()
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")




game_is_on = True
while game_is_on:
	
	screen.update()
	ball.move()


screen.exitonclick() # Close the window on click
