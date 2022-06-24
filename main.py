from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

is_eating = True

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while is_eating:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect food collision
    if snake.head.distance(food) < 15:
        food.refresh()
        score.update_score()
        screen.bgcolor("yellow")
        screen.bgcolor("black")
        snake.extend()

    # detect wall collision
    if snake.head.xcor() > 280 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        screen.bgcolor("red")
        screen.bgcolor("black")
        score.game_over()
        is_eating = False

    # detect tail collision
    for segment in snake.snake_body[1:]:
        if snake.head.distance(segment) < 10:
            screen.bgcolor("green")
            screen.bgcolor("black")
            score.game_over()
            is_eating = False
screen.exitonclick()
