import random
import turtle
import time
from snake import Snake
from food import Food
from scoreboard import Score

screen = turtle.Screen()
screen.setup(600,600)
screen.bgcolor('black')
screen.title('Snake stealer')
screen.tracer(0)
screen.listen()
screen.colormode(255)

snake = Snake()
food = Food()
scoreboard = Score()

screen.onkey(key='Left', fun=snake.left_move)
screen.onkey(key='Right', fun=snake.right_move)
screen.onkey(key='Up', fun=snake.up_move)
screen.onkey(key='Down', fun=snake.down_move)

snake.create_snake()

game_on = True
while game_on:
    screen.update()
    time.sleep(0.05)
    snake.move()
    if snake.pens[0].distance(food) < 15:
        snake.extend()
        scoreboard.get_points()
        food.refresh()
    if snake.pens[0].xcor()>280 or snake.pens[0].xcor()<-280 or snake.pens[0].ycor()>280 or snake.pens[0].ycor()<-280:
        snake.reset()
        scoreboard.load_score()

    for segment in snake.pens[1:]:
        if snake.pens[0].distance(segment)<10:
            snake.reset()
            scoreboard.load_score()

screen.exitonclick()