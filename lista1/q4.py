from turtle import * 

bgcolor('green')

color('blue')
speed(10)

right(90)
goto(-200, 0)

length = 200

while length > 0:
    forward(length)
    left(90)
    length = length - 2

color('green')
goto(200, 0)
color('blue')

length = 200

while length > 0:
    forward(length)
    left(89)
    length = length - 2

done()