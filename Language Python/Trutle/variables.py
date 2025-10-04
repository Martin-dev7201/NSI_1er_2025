from turtle import *
reset()
speed("fastest")
down()
color('blue')
lg = 10
for i in range(25) :
    for j in range(4):
        forward(lg)
        left(90)
    lg = lg + 10
done()