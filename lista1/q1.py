from turtle import * 

color('pink')
bgcolor('green')

for i in range(4):
    for j in range(4):
        forward(20 + i * 20)
        left(90)
        print(pos())

    if (i < 3):
        color('green')
        goto(pos()[0] - 10, pos()[1] - 10)
        color('pink')

done()