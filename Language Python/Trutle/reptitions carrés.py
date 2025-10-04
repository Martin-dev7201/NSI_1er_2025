from turtle import*
reset()
speed("fastest")
up()
goto(-500,0)
down()
couleur=1
color('orange')
for i in range(39):
    for j in range(4):
        forward(20)
        left(90)
    up()
    forward(25)
    down()
    if (i%3==0):
        color("blue")
    elif(i%3==1):
        color("green")
    else:
        color("orange")
done()    