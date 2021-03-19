from turtle import *
reset()
color('blue')
width(3)
for i in range(6):
    down()
    forward(100)
    up()
    for i in range(6):
        down()
        forward(30)
        up()
        backward(30)
        right(60)
    backward(100)
    right(60)
