# coding=utf-8
import turtle
import math

pen = turtle.Turtle()
bg = turtle.Screen()
root_list =[(0,0)]

def movePen(pen,x,y):
    pen.up()
    pen.setpos(x, y)
    pen.down()

def get_tree(pen,x,y,r,t,len,cut):
    movePen(pen,x,y)
    radio = r + r*t
    distance = len-cut*(t-1)

    if(x==0 and y==0):
        pen.lt(90)
        pen.forward(50)

    root_Pos = pen.pos()
    print("左偏移角度：", radio)
    pen.lt(radio)
    pen.forward(distance)
    pen.rt(radio)
    l_Pos = pen.pos()
    movePen(pen,root_Pos[0],root_Pos[1])
    print("右偏移角度：", radio)
    pen.rt(radio)
    pen.forward(distance)
    pen.lt(radio)
    r_Pos = pen.pos()
    return (l_Pos,r_Pos)


def main(pen):
    global root_list
    index = 0
    while len(root_list)<17:
        newList = []
        for i in root_list:
            x = i[0]
            y = i[1]
            new_root = get_tree(pen,x,y,15,index,80,10)
            newList.append(new_root[0])
            newList.append(new_root[1])

        root_list = newList
        index += 1


if __name__ == '__main__':
    main(pen)


turtle.done()