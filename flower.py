# imports n shit
from turtle import *
import colorsys

# set env
speed(0)
bgcolor('black')

# set starting point
h=.6

# loop and draw all the petals
for i in range(219):
    c=colorsys.hsv_to_rgb(h,1,1)
    pensize(i/85)
    pencolor(c)
    h+=0.0025
    circle(5-i,100)
    lt(80)
    circle(5-i,100)
    rt(100)

# close the final petal
circle(5-i,100)

# done :3
done()

# I love you Dave <3
