import turtle
tao = turtle.Pen()
tao.shape('turtle')

def P():
    '''funtion for drawing'''
    for i in range(1):
        tao.pensize(20)
        tao.pencolor('red')
        tao.left(90)
        tao.fd(200)
        tao.backward(100)
        tao.right(90)
        tao.fd(50)
        tao.circle(50,180)
        tao.fd(50)
        tao.left(180)

def r():
    for i in range(1):
        tao.pensize(10)
        tao.pencolor('yellow')
        tao.fillcolor('black')
        tao.begin_fill()
        
        tao.circle(150)

        tao.end_fill()
        
def Go(x,y):
    tao.penup()
    tao.goto(x,y)
    tao.pendown()

Go(0,-100)
r()
Go(-50,-50)
P()

