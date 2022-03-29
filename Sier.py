import turtle

def drawTriangle(points,color,myTurtle):
    myTurtle.fillcolor(color)
    myTurtle.up()
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.down()
    myTurtle.begin_fill()
    myTurtle.goto(points[1][0],points[1][1])
    myTurtle.goto(points[2][0],points[2][1])
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.end_fill()

def mid(p1,p2):
    return ( (p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2)

def drawsierpinski(points,degree,myTurtle):
    colormap = ['blue','red','green','white','yellow',
                'violet','orange']
    drawTriangle(points,colormap[degree],myTurtle)
    if degree > 0:
        drawsierpinski([points[0],
                        mid(points[0], points[1]),
                        mid(points[0], points[2])],
                   degree-1, myTurtle)
        drawsierpinski([points[1],
                        mid(points[0], points[1]),
                        mid(points[1], points[2])],
                   degree-1, myTurtle)
        drawsierpinski([points[2],
                        mid(points[2], points[1]),
                        mid(points[0], points[2])],
                   degree-1, myTurtle)

def main():
   myTurtle = turtle.Turtle()
   myscreen = turtle.Screen()
   myPoints = [[-100,-50],[0,100],[100,-50]]
   drawsierpinski(myPoints,3,myTurtle)
   myscreen.exitonclick()

main()