import turtle
tao = turtle.Pen() 
tao.shape('turtle') 

def drawShape(n):
    for i in range(n):
        tao.forward(100)
        tao.left(360/n)
    

tao.pensize(3)
for i in range (3,12):
   drawShape(i)
