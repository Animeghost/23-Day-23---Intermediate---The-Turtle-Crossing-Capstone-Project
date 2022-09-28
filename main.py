import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard



screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
score = Scoreboard()
screen.listen()
screen.onkeypress(fun=player.move_up,key='Up')
loop=0
game_is_on = True
while game_is_on:
    increse=0.1
    time.sleep(increse)
    screen.update()
    
    #print(loop,' run ,0.1 seconds',loop%10,'modulo')
    #detect collision with the cieling
    if player.ycor() > 280:
        
        player.refresh()
        score.score_num += 1
        car.refresh()
        
        score.score()
    
    # creates cars for level and increases the amount of cars being created per level
    if player.ycor() < 280 :
        car.more_cars()
        car.car_move()
        if score.score_num >= 12:
            car.more_cars()
        
    # detect collision with cars
    for cars in car.cars:
        if player.distance(cars) < 10:
            score.game_over()
            game_is_on = False

    
screen.exitonclick()
    
    
    
    