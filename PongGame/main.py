import turtle
from pong import Pong
from object import Ball
import time
from wall import Wall
from score import Scoreboard

screen = turtle.Screen()
screen.bgcolor('black')
screen.setup(800,600)
screen.listen()
screen.tracer(0)
screen.colormode(255)
screen.title("Pong Game")

ball = Ball()
wall = Wall()
wall.create_wall()
pong = Pong(370, 0)
pong2 = Pong(-370, 0)

screen.onkey(pong.move_up, "Up")
screen.onkey(pong.move_down, "Down")
screen.onkey(pong2.move_up, "w")
screen.onkey(pong2.move_down, "s")

scoreboard = Scoreboard()

game_on = True
while game_on:
    if scoreboard.end_game():
        game_on = False
    ball.move()
    ball.wall_bounce(y=295)
    pong.hit_r(ball,pong2)
    pong2.hit_l(ball,pong)
    if ball.xcor()>380:
        scoreboard.count_point_r()
        ball.reset()
    if ball.xcor()<-380:
        scoreboard.count_point_l()
        ball.reset()
    screen.update()
    time.sleep(0.005)

screen.exitonclick()

