# coding=utf-8
import turtle

def movePen(pen,x,y):
    pen.up()
    pen.setpos(x, y)
    pen.down()

# create new pen.
pen = turtle.Turtle()
window = turtle.Screen()
window.bgcolor("#adceff")
for i in range(20):
    pen.forward(i*5)
    pen.right(90)


pen.forward(200)
#pen.right(90)

for i in range(20):
    pen.forward((20-i)*5)
    pen.right(90)

movePen(pen,0,-100)

pen.pencolor("#97ceb0")

pen.begin_fill()
pen.pensize(10)
i = 0
while True:
    pen.forward(200)
    pen.right(144)
    i+=1
    if(i == 5):
        break
pen.end_fill()


movePen(pen,0,-300)

pen.circle(20)


# end
turtle.done()


