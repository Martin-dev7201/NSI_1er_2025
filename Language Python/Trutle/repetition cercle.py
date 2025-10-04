from turtle import*
reset()
speed("fastest")
couleur=1
color('orange')
for i in range(36):
    down()
    circle(80)
    up()
    left(10)
     if (i%3==0):
        color("blue")
    elif(i%3==1):
        color("green")
    else:
        color("orange")
done()
    