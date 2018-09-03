# coding=utf-8
import turtle

# create new pen.
pen = turtle.Turtle()

for i in range(20):
    pen.forward(i*5)
    pen.right(144)

pen.up()
pen.setpos(100,0)
pen.down()

pen.pencolor("green")

pen.begin_fill()
pen.pensize(10)
while True:
    pen.forward(200)
    pen.right(144)
    if abs(pen.pos())<101:
        break
pen.end_fill()

# end
turtle.done()


