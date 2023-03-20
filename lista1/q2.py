from turtle import *

color('pink')
bgcolor('green')

def draw_poly(n, sz):
    angle = 360 / n

    for i in range(n):
        forward(sz)
        left(angle)

draw_poly(8, 50)