# coding=utf-8
import turtle

pen = turtle.Turtle()
bg = turtle.Screen()
pen.hideturtle()

# 鼻子
pen.color("#f2bed4")
pen.begin_fill()
pen.fillcolor("#facada")
pen.circle(30)
pen.end_fill()

# 椭圆
a = 1
for i in range(120):
    if 0<=i<30 or 60 <=i<90:
        a+=0.2
        pen.lt(3)
        pen.fd(a)
    else:
        a-=0.2
        pen.lt(3)
        pen.fd(a)


















turtle.done()